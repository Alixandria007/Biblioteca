from typing import Iterable
from django.db import models
from utils import resize_imgs

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
    sinopse_curta = models.TextField(max_length=1200, blank = True, null=True)
    sinopse_longa = models.TextField(max_length=12000, blank = True, null=True)
    estoque =  models.PositiveIntegerField(default = 1, blank = False)
    paginas = models.PositiveIntegerField(default = 1, blank = False)
    imagem = models.ImageField(upload_to='assets/imgs/%Y/%m/', null = True,)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    genero = models.ManyToManyField(to = Genero)

    def __str__(self):
        return f'{self.nome}'
    
    def save(self, *args, **kwargs ):
        img_name = str(self.imagem.name)
        super_save = super().save(*args, **kwargs)
        img_changed = False

        if self.imagem:
            img_changed = img_name != self.imagem.name

        if img_changed:
            self.imagem = resize_imgs.resize_imgs(self.imagem, 500 , True , 80)

        return super_save
        