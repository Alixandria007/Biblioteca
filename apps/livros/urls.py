from django.urls import path
from . import views

app_name = "livros"

urlpatterns = [
    path('', views.index, name='index'),
    path('livro/<slug:slug>', views.livro, name='livro'),
    path('autor/<int:id>', views.autor, name='autor'),
    path('genero/<int:id>', views.genero, name='genero'),
    path('autores/', views.ver_autores, name='ver_autores'),
    path('adicionar_emprestimo', views.adicionar_emprestimo, name='adicionar_emprestimo'),
]
