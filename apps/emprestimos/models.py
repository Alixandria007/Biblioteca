from django.db import models

# Create your models here.

class Autor(models.Model):

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


    nome = models.CharField(max_length = 120 , null = False, blank = False)

    def __str__(self) -> str:
        return self.nome



class Genero(models.Model):

    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

    nome = models.CharField(max_length = 120 , null = False, blank = False)

    def __str__(self):
        return f'{self.nome}'


class Livros(models.Model):

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    nome = models.CharField(max_length=120, blank = False , null = False)
    slug = models.SlugField(null = False, blank= False)
    sinopse = models.TextField(max_length=1200, blank = False, null = False)
    paginas = models.PositiveIntegerField(default = 1, blank = False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete = models.SET_NULL , null = True)

    def __str__(self):
        return f'{self.nome}'