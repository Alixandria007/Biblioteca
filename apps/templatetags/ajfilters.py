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

@register.filter
def quant_previa(previa):
    return len(previa)

@register.filter
def formt_cpf(cpf):
    cont = 0
    novo_cpf = ""

    for i in cpf:
        if cont % 3 == 0 and not cont == 0 and not cont == 9:
            novo_cpf += '.'

        if cont == 9:
            novo_cpf += '-'

        novo_cpf += i
        cont += 1

    return novo_cpf