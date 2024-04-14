# Generated by Django 5.0.4 on 2024-04-13 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_alter_livros_sinopse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livros',
            old_name='sinopse',
            new_name='sinopse_curta',
        ),
        migrations.AddField(
            model_name='livros',
            name='sinopse_longa',
            field=models.TextField(blank=True, max_length=1200, null=True),
        ),
    ]
