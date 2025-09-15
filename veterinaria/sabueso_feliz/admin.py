from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Direccion, Sucursal, Tipo_Documento, Cargo, Empleado, Raza, Duenio, Perro,
    PerroxDuenio, Vacuna, Calendario_Vacunas, Sintomas, Diagnostico, Medicamentos,
    Stock, Consultas, Medicamentos_Recetados, SintomasxConsulta, DiagnosticoxConsulta,
    Estado_Duenio, Estado_Consulta, Historial_Consulta
)

# Registro de modelos con configuraciones básicas
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'barrio', 'ciudad', 'pais')
    search_fields = ('calle', 'barrio', 'ciudad', 'pais')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'descripcion')
    search_fields = ('direccion__calle', 'descripcion')

@admin.register(Tipo_Documento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descripcion')
    search_fields = ('tipo', 'descripcion')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'descripcion')
    search_fields = ('cargo', 'descripcion')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('numDoc', 'nombre', 'apellido', 'tipoDoc', 'cargo', 'sucursal', 'es_supervisor')
    search_fields = ('nombre', 'apellido', 'numDoc')
    list_filter = ('tipoDoc', 'cargo', 'sucursal', 'es_supervisor')

@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    list_display = ('raza', 'denominacion', 'altura_max_hembra', 'peso_max_hembra')
    search_fields = ('raza', 'denominacion')

@admin.register(Duenio)
class DuenioAdmin(admin.ModelAdmin):
    list_display = ('telefono', 'nombre', 'apellido')
    search_fields = ('nombre', 'apellido', 'telefono')

@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ('num_hist_clinica', 'nombre', 'sucursal', 'raza')
    search_fields = ('nombre', 'num_hist_clinica')
    list_filter = ('sucursal', 'raza')

@admin.register(PerroxDuenio)
class PerroxDuenioAdmin(admin.ModelAdmin):
    list_display = ('perro', 'duenio', 'fecha_inicio', 'estado')
    search_fields = ('perro__nombre', 'duenio__nombre')
    list_filter = ('estado',)

@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = ('vacuna', 'laboratorio', 'dosisxgramo')
    search_fields = ('vacuna', 'laboratorio')

@admin.register(Calendario_Vacunas)
class CalendarioVacunasAdmin(admin.ModelAdmin):
    list_display = ('perro', 'vacuna', 'fecha_programada_vacuna', 'empleado')
    search_fields = ('perro__nombre', 'vacuna__vacuna')
    list_filter = ('fecha_programada_vacuna', 'empleado')

@admin.register(Sintomas)
class SintomasAdmin(admin.ModelAdmin):
    list_display = ('sintoma', 'descripcion')
    search_fields = ('sintoma', 'descripcion')

@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('diagnostico', 'descripcion')
    search_fields = ('diagnostico', 'descripcion')

@admin.register(Medicamentos)
class MedicamentosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio', 'fecha_ultima_compra', 'cant_minima')
    search_fields = ('nombre', 'laboratorio')
    list_filter = ('fecha_ultima_compra',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('cod_stock', 'medicamento', 'sucursal', 'cant_stock')
    search_fields = ('medicamento__nombre', 'sucursal__direccion__calle')
    list_filter = ('sucursal',)

@admin.register(Consultas)
class ConsultasAdmin(admin.ModelAdmin):
    list_display = ('num_consulta', 'perro', 'sucursal', 'fecha_entrada', 'empleado', 'estado')
    search_fields = ('perro__nombre', 'num_consulta', 'diagnostico')
    list_filter = ('sucursal', 'fecha_entrada', 'estado')

@admin.register(Medicamentos_Recetados)
class MedicamentosRecetadosAdmin(admin.ModelAdmin):
    list_display = ('medicamento', 'consulta', 'periodicidad')
    search_fields = ('medicamento__nombre', 'consulta__num_consulta')

@admin.register(SintomasxConsulta)
class SintomasxConsultaAdmin(admin.ModelAdmin):
    list_display = ('consulta', 'sintoma')
    search_fields = ('sintoma__sintoma', 'consulta__num_consulta')
    list_filter = ('sintoma',)

@admin.register(DiagnosticoxConsulta)
class DiagnosticoxConsultaAdmin(admin.ModelAdmin):
    list_display = ('diagnostico', 'consulta')
    search_fields = ('diagnostico__diagnostico', 'consulta__num_consulta')
    list_filter = ('diagnostico',)

@admin.register(Estado_Duenio)
class EstadoDuenioAdmin(admin.ModelAdmin):
    list_display = ('cod_estado', 'estado', 'descripcion')
    search_fields = ('estado', 'descripcion')

@admin.register(Estado_Consulta)
class EstadoConsultaAdmin(admin.ModelAdmin):
    list_display = ('cod_estado', 'estado', 'descripcion')
    search_fields = ('estado', 'descripcion')

@admin.register(Historial_Consulta)
class HistorialConsultaAdmin(admin.ModelAdmin):
    list_display = ('cod_hist_estado', 'cod_estado', 'fecha_inicio')
    search_fields = ('historial', 'cod_estado__estado')
    list_filter = ('fecha_inicio', 'cod_estado')