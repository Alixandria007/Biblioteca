from django.db import models
from django.contrib.auth.models import User
from apps.leitores.models import Leitor
from apps.livros.models import Autor,Genero

# Create your models here.

class Emprestimo(models.Model):
    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = "Emprestimos"

    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    data_inicial = models.DateField(null = False, blank = False)
    data_final = models.DateField(null = False, blank = False)
    quant_livros = models.PositiveIntegerField(default = 1)
    status = models.CharField(
        null = False,
        max_length = 1,
        choices = {
            'C' : 'Criado',
            'D' : 'Devolvido',
            'A' : 'Atrasado'
        })
    
    def __str__(self) -> str:
        return f"Emprestimo nº{self.pk}"
    
class LivroEmprestimo(models.Model):
    class Meta:
        verbose_name = 'Livro Emprestado'
        verbose_name_plural = "Livros Emprestados"

    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120, blank = False , null = False)
    livro_id = models.PositiveIntegerField()
    slug = models.SlugField(null = False, blank= False)
    sinopse = models.TextField(max_length=1200, blank = False, null = False)
    quantidade =  models.PositiveIntegerField(default = 1, blank = False)
    paginas = models.PositiveIntegerField(default = 1, blank = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    imagem = models.CharField( max_length = 1200, null=True, default=None)

    def __str__(self) -> str:
        return f"Livro Emprestado no pedido nº{self.emprestimo}"
