# Generated by Django 4.2.19 on 2025-02-17 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_aluno'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cidade',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]
