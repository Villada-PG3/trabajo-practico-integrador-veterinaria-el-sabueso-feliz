from django.db import models
from django.core.validators import MinValueValidator

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
        constraints = [
            models.UniqueConstraint(fields=['calle', 'barrio', 'numero', 'ciudad', 'pais'], name='unique_direccion')
        ]

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.barrio}, {self.ciudad}, {self.pais}"

class Sucursal(models.Model):
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        constraints = [
            models.UniqueConstraint(fields=['direccion'], name='unique_sucursal')
        ]

    def __str__(self):
        return f"Sucursal {self.direccion}"

class Tipo_Documento(models.Model):
    tipo = models.CharField(max_length=50, primary_key=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documento"

    def __str__(self):
        return self.tipo

class Cargo(models.Model):
    cargo = models.CharField(max_length=50, primary_key=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.cargo

class Empleado(models.Model):
    matricula_habilitante = models.CharField(max_length=50, blank=True, null=True)
    numDoc = models.IntegerField(primary_key=True)
    tipoDoc = models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    es_supervisor = models.BooleanField(default=False)
    es_supervisor_suplente = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Raza(models.Model):
    raza = models.CharField(max_length=100, primary_key=True)
    denominacion = models.CharField(max_length=100)
    cuidados_especiales = models.TextField(blank=True)
    altura_max_hembra = models.IntegerField(validators=[MinValueValidator(0)])
    altura_min_hembra = models.IntegerField(validators=[MinValueValidator(0)])
    peso_max_hembra = models.IntegerField(validators=[MinValueValidator(0)])
    peso_min_hembra = models.IntegerField(validators=[MinValueValidator(0)])
    altura_max_macho = models.IntegerField(validators=[MinValueValidator(0)])
    altura_min_macho = models.IntegerField(validators=[MinValueValidator(0)])
    peso_max_macho = models.IntegerField(validators=[MinValueValidator(0)])
    peso_min_macho = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"

    def __str__(self):
        return self.raza

class Duenio(models.Model):
    telefono = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Perro(models.Model):
    num_hist_clinica = models.IntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name = "Perro"
        verbose_name_plural = "Perros"
        constraints = [
            models.UniqueConstraint(
                fields=['num_hist_clinica', 'sucursal'],
                name='unique_perro',
                include=['num_hist_clinica', 'sucursal']
            )
        ]
        indexes = [
            models.Index(fields=['num_hist_clinica', 'sucursal'])
        ]

    def __str__(self):
        return self.nombre

class PerroxDuenio(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    duenio = models.ForeignKey(Duenio, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default='2000-01-01')
    fecha_fin = models.DateField( default='2000-01-01')
    estado = models.ForeignKey('Estado_Duenio', on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = "Perro por Dueño"
        verbose_name_plural = "Perros por Dueño"
        constraints = [
            models.UniqueConstraint(fields=['perro', 'duenio'], name='unique_perroxduenio')
        ]

    def __str__(self):
        return f"{self.perro} - {self.duenio}"

class Vacuna(models.Model):
    vacuna = models.CharField(max_length=100, primary_key=True)
    laboratorio = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    dosisxgramo = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Vacuna"
        verbose_name_plural = "Vacunas"

    def __str__(self):
        return self.vacuna

class Calendario_Vacunas(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    fecha_programada_vacuna = models.DateField()
    fecha_real_vacuna = models.DateField(blank=True, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    dosis = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Calendario de Vacunas"
        verbose_name_plural = "Calendarios de Vacunas"
        constraints = [
            models.UniqueConstraint(fields=['perro', 'vacuna'], name='unique_calendario_vacunas')
        ]

    def __str__(self):
        return f"{self.perro} - {self.vacuna}"

class Sintomas(models.Model):
    sintoma = models.CharField(max_length=100, primary_key=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Síntoma"
        verbose_name_plural = "Síntomas"

    def __str__(self):
        return self.sintoma

class Diagnostico(models.Model):
    diagnostico = models.CharField(max_length=100, primary_key=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Diagnóstico"
        verbose_name_plural = "Diagnósticos"

    def __str__(self):
        return self.diagnostico

class Medicamentos(models.Model):
    id_med = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    fecha_ultima_compra = models.DateField()
    cant_minima = models.IntegerField()  
    dosis = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"

    def __str__(self):
        return self.nombre

class Stock(models.Model):
    cod_stock = models.AutoField(primary_key=True)
    medicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cant_stock = models.IntegerField(validators=[MinValueValidator(0)])
    cant_min_sucursal = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return f"Stock {self.medicamento}"

class Consultas(models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    num_consulta = models.IntegerField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_salida = models.DateField(blank=True, null=True)
    peso_actual = models.FloatField(validators=[MinValueValidator(0)])
    altura_actual = models.FloatField(validators=[MinValueValidator(0)])
    sintomas_detectados = models.TextField(blank=True)  
    diagnostico = models.CharField(max_length=100)
    med_recetados = models.ForeignKey('Medicamentos_Recetados', on_delete=models.CASCADE, blank=True, null=True)
    estado = models.CharField(max_length=100) 

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        constraints = [
            models.UniqueConstraint(fields=['perro', 'num_consulta', 'sucursal'], name='unique_consulta')
        ]

    def __str__(self):
        return f"Consulta {self.num_consulta} - {self.perro}"

class Medicamentos_Recetados(models.Model):
    medicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE)
    consulta = models.ForeignKey(Consultas, on_delete=models.CASCADE)
    periodicidad = models.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Medicamento Recetado"
        verbose_name_plural = "Medicamentos Recetados"
        constraints = [
            models.UniqueConstraint(fields=['medicamento', 'consulta'], name='unique_medicamentos_recetados')
        ]

    def __str__(self):
        return f"{self.medicamento} - {self.consulta}"

class SintomasxConsulta(models.Model):
    consulta = models.ForeignKey(Consultas, on_delete=models.CASCADE)
    sintoma = models.ForeignKey(Sintomas, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Síntoma por Consulta"
        verbose_name_plural = "Síntomas por Consulta"
        constraints = [
            models.UniqueConstraint(fields=['consulta', 'sintoma'], name='unique_sintomasxconsulta')
        ]

    def __str__(self):
        return f"{self.sintoma} - {self.consulta}"

class DiagnosticoxConsulta(models.Model):
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)
    consulta = models.ForeignKey(Consultas, on_delete=models.CASCADE)  
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Diagnóstico por Consulta"
        verbose_name_plural = "Diagnósticos por Consulta"
        constraints = [
            models.UniqueConstraint(fields=['diagnostico', 'consulta'], name='unique_diagnosticoxconsulta')
        ]

    def __str__(self):
        return f"{self.diagnostico} - {self.consulta}"

class Estado_Duenio(models.Model):
    cod_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Estado de Dueño"
        verbose_name_plural = "Estados de Dueño"

    def __str__(self):
        return self.estado

class Estado_Consulta(models.Model):
    cod_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Estado de Consulta"
        verbose_name_plural = "Estados de Consulta"

    def __str__(self):
        return self.estado

class Historial_Consulta(models.Model):
    cod_hist_estado = models.AutoField(primary_key=True)
    historial = models.TextField()
    cod_estado = models.ForeignKey(Estado_Consulta, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Historial de Consulta"
        verbose_name_plural = "Historiales de Consulta"

    def __str__(self):
        return f"Historial {self.cod_hist_estado}"
