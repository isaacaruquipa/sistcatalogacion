from django.contrib import admin

# importar todos los modelos de la aplicacion
from GestionArchivos.models import *

# Registro de modelos
#  titulo = models.CharField(max_length=100)
#  fecha_creacion = models.DateTimeField(auto_now_add=True)    
#  fecha_modificacion = models.DateTimeField(auto_now=True)
#  fecha_eliminacion = models.DateTimeField(null=True, blank=True)

@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">insert_drive_file</i>'
    list_display = ('titulo', 'fecha_creacion', 'fecha_modificacion', 'fecha_eliminacion')
    list_filter = ('fecha_creacion', 'fecha_modificacion', 'fecha_eliminacion')
    search_fields = ('titulo',)


# admin.site.register(Ubicacion)
# nombre = models.CharField(max_length=100)
    # descripcion = models.TextField()
    # fila = models.IntegerField()
    # columna = models.IntegerField()
@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">location_on</i>'
    list_display = ('nombre', 'descripcion', 'fila', 'columna')
    list_filter = ('fila', 'columna')
    search_fields = ('nombre',)



# Modelo (ProgramasCursosActividades)
# tipo = models.CharField(max_length=100)
#     fecha_inicio = models.DateTimeField()
#     fecha_modificacion = models.DateTimeField(auto_now=True)
#     fecha_finalizacion = models.DateTimeField(null=True, blank=True)
#     version = models.CharField(max_length=20)
@admin.register(ProgramasCursosActividades)

class ProgramasCursosActividadesAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">assignment</i>'
    list_display = ('tipo', 'fecha_inicio', 'fecha_modificacion', 'fecha_finalizacion', 'version')
    list_filter = ('fecha_inicio', 'fecha_modificacion', 'fecha_finalizacion', 'version')
    search_fields = ('tipo',)


# admin.site.register(Lugar)
# nombre = models.CharField(max_length=100)
#     ubicacion = models.CharField(max_length=100)
#     descripcion = models.TextField()

@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">location_on</i>'
    list_display = ('nombre', 'ubicacion', 'descripcion')
    list_filter = ('ubicacion',)
    search_fields = ('nombre',)


# admin.site.register(Ambiente)
# nombre = models.CharField(max_length=100)

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">location_on</i>'
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)


# admin.site.register(Gabeta)

    # cod_gabeta = models.CharField(max_length=100)
@admin.register(Gabeta)
class GabetaAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">location_on</i>'
    list_display = ('cod_gabeta',)
    list_filter = ('cod_gabeta',)
    search_fields = ('cod_gabeta',)




# admin.site.register(ArchivoUbicacion)
# id_archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE)
#     id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
#     id_pca= models.ForeignKey(ProgramasCursosActividades, on_delete=models.CASCADE) 
@admin.register(ArchivoUbicacion)
class ArchivoUbicacionAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">location_on</i>'
    list_display = ('id_archivo', 'id_ubicacion', 'id_pca')
    list_filter = ('id_archivo', 'id_ubicacion', 'id_pca')
    search_fields = ('id_archivo', 'id_ubicacion', 'id_pca')


# admin.site.register(TipoArchivo)
# nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()

@admin.register(TipoArchivo)
class TipoArchivoAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">insert_drive_file</i>'
    list_display = ('nombre', 'descripcion')
    list_filter = ('nombre', 'descripcion')
    search_fields = ('nombre',)



# Registrar modelo Estudiante
#  matricula = models.CharField(max_length=50)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">person</i>'
    list_display = ('matricula',)
    list_filter = ('matricula',)
    search_fields = ('matricula',)


# Registrar modelo Docente 
# fecha_nombramiento = models.DateTimeField()
@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">person</i>'
    list_display = ('fecha_nombramiento',)
    list_filter = ('fecha_nombramiento',)
    search_fields = ('fecha_nombramiento',)



# Registrar modelo Administrador
# nro_contrato = models.CharField(max_length=50)

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">person</i>'
    list_display = ('nro_contrato',)
    list_filter = ('nro_contrato',)
    search_fields = ('nro_contrato',)
