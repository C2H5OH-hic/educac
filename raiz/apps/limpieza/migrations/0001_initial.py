# Generated by Django 5.1.3 on 2024-12-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Limpieza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.TextField()),
                ('completado', models.BooleanField(default=False)),
            ],
        ),
    ]
