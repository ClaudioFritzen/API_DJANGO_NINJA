# Generated by Django 5.1.6 on 2025-02-23 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treino', '0002_aulasconcluidas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aulasconcluidas',
            old_name='faixa',
            new_name='faixa_atual',
        ),
    ]
