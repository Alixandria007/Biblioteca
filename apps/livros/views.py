from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .  import models
from apps.leitores.models import Leitor

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


def adicionar_emprestimo(request):
    livro_id = request.GET.get('livro_id', None)
    
    if not livro_id:
        messages.error(
            request,
            'Esse livro não existe.'
        )

        return redirect(request.META.get('HTTP_REFERER'))

    livro = get_object_or_404(models.Livros, id = livro_id)

    livro_nome = livro.nome
    livro_slug = livro.slug
    livro_sinopse_curta = livro.sinopse_curta
    livro_sinopse_longa = livro.sinopse_longa
    livro_imagem = livro.imagem
    livro_estoque = livro.estoque
    livro_autor = livro.autor.nome
    livro_genero = livro.genero
    livro_paginas = livro.paginas

    if livro_imagem:
        livro_imagem = livro_imagem.name
    else:
        livro_imagem = ''

    if livro_estoque == 0:
        messages.error(
            request,
            'Estoque insuficiente.'
        )

        return redirect(request.META.get('HTTP_REFERER'))
    
    if not request.session.get('previa_emprestimo'):
        request.session['previa_emprestimo'] = {}
        request.session.save()

    previa_emprestimo = request.session['previa_emprestimo']

    if livro_id in previa_emprestimo:
        messages.warning(
            request,
            'Este livro já esta adicionado.'
        )

        return redirect(request.META.get('HTTP_REFERER'))
    
    else:
        previa_emprestimo[livro_id] = {
            'id': livro_id,
            'nome': livro_nome,
            'slug' : livro_slug,
            'sinopse_curta' : livro_sinopse_curta,
            'paginas' : livro_paginas,
            'genero': [{
            'id': genero.id,
            'nome': genero.nome,
        } for genero in livro.genero.all()],
            'autor' : livro_autor,
            'imagem' : livro_imagem,
        }

        request.session.save()
        livro.save()
        

        messages.success(
            request,
            'Livro registrado com sucesso.'
        )

        return redirect(request.META.get('HTTP_REFERER'))

def previa_emprestimo(request):
    previa = request.session['previa_emprestimo']

    context = {
        'previa' : previa
    }

    return render(request, 'previa_emprestimo.html', context)

def realizar_emprestimo(request):
    import datetime
    previa = request.session['previa_emprestimo']

    if previa.get('leitor'):

        leitor = Leitor.objects.filter(leitor__username = previa['leitor']).first()


        context = {
            'leitor' : leitor,
            'previa' : previa,
            'hoje' : datetime.date.today().isoformat()
        }

    else:
        context = {
            'previa' : previa,
            'hoje' : datetime.date.today().isoformat()
        }


    return render(request, 'realizar_emprestimo.html', context)

def remover_livro(request, id):
    previa = request.session['previa_emprestimo']

    if previa.get(str(id)):
        del previa[str(id)]
        request.session.save()

        messages.success(
            request,
            "Livro apagado com sucesso"
        )
    else:
        messages.error(
            request,
            "Este livro não está adicionado a previa"
        )

    return redirect(request.META.get('HTTP_REFERER'))

def search(request):
    search = request.GET.get('search', None)

    if search == '':
        return redirect('livros:index')
    
    livros = models.Livros.objects.filter(Q(nome__icontains = search)|Q(sinopse_curta__icontains = search))

    paginator = Paginator(livros, 20)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'index.html', context)