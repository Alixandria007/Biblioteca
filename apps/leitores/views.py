from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from . import forms

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

        usuario = user_form.save()

        leitor = leitor_form.save(commit=False)
        leitor.leitor = usuario
        leitor.save()

        messages.success(
            request,
            "Leitor cadastrado com sucesso."
        )

            

    return render(request, 'adicionar_usuario.html', context)