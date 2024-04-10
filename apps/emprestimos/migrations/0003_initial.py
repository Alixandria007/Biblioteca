# Generated by Django 5.0.4 on 2024-04-10 01:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emprestimos', '0002_remove_livros_autor_remove_livros_genero_and_more'),
        ('livros', '0002_livros_estoque_livros_imagem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
                ('quant_livros', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=[('C', 'Criado'), ('D', 'Devolvido'), ('A', 'Atrasado')], max_length=1)),
                ('leitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Emprestimo',
                'verbose_name_plural': 'Emprestimos',
            },
        ),
        migrations.CreateModel(
            name='LivroEmprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('livro_id', models.PositiveIntegerField()),
                ('slug', models.SlugField()),
                ('sinopse', models.TextField(max_length=1200)),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('paginas', models.PositiveIntegerField(default=1)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.autor')),
                ('emprestimo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emprestimos.emprestimo')),
                ('genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='livros.genero')),
            ],
            options={
                'verbose_name': 'Livro Emprestado',
                'verbose_name_plural': 'Livros Emprestados',
            },
        ),
    ]
