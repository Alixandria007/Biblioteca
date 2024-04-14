from django.template import Library
from apps.livros import models

register = Library()

@register.filter
def contar_livros(autor_id):
    livros = models.Livros.objects.filter(autor__id = autor_id).count()
    return livros

@register.filter
def contar_paginas(autor_id):
    livros = models.Livros.objects.filter(autor__id = autor_id)
    paginas = 0

    for livro in livros:
        paginas += livro.paginas

    return paginas