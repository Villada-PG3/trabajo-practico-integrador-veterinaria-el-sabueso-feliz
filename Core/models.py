from django.db import models
from django.contrib.auth.models import AbstractUser

# ----------------------------
# Usuario con rol propio
# ----------------------------
class User(AbstractUser):
    ROLES = (
        ("ADMIN", "Administrador"),
        ("VET", "Veterinario"),
        ("ADMIN_OP", "Administrativo"),
        ("OWNER", "Propietario"),
    )
    rol = models.CharField(max_length=20, choices=ROLES)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    activo = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True)  # para veterinarios

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"

# ----------------------------
# Propietario
# ----------------------------
class Propietario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    notas = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

# ----------------------------
# Paciente / Mascota
# ----------------------------
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True)
    sexo = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    vacunas = models.TextField(blank=True)
    alergias = models.TextField(blank=True)
    foto = models.ImageField(upload_to="pacientes/", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

# ----------------------------
# Cita
# ----------------------------
class Cita(models.Model):
    ESTADOS = (
        ("programada", "Programada"),
        ("atendida", "Atendida"),
        ("cancelada", "Cancelada"),
    )
    TIPOS = (
        ("consulta", "Consulta"),
        ("vacunacion", "Vacunación"),
        ("cirugia", "Cirugía"),
    )
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(User, limit_choices_to={"rol": "VET"}, on_delete=models.SET_NULL, null=True)
    fecha_hora = models.DateTimeField()
    duracion = models.IntegerField(default=30)  # duración en minutos
    tipo = models.CharField(max_length=50, choices=TIPOS, default="consulta")
    estado = models.CharField(max_length=20, choices=ESTADOS, default="programada")
    notas = models.TextField(blank=True)

    def __str__(self):
        veterinario_nombre = self.veterinario.username if self.veterinario else "Sin asignar"
        return (
            f"Cita: {self.paciente.nombre} con {veterinario_nombre} - "
            f"{self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"
        )

# ----------------------------
# Historial Médico
# ----------------------------
class HistorialMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(User, limit_choices_to={"rol": "VET"}, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    notas = models.TextField(blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    examenes = models.TextField(blank=True)
    imagenes = models.ImageField(upload_to="historial_medico/", blank=True, null=True)
    proximo_control = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Historial de {self.paciente.nombre} - {self.fecha.strftime('%d/%m/%Y')}"
