from django.urls import path
from . import views

app_name = "livros"

urlpatterns = [
    path('', views.index, name='index'),
    path('livro/<slug:slug>', views.livro, name='livro'),
    path('autor/<int:id>', views.autor, name='autor'),
    path('genero/<int:id>', views.genero, name='genero'),
    path('autores/', views.ver_autores, name='ver_autores'),
    path('generos/', views.ver_generos, name='ver_generos'),
    path('adicionar_emprestimo', views.adicionar_emprestimo, name='adicionar_emprestimo'),
    path('previa_emprestimo', views.previa_emprestimo, name='previa_emprestimo'),
    path('realizar_emprestimo', views.realizar_emprestimo, name='realizar_emprestimo'),
    path('remover_livro/<int:id>', views.remover_livro, name='remover_livro'),
    path('search/', views.search, name='search'),
]
