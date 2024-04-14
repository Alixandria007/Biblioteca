from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .  import models

# Create your views here.

def index(request):
    livros = models.Livros.objects.all().order_by('-pk')

    paginator = Paginator(livros, 20)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title' : 'Catalogo de Livros'
    }

    return render(request, 'index.html', context)

def livro(request, slug):
    livro_ = models.Livros.objects.filter(slug = slug).first()

    context = {
        'livro' : livro_ 
    }

    return render(request, 'livro.html', context)

def autor(request,id):
    autor_ = models.Livros.objects.filter(autor__id = id).order_by('-id')

    paginator = Paginator(autor_, 20)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    autor_name = models.Autor.objects.filter(id = id).first()

    context = {
        'page_obj': page_obj,
        'title' : autor_name.nome
    }

    return render(request, 'index.html', context)

def genero(request,id):
    genero_ = models.Livros.objects.filter(genero__id = id).order_by('-id')

    paginator = Paginator(genero_, 20)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    genero_name = models.Genero.objects.filter(id = id).first()

    context = {
        'page_obj': page_obj,
        'title' : genero_name.nome
    }

    return render(request, 'index.html', context)

def ver_autores(request):
    autores = models.Autor.objects.all()

    context = {
        'autores' : autores 
    }
    

    return render(request, 'ver_autores.html', context)