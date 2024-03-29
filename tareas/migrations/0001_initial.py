# Generated by Django 2.2.7 on 2019-11-07 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('estado', models.SmallIntegerField(choices=[(1, 'Por Hacer'), (2, 'Haciendo'), (3, 'Hecho')], default=1)),
                ('fecha_inicial', models.DateTimeField()),
                ('fecha_final', models.DateTimeField(null=True)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
            },
        ),
    ]
