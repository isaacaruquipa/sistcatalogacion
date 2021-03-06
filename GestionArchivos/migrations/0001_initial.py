# Generated by Django 3.2.13 on 2022-06-17 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ambiente',
                'verbose_name_plural': 'Ambientes',
                'db_table': 'ambientes',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_eliminacion', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Archivo',
                'verbose_name_plural': 'Archivos',
                'db_table': 'archivos',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
                'db_table': 'lugares',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='ProgramasCursosActividades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_finalizacion', models.DateTimeField(blank=True, null=True)),
                ('version', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Programa/Curso/Actividad',
                'verbose_name_plural': 'Programas/Cursos/Actividades',
                'db_table': 'programas_cursos_actividades',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fila', models.IntegerField()),
                ('columna', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Ubicaci??n',
                'verbose_name_plural': 'Ubicaciones',
                'db_table': 'ubicaciones',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoArchivo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('id_archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionArchivos.archivo')),
            ],
            options={
                'verbose_name': 'Tipo de archivo',
                'verbose_name_plural': 'Tipos de archivos',
                'db_table': 'tipos_archivos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Gabeta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cod_gabeta', models.CharField(max_length=100)),
                ('id_ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionArchivos.ambiente')),
            ],
            options={
                'verbose_name': 'Gabeta',
                'verbose_name_plural': 'Gabetas',
                'db_table': 'gabetas',
                'ordering': ['cod_gabeta'],
            },
        ),
        migrations.CreateModel(
            name='ArchivoUbicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionArchivos.archivo')),
                ('id_pca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionArchivos.programascursosactividades')),
                ('id_ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionArchivos.ubicacion')),
            ],
            options={
                'verbose_name': 'Archivo Ubicaci??n',
                'verbose_name_plural': 'Archivos Ubicaciones',
                'db_table': 'archivos_ubicaciones',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='ambiente',
            name='id_lugar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionArchivos.lugar'),
        ),
    ]
