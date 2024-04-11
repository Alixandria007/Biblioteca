from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Leitor)
class LeitorAdmin(admin.ModelAdmin):

    list_display = 'id', 'leitor', 'idade', 'cpf',
    list_display_links = 'id',
    ordering = '-id',