from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):

    list_display = 'id', 'leitor', 'data_inicial', 'data_final', 'status'
    list_display_links = 'id',
    ordering = '-id',

@admin.register(models.LivroEmprestimo)
class LivroEmprestimoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'quantidade', 'paginas', 'autor', 'genero'
    list_display_links = 'id',
    ordering = '-id',