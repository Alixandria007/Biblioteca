from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from . import forms, models
from apps.emprestimos.models import Emprestimo

# Create your views here.

def adicionar(request):

    context = {
        'userform' : forms.UserForm(
             data = request.POST or None
        ),
        'leitorform': forms.LeitorForm(
             data = request.POST or None
        )
    }

    leitor_form = context['leitorform']
    user_form = context["userform"]

    if request.method == "POST":
        if not leitor_form.is_valid() or not user_form.is_valid():
            messages.error(
                request,
                "Existem erros no formulario."
            )
            
            return render(request, 'adicionar_usuario.html', context)

        usuario = user_form.save(commit=False)

        cont = 2
        if User.objects.filter(username = usuario.first_name).exists():
            while True:

                usuario.username = f"{usuario.first_name}_{cont}"

                if not User.objects.filter(username = f"{usuario.first_name}_{cont}").exists():
                    usuario.save()
                    break

                cont += 1
        else:
            usuario.username = usuario.first_name
            usuario.save()

        leitor = leitor_form.save(commit=False)
        leitor.leitor = usuario
        leitor.save()

        messages.success(
            request,
            "Leitor cadastrado com sucesso."
        )

            

    return render(request, 'adicionar_usuario.html', context)

def consultar(request):
    leitor = models.Leitor.objects.all()

    paginator = Paginator(leitor, 10)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    context = {
        'leitores' : page_obj,
        'search_leitor' : True,
    }
    

    return render(request, 'consultar_usuario.html', context)

def search(request):
    search = request.GET.get('search', None)

    if search == '':
        return redirect('leitores:consultar')

    
    leitores = models.Leitor.objects.filter(Q(leitor__first_name__icontains = search)|Q(leitor__last_name__icontains = search)| Q(cpf__icontains = search))

    paginator = Paginator(leitores, 20)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    context = {
        'leitores': page_obj,
        'search_leitor' : True,
    }

    return render(request, 'consultar_usuario.html', context)

def usuario(request, id):

    leitor = models.Leitor.objects.filter(id = id).first()

    context = {
        'leitor': leitor,
        'search_leitor' : True,
    }

    return render(request, 'usuario.html', context)

def adicionar_emprestimo(request, id):

    

    leitor = models.Leitor.objects.filter(id = id).first()

    previa = request.session
    previa['leitor'] = leitor.leitor.username
    request.session.save()
    
    if Emprestimo.objects.filter(status__in = ["C", "A"] , leitor__leitor__username =  request.session['leitor']).exists():
        messages.error(
            request,
            'O Leitor já possui um emprestimo pendente.'
        )

        del request.session['leitor']
        request.session.save()
        
        return redirect('livros:realizar_emprestimo')

    if request.session.get("previa_emprestimo"):
        return redirect("livros:realizar_emprestimo")
    else:
        return redirect("livros:index")