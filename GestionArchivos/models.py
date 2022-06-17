from django.db import models

# Modelo archivo
class Archivo(models.Model):
    # campo id de tipo incrementable en mariadb
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)    
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'archivos'
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'
        ordering = ['titulo']



# Modelo tipo_archivo campos(id, id_archivo, nombre, descripcion)
class TipoArchivo(models.Model):
    id = models.AutoField(primary_key=True)
    id_archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipos_archivos'
        verbose_name = 'Tipo de archivo'
        verbose_name_plural = 'Tipos de archivos'
        ordering = ['nombre']




# Modelo Programas_cursos_actividades(id, nombre, tipo, fecha_inicio, fecha_modificacion, fecha_finalizacion, version)

class ProgramasCursosActividades(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)
    version = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'programas_cursos_actividades'
        verbose_name = 'Programa/Curso/Actividad'
        verbose_name_plural = 'Programas/Cursos/Actividades'
        ordering = ['tipo']


#  Modelo Ubicacion(id, nombre, descripcion, fila, columna)
class Ubicacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fila = models.IntegerField()
    columna = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'ubicaciones'
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'
        ordering = ['nombre']



# Modelo Lugar (id, nombre, ubicacion, descripcion)
class Lugar(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'lugares'
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        ordering = ['nombre']


# Modelo Ambiente (id, id_lugar, nombre)
class Ambiente(models.Model):
    id = models.AutoField(primary_key=True)
    id_lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'ambientes'
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'
        ordering = ['nombre']




# Modelo Gabeta (id, id_ambiente, cod_gabeta)
class Gabeta(models.Model):
    id = models.AutoField(primary_key=True)
    id_ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    cod_gabeta = models.CharField(max_length=100)

    def __str__(self):
        return self.cod_gabeta

    class Meta:
        db_table = 'gabetas'
        verbose_name = 'Gabeta'
        verbose_name_plural = 'Gabetas'
        ordering = ['cod_gabeta']
    


    










# relacion muchos a muchos de Modelo Archivo, Ubicacion, ProgramasCursosActividades
class ArchivoUbicacion(models.Model):
    id = models.AutoField(primary_key=True)
    id_archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE)
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    id_pca= models.ForeignKey(ProgramasCursosActividades, on_delete=models.CASCADE)   

    class Meta:
        db_table = 'archivos_ubicaciones'
        verbose_name = 'Archivo Ubicación'
        verbose_name_plural = 'Archivos Ubicaciones'
        ordering = ['id']



# Importar usuario de django
from django.contrib.auth.models import User


# Modelo Estudiantes(id_usuario, matricula) hereda de User
class Estudiante(models.Model):
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=50)

    class Meta:
        db_table = 'estudiantes'
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['matricula']

# Modelo Docentes (id_usuario, fecha_nombramiento) hereda de User
class Docente(models.Model):
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nombramiento = models.DateTimeField()

    class Meta:
        db_table = 'docentes'
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering = ['fecha_nombramiento']


# Modelo administrador (id_usuario, nro_contrato) hereda de User
class Administrador(models.Model):
    id_usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nro_contrato = models.CharField(max_length=50)

    class Meta:
        db_table = 'administradores'
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        ordering = ['nro_contrato']














