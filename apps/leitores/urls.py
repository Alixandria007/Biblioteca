from django.urls import path
from . import views

app_name = "leitores"

urlpatterns = [
    path('adicionar/', views.adicionar, name='adicionar'),
    path('consultar/', views.consultar, name='consultar'),
]
