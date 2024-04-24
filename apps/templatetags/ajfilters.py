from django.template import Library
from apps.livros import models
from apps.emprestimos.models import Emprestimo

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
def contar_livros_genero(genero_id):
    livros = models.Livros.objects.filter(genero__id = genero_id).count()
    return livros

@register.filter
def contar_paginas_genero(genero_id):
    livros = models.Livros.objects.filter(genero__id = genero_id)
    paginas = 0

    for livro in livros:
        paginas += livro.paginas

    return paginas

@register.filter
def quant_previa(previa):
    return len(previa)

@register.filter
def contar_emprestimos(id_user):
    return Emprestimo.objects.filter(leitor__id = id_user).count()

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