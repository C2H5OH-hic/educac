# Generated by Django 5.1.3 on 2024-12-09 17:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('experimentos', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes')], max_length=10)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('estudiante', models.ForeignKey(limit_choices_to={'rol': 'estudiante'}, on_delete=django.db.models.deletion.CASCADE, related_name='horarios_como_estudiante', to=settings.AUTH_USER_MODEL)),
                ('experimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experimentos.experimento')),
                ('profesor', models.ForeignKey(limit_choices_to={'rol': 'profesor'}, on_delete=django.db.models.deletion.CASCADE, related_name='horarios_como_profesor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
