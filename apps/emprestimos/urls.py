from django.urls import path
from . import views

app_name = 'emprestimos'

urlpatterns = [
    path('criar_emprestimo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('consultar_emprestimo/', views.consultar_emprestimos, name='consultar_emprestimos'),
    path('ver_atrasos/', views.ver_atrasos, name='ver_atrasos'),
    path('emprestimo/<int:id>', views.emprestimo, name='emprestimo'),
    path('encerrar/<int:id>', views.encerrar_emprestimo, name='encerrar_emprestimo'),
]
