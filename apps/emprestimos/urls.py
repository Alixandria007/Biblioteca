from django.urls import path
from . import views

app_name = 'emprestimos'

urlpatterns = [
    path('criar_emprestimo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('consultar_emprestimo/', views.consultar_emprestimos, name='consultar_emprestimos'),
]
