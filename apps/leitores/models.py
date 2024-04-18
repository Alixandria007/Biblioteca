from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Leitor(models.Model):
    class Meta:
        verbose_name = "Leitor"
        verbose_name_plural = "Leitores"

    leitor = models.ForeignKey(User, on_delete = models.CASCADE)
    idade = models.PositiveIntegerField(default = 1)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length = 15, blank = True, null=True)
    cpf = models.CharField(max_length = 11 ,unique = True, blank=False)

    def __str__(self):
        return f"Leitor {self.leitor.username}"