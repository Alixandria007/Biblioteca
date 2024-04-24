from django.shortcuts import render, redirect
import datetime
from apps.leitores.models import Leitor
from apps.livros.models import Genero,Autor,Livros
from django.core.paginator import Paginator
from django.contrib import messages
from . import models
# Create your views here.

def criar_emprestimo(request):

    if not request.session['leitor']:

        messages.error(
            request,
            'Não há leitor definido para poder criar o emprestimo.'
        )

        return redirect('livros:realizar_emprestimo')
    
    if not request.session.get('previa_emprestimo'):
        messages.error(
            request,
            'Não há livros em sua previa.'
        )

        return redirect('livros:index')
    

    leitor = Leitor.objects.filter(leitor__username = request.session['leitor']).first()
    previa = request.session['previa_emprestimo']
    data_final = request.GET.get('data-final')

    emprestimo = models.Emprestimo(
        leitor = leitor,
        data_inicial = datetime.date.today().isoformat(),
        data_final = data_final,
        quant_livros = len(previa),
        status = 'C'
    )

    emprestimo.save()


    models.LivroEmprestimo.objects.bulk_create(
        models.LivroEmprestimo(
            emprestimo = emprestimo,
            nome = l['nome'],
            livro_id = l['id'],
            slug = l['slug'],
            sinopse = l['sinopse_curta'],
            quantidade = 1,
            paginas = l['paginas'],
            autor = Autor.objects.filter(nome = l['autor']).first(),
            imagem = l['imagem']
        ) for l in previa.values()
    )

    messages.success(
        request,
        f'Emprestimo do leitor {leitor.leitor.first_name} Criado.'
    )

    del request.session['previa_emprestimo']
    del request.session['leitor']
    
    return redirect('livros:index')


def consultar_emprestimos(request):
    emprestimos = models.Emprestimo.objects.all()

    for emprestimo in emprestimos:

        if emprestimo.status == "C" and datetime.date.today() > emprestimo.data_final:
            emprestimo.status = "A"
            emprestimo.save()

    paginator = Paginator(emprestimos, 10)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    context = {
        'emprestimos' : page_obj,
        'search_emprestimo' : True,
    }
    

    return render(request, 'consultar_emprestimo.html', context)

def emprestimo(request, id):
    emprestimo_ = models.Emprestimo.objects.filter(id = id).first()

    livro_emprestimo = models.LivroEmprestimo.objects.filter(emprestimo__id = id).all()

    context = {
        'emprestimo': emprestimo_,
        'livros': livro_emprestimo,
        'search_leitor' : True,
    }

    return render(request, 'emprestimo.html', context)


def encerrar_emprestimo(request,id):

    emprestimo = models.Emprestimo.objects.filter(id = id).first()

    if emprestimo.status == "D":
        messages.warning(
            request,
            "Este Emprestimo já foi encerrado."
        )

        return redirect(request.META["HTTP_REFERER"])

    emprestimo.status = 'D'
    emprestimo.save()

    messages.success(
        request,
        f"Emprestimo Nº{emprestimo.id} encerrado."
    )

    return redirect(request.META["HTTP_REFERER"])

def ver_atrasos(request):
    emprestimos_ = models.Emprestimo.objects.all()

    for emprestimo in emprestimos_:

        if emprestimo.status == "C" and datetime.date.today() > emprestimo.data_final:
            emprestimo.status = "A"
            emprestimo.save()

    emprestimos_atrasados = models.Emprestimo.objects.filter(status = "A" ).all()

    paginator = Paginator(emprestimos_atrasados, 10)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    context = {
        'emprestimos' : page_obj,
        'search_emprestimo' : True,
        'atraso' : "Atrasados"
    }

    return render(request, 'consultar_emprestimo.html', context)