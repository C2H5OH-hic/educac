# Generated by Django 5.1.3 on 2024-12-02 06:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('experimentos', '0002_initial'),
        ('limpieza', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='limpieza',
            name='asignado_a',
            field=models.ForeignKey(limit_choices_to={'rol': 'estudiante'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='limpieza',
            name='experimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experimentos.experimento'),
        ),
    ]
