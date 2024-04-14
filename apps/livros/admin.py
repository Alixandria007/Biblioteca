from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):

    list_display = 'id' , 'nome'
    list_display_links = 'id',
    list_per_page = 10
    ordering = '-id',

@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):

    list_display = 'id' , 'nome'
    list_display_links = 'id',
    list_per_page = 10
    ordering = '-id',

@admin.register(models.Livros)
class LivrosAdmin(admin.ModelAdmin):

    list_display = 'id', 'nome' , 'paginas' , 'autor'
    list_display_links = 'id',
    list_editable  = 'nome', 'paginas'
    list_per_page = 10
    ordering = '-id',

    prepopulated_fields = {
        'slug' : ('nome',),
    }

