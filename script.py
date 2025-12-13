"""
Script de carga de datos de ejemplo para Sabueso Feliz.

Uso:
    python script.py

Requiere que las migraciones ya estén aplicadas.
"""

import os
from decimal import Decimal
from datetime import date, datetime, timedelta

import django
from django.db import transaction
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from Core.models import (  # noqa: E402
    Cita,
    CitaFarmaco,
    Farmaco,
    HistorialMedico,
    Paciente,
    Producto,
    Propietario,
    Sucursal,
    User,
    VacunaRecomendada,
    VacunaRegistro,
)


def _reset_data():
    """Borra datos existentes para permitir una carga limpia."""
    CitaFarmaco.objects.all().delete()
    HistorialMedico.objects.all().delete()
    VacunaRegistro.objects.all().delete()
    Cita.objects.all().delete()
    Paciente.objects.all().delete()
    Propietario.objects.all().delete()
    Farmaco.objects.all().delete()
    Producto.objects.all().delete()
    VacunaRecomendada.objects.all().delete()
    Sucursal.objects.all().delete()
    User.objects.all().delete()


def run():
    with transaction.atomic():
        _reset_data()

        # Sucursales
        central = Sucursal.objects.create(
            nombre="Sabueso Central",
            direccion="Av. Principal 123",
            ciudad="Cordoba",
            telefono="+54 351 555-0000",
        )
        norte = Sucursal.objects.create(
            nombre="Sabueso Norte",
            direccion="Calle Secundaria 456",
            ciudad="Cordoba",
            telefono="+54 351 555-0001",
        )

        # Usuarios
        superadmin = User.objects.create_superuser(
            username="admin",
            email="admin@sabueso.test",
            password="admin123",
            rol="ADMIN",
            sucursal=central,
        )
        admin_op = User.objects.create_user(
            username="operaciones",
            email="operaciones@sabueso.test",
            password="oper123",
            rol="ADMIN_OP",
            sucursal=central,
        )
        vet = User.objects.create_user(
            username="drperro",
            email="vet@sabueso.test",
            password="vet123",
            first_name="Dra.",
            last_name="Canela",
            rol="VET",
            sucursal=central,
            especialidad="Clínica general",
        )
        owner = User.objects.create_user(
            username="propietario",
            email="owner@sabueso.test",
            password="owner123",
            first_name="Lola",
            last_name="Gomez",
            rol="OWNER",
            telefono="+54 351 555-1234",
            direccion="Bv. Perro Feliz 789",
        )
        owner2 = User.objects.create_user(
            username="propietario2",
            email="owner2@sabueso.test",
            password="owner123",
            first_name="Carlos",
            last_name="Lopez",
            rol="OWNER",
            telefono="+54 351 555-5678",
            direccion="Av. Mascotas 321",
        )

        propietario = Propietario.objects.create(
            user=owner, telefono=owner.telefono, direccion=owner.direccion, ciudad="Cordoba"
        )
        propietario2 = Propietario.objects.create(
            user=owner2, telefono=owner2.telefono, direccion=owner2.direccion, ciudad="Cordoba"
        )

        # Mascotas
        firulais = Paciente.objects.create(
            nombre="Firulais",
            especie="Perro",
            raza="Labrador",
            sexo="Macho",
            fecha_nacimiento=date(2021, 5, 20),
            propietario=propietario,
            vacunas="Antirrábica",
        )
        michi = Paciente.objects.create(
            nombre="Michi",
            especie="Gato",
            raza="Siames",
            sexo="Hembra",
            fecha_nacimiento=date(2020, 11, 2),
            propietario=propietario2,
            alergias="Penicilina",
        )

        # Farmacos
        antiparasitario = Farmaco.objects.create(
            nombre="Antiparasitario Plus",
            categoria=Farmaco.Categoria.ANTIPARASITARIOS_EXTERNOS,
            descripcion="Pipeta para pulgas y garrapatas",
            stock=30,
            sucursal=central,
        )
        analgesico = Farmaco.objects.create(
            nombre="Analgesico Vet",
            categoria=Farmaco.Categoria.ANALGESICOS_ANTIINFLAMATORIOS,
            descripcion="Alivio del dolor moderado",
            stock=20,
            sucursal=central,
        )

        # Productos tienda
        Producto.objects.create(
            nombre="Alimento Premium 10kg",
            descripcion="Alimento balanceado para perros adultos.",
            categoria="alimentos",
            precio=Decimal("25000"),
            disponible=True,
        )
        Producto.objects.create(
            nombre="Juguete Cuerda",
            descripcion="Cuerda resistente para juegos de tracción.",
            categoria="accesorios",
            precio=Decimal("3500"),
            disponible=True,
        )
        Producto.objects.create(
            nombre="Piedras sanitarias 5kg",
            descripcion="Arena sanitaria para gatos.",
            categoria="alimentos",
            precio=Decimal("4200"),
            disponible=True,
        )

        # Vacunas
        vacuna_perros = VacunaRecomendada.objects.create(
            nombre="Triple Canina",
            especie="canino",
            descripcion="Protección combinada para cachorros.",
            edad_recomendada=2,
            unidad_tiempo="meses",
            refuerzo="Refuerzo a los 12 meses",
            orden=1,
        )
        vacuna_gatos = VacunaRecomendada.objects.create(
            nombre="Triple Felina",
            especie="felino",
            descripcion="Protección contra rinotraqueitis, calicivirosis y panleucopenia.",
            edad_recomendada=2,
            unidad_tiempo="meses",
            refuerzo="Refuerzo anual",
            orden=1,
        )

        VacunaRegistro.objects.create(
            paciente=firulais,
            vacuna=vacuna_perros,
            fecha_aplicacion=timezone.localdate() - timedelta(days=20),
            notas="Aplicada sin reacciones adversas.",
        )

        # Citas y atenciones
        cita_future = Cita.objects.create(
            paciente=firulais,
            veterinario=vet,
            sucursal=central,
            fecha_solicitada=timezone.localdate() + timedelta(days=2),
            fecha_hora=timezone.now() + timedelta(days=2, hours=3),
            tipo="consulta",
            estado="programada",
            notas="Control de rutina y refuerzo de vacunas.",
        )
        cita_past = Cita.objects.create(
            paciente=michi,
            veterinario=vet,
            sucursal=central,
            fecha_solicitada=timezone.localdate() - timedelta(days=10),
            fecha_hora=timezone.now() - timedelta(days=9, hours=2),
            tipo="vacunacion",
            estado="atendida",
            notas="Consulta por alergia.",
        )

        HistorialMedico.objects.create(
            paciente=michi,
            veterinario=vet,
            cita=cita_past,
            diagnostico="Dermatitis leve",
            tratamiento="Antihistamínico tópico",
            notas="Control en 2 semanas",
            peso=4.2,
            temperatura=38.2,
        )

        CitaFarmaco.objects.create(cita=cita_past, farmaco=antiparasitario, cantidad=1)
        CitaFarmaco.objects.create(cita=cita_past, farmaco=analgesico, cantidad=1)

    print("Datos de ejemplo cargados.")
    print("Usuarios de prueba:")
    print("  superadmin -> user: admin / pass: admin123")
    print("  operador   -> user: operaciones / pass: oper123")
    print("  veterinario-> user: drperro / pass: vet123")
    print("  propietario-> user: propietario / pass: owner123")


if __name__ == "__main__":
    run()
