from django.urls import path
from . import views

app_name = "leitores"

urlpatterns = [
    path('adicionar/', views.adicionar, name='adicionar'),
    path('consultar/', views.consultar, name='consultar'),
    path('usuario/<int:id>/', views.usuario, name='usuario'),
    path('adicionar_emprestimo/<int:id>', views.adicionar_emprestimo, name='adicionar_emprestimo'),
    path('search/', views.search, name='search'),
]
