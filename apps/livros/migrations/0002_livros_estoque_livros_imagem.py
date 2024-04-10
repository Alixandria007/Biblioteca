# Generated by Django 5.0.4 on 2024-04-10 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='estoque',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='livros',
            name='imagem',
            field=models.ImageField(null=True, upload_to='assets/imgs/%Y/%m/'),
        ),
    ]