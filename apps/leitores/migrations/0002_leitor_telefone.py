# Generated by Django 5.0.4 on 2024-04-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leitores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leitor',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]