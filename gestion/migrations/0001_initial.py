# Generated by Django 3.2.14 on 2022-11-22 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('especialidad', models.CharField(max_length=150, verbose_name='Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('obra_social', models.CharField(max_length=150, verbose_name='Obra Social')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=None, verbose_name='Fecha')),
                ('observacion', models.CharField(max_length=150, verbose_name='Observacion')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.paciente')),
            ],
        ),
    ]
