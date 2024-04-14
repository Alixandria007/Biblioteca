from django.shortcuts import render
from django.core.paginator import Paginator
from .  import models

# Create your views here.

def index(request):
    livros = models.Livros.objects.all().order_by('-pk')

    paginator = Paginator(livros, 20)
    page_number = request.GET.get('page', None)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'index.html', context)

def livro(request, slug):
    livro_ = models.Livros.objects.filter(slug = slug).first()

    context = {
        'livro' : livro_ 
    }

    return render(request, 'livro.html', context)