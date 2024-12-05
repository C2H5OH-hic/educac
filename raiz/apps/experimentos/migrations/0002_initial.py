# Generated by Django 5.1.3 on 2024-12-02 06:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('experimentos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='experimento',
            name='estudiantes',
            field=models.ManyToManyField(limit_choices_to={'rol': 'estudiante'}, related_name='experimentos_participados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experimento',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experimentos_dirigidos', to=settings.AUTH_USER_MODEL),
        ),
    ]
