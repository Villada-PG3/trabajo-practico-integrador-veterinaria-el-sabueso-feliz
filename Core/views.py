from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Cita, HistorialMedico, Paciente, Propietario, User
# ----------------------------
# DASHBOARD
# ----------------------------
@login_required
def dashboard(request):
    user = request.user
    context = {}
    
    if user.rol == "ADMIN":
        context['total_usuarios'] = User.objects.count()
        context['total_pacientes'] = Paciente.objects.count()
        context['total_citas'] = Cita.objects.count()
        context['total_historiales'] = HistorialMedico.objects.count()
        resumen = {estado: 0 for estado, _ in Cita.ESTADOS}
        for item in Cita.objects.values('estado').annotate(total=Count('id')):
            resumen[item['estado']] = item['total']
        context['resumen_citas'] = resumen
        context['todas_citas'] = (
            Cita.objects.select_related('paciente', 'paciente__propietario__user', 'veterinario')
            .order_by('-fecha_hora')[:20]
        )
        context['todos_pacientes'] = (
            Paciente.objects.select_related('propietario__user')
            .order_by('nombre')[:20]
        )
    elif user.rol == "VET":
        context['mis_citas'] = Cita.objects.filter(veterinario=user).order_by('-fecha_hora')
        context['mis_historiales'] = HistorialMedico.objects.filter(veterinario=user).order_by('-fecha')
    elif user.rol == "OWNER":
        propietario = get_object_or_404(Propietario, user=user)
        context['mis_mascotas'] = Paciente.objects.filter(propietario=propietario)
        context['mis_citas'] = Cita.objects.filter(paciente__propietario=propietario).order_by('-fecha_hora')
        context['mis_historiales'] = HistorialMedico.objects.filter(paciente__propietario=propietario).order_by('-fecha')
    elif user.rol == "ADMIN_OP":
        context['todas_citas'] = Cita.objects.all().order_by('-fecha_hora')
        context['todos_pacientes'] = Paciente.objects.all()

    return render(request, "core/dashboard.html", context)


# ----------------------------
# LISTADO DE MASCOTAS (Propietario)
# ----------------------------
@login_required
def mis_mascotas(request):
    propietario = get_object_or_404(Propietario, user=request.user)
    mascotas = Paciente.objects.filter(propietario=propietario)
    return render(request, "core/mis_mascotas.html", {'mascotas': mascotas})


# ----------------------------
# DETALLE MASCOTA + HISTORIAL
# ----------------------------
@login_required
def detalle_mascota(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    # Verificación de rol y propiedad
    if request.user.rol == "OWNER" and paciente.propietario.user != request.user:
        messages.error(request, "No tienes permiso para ver esta mascota.")
        return redirect('dashboard')

    historiales = HistorialMedico.objects.filter(paciente=paciente).order_by('-fecha')
    citas = Cita.objects.filter(paciente=paciente).order_by('-fecha_hora')

    return render(request, "core/detalle_mascota.html", {
        'paciente': paciente,
        'historiales': historiales,
        'citas': citas
    })


# ----------------------------
# REGISTRAR HISTORIAL MÉDICO (VET)
# ----------------------------
@login_required
def registrar_historial(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    if request.user.rol != "VET":
        messages.error(request, "No tienes permiso para registrar historial médico.")
        return redirect('dashboard')

    if request.method == "POST":
        diagnostico = request.POST.get("diagnostico")
        tratamiento = request.POST.get("tratamiento")
        notas = request.POST.get("notas")
        peso = request.POST.get("peso")
        temperatura = request.POST.get("temperatura")
        examenes = request.POST.get("examenes")
        proximo_control = request.POST.get("proximo_control") or None

        HistorialMedico.objects.create(
            paciente=paciente,
            veterinario=request.user,
            diagnostico=diagnostico,
            tratamiento=tratamiento,
            notas=notas,
            peso=peso or None,
            temperatura=temperatura or None,
            examenes=examenes,
            proximo_control=proximo_control
        )
        messages.success(request, "Historial médico registrado correctamente ✅")
        return redirect('detalle_mascota', paciente_id=paciente.id)

    return render(request, "core/registrar_historial.html", {'paciente': paciente})


# ----------------------------
# LISTADO DE CITAS
# ----------------------------
@login_required
def mis_citas(request):
    user = request.user
    if user.rol == "VET":
        citas = Cita.objects.filter(veterinario=user).order_by('-fecha_hora')
    elif user.rol == "OWNER":
        propietario = get_object_or_404(Propietario, user=user)
        citas = Cita.objects.filter(paciente__propietario=propietario).order_by('-fecha_hora')
    elif user.rol == "ADMIN_OP" or user.rol == "ADMIN":
        citas = Cita.objects.all().order_by('-fecha_hora')
    else:
        citas = []

    return render(request, "core/mis_citas.html", {'citas': citas})


# ----------------------------
# LOGIN
# ----------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)  # <-- aquí falla si password no está hasheado
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "core/login.html")

# ----------------------------
# LOGOUT
# ----------------------------
def logout_view(request):
    logout(request)
    return redirect('login')

# ----------------------------
# REGISTRO PROPIETARIO
# ----------------------------
def registro_propietario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        telefono = request.POST.get("telefono")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
        else:
            # Crear usuario con contraseña hasheada
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password1,   # create_user se encarga de hashear
                rol="OWNER"
            )
            Propietario.objects.create(user=user, telefono=telefono)
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('login')

    return render(request, "core/registro_propietario.html")

from django.contrib.auth.decorators import login_required
from django.contrib import messages

# ----------------------------
# LISTAR USUARIOS (ADMIN)
# ----------------------------
@login_required
def listar_usuarios(request):
    if request.user.rol != "ADMIN":
        messages.error(request, "No tienes permiso para ver esta página.")
        return redirect('dashboard')

    usuarios = User.objects.all().order_by('username')
    return render(request, "core/usuarios.html", {'usuarios': usuarios})


# ----------------------------
# LISTAR PACIENTES (ADMIN)
# ----------------------------
@login_required
def listar_pacientes(request):
    if request.user.rol not in ["ADMIN", "ADMIN_OP"]:
        messages.error(request, "No tienes permiso para ver esta página.")
        return redirect('dashboard')

    pacientes = Paciente.objects.all().order_by('nombre')
    return render(request, "core/pacientes.html", {'pacientes': pacientes})



# ----------------------------
# REGISTRAR NUEVA MASCOTA (Propietario)
# ----------------------------
@login_required
def registrar_mascota(request):
    if request.user.rol != "OWNER":
        messages.error(request, "No tienes permiso para registrar mascotas.")
        return redirect('dashboard')

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        especie = request.POST.get("especie")
        raza = request.POST.get("raza")
        sexo = request.POST.get("sexo")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")

        propietario = get_object_or_404(Propietario, user=request.user)

        Paciente.objects.create(
            nombre=nombre,
            especie=especie,
            raza=raza,
            sexo=sexo,
            fecha_nacimiento=fecha_nacimiento,
            propietario=propietario
        )
        messages.success(request, f"Mascota {nombre} registrada correctamente ✅")
        return redirect('mis_mascotas')

    return render(request, "core/registrar_mascota.html")


# ----------------------------
# AGENDAR CITA (Propietario)
# ----------------------------
@login_required
def agendar_cita(request, paciente_id=None):
    if request.user.rol != "OWNER":
        messages.error(request, "No tienes permiso para agendar citas.")
        return redirect('dashboard')

    propietario = get_object_or_404(Propietario, user=request.user)
    mascotas = Paciente.objects.filter(propietario=propietario)
    paciente_seleccionado = None

    if request.method == "POST":
        paciente_id_form = request.POST.get("paciente")
        fecha_hora_raw = request.POST.get("fecha_hora")
        notas = request.POST.get("notas", "").strip()

        paciente = get_object_or_404(Paciente, id=paciente_id_form, propietario=propietario)
        paciente_seleccionado = paciente

        if not fecha_hora_raw:
            messages.error(request, "Debes seleccionar una fecha y hora válidas para la cita.")
        else:
            try:
                fecha_hora_dt = datetime.fromisoformat(fecha_hora_raw)
            except ValueError:
                messages.error(request, "El formato de la fecha y hora no es válido.")
            else:
                if timezone.is_naive(fecha_hora_dt):
                    fecha_hora_dt = timezone.make_aware(
                        fecha_hora_dt, timezone.get_current_timezone()
                    )

                if fecha_hora_dt < timezone.now():
                    messages.error(
                        request,
                        "La fecha y hora seleccionadas ya pasaron. Elige un horario futuro.",
                    )
                else:
                    Cita.objects.create(
                        paciente=paciente,
                        fecha_hora=fecha_hora_dt,
                        notas=notas,
                        estado="pendiente",
                    )
                    messages.success(
                        request,
                        f"Solicitud registrada para {paciente.nombre}. Un administrador asignará un veterinario pronto.",
                    )
                    return redirect('mis_citas')

    if paciente_id and paciente_seleccionado is None:
        paciente_seleccionado = get_object_or_404(
            Paciente, id=paciente_id, propietario=propietario
        )

    return render(request, "core/agendar_cita.html", {
        'mascotas': mascotas,
        'paciente_seleccionado': paciente_seleccionado
    })

@login_required
def asignar_veterinario_cita(request, cita_id):
    if request.user.rol not in ("ADMIN", "ADMIN_OP"):
        messages.error(request, "No tienes permiso para asignar veterinarios a las citas.")
        return redirect('dashboard')

    cita = get_object_or_404(Cita, id=cita_id)
    veterinarios = User.objects.filter(rol="VET", activo=True).order_by('first_name', 'last_name')

    if request.method == "POST":
        vet_id = request.POST.get("veterinario")
        if not vet_id:
            messages.error(request, "Debes seleccionar un veterinario para asignar la cita.")
        else:
            veterinario = get_object_or_404(User, id=vet_id, rol="VET")
            cita.veterinario = veterinario
            cita.estado = "programada"
            cita.save(update_fields=["veterinario", "estado"])
            nombre_vet = veterinario.get_full_name() or veterinario.username
            messages.success(request, f"Veterinario {nombre_vet} asignado correctamente a la cita ✅")
            return redirect('listar_citas_admin')

    return render(request, "core/asignar_veterinario.html", {
        'cita': cita,
        'veterinarios': veterinarios
    })


@login_required
def listar_citas_admin(request):
    if request.user.rol not in ("ADMIN", "ADMIN_OP"):
        messages.error(request, "No tienes permiso para ver esta página.")
        return redirect('dashboard')

    citas_pendientes = (
        Cita.objects.select_related('paciente', 'paciente__propietario__user')
        .filter(estado="pendiente")
        .order_by("fecha_hora")
    )
    citas_programadas = (
        Cita.objects.select_related('paciente', 'paciente__propietario__user', 'veterinario')
        .filter(estado="programada")
        .order_by("fecha_hora")
    )
    citas_atendidas = (
        Cita.objects.select_related('paciente', 'paciente__propietario__user', 'veterinario')
        .filter(estado="atendida")
        .order_by("-fecha_hora")
    )

    conteo_pendientes = citas_pendientes.count()
    conteo_programadas = citas_programadas.count()
    conteo_atendidas = citas_atendidas.count()
    conteo_canceladas = Cita.objects.filter(estado="cancelada").count()

    contexto = {
        "citas_pendientes": citas_pendientes,
        "citas_programadas": citas_programadas,
        "citas_atendidas": citas_atendidas,
        "conteo_estados": {
            "pendiente": conteo_pendientes,
            "programada": conteo_programadas,
            "atendida": conteo_atendidas,
            "cancelada": conteo_canceladas,
        },
    }

    return render(request, "core/citas_admin.html", contexto)


@login_required
def asignar_veterinario_citas(request):
    if request.user.rol not in ("ADMIN", "ADMIN_OP"):
        messages.error(request, "No tienes permiso para gestionar estas citas.")
        return redirect('dashboard')

    veterinarios = User.objects.filter(rol="VET", activo=True).order_by('first_name', 'last_name')
    citas_pendientes = (
        Cita.objects.select_related('paciente', 'paciente__propietario__user')
        .filter(estado="pendiente")
        .order_by('fecha_hora')
    )

    if request.method == "POST":
        cita_id = request.POST.get("cita")
        vet_id = request.POST.get("veterinario")

        if not cita_id or not vet_id:
            messages.error(request, "Selecciona una cita y un veterinario válidos.")
        else:
            cita = get_object_or_404(Cita, id=cita_id, estado__in=["pendiente", "programada"])
            veterinario = get_object_or_404(User, id=vet_id, rol="VET")
            cita.veterinario = veterinario
            cita.estado = "programada"
            cita.save(update_fields=["veterinario", "estado"])
            nombre_vet = veterinario.get_full_name() or veterinario.username
            messages.success(request, f"Veterinario {nombre_vet} asignado correctamente a la cita de {cita.paciente.nombre} ✅")
            return redirect('asignar_veterinario_citas')

    return render(request, "core/asignar_veterinario_citas.html", {
        'citas_pendientes': citas_pendientes,
        'veterinarios': veterinarios
    })

# Atender Cita (VET)
@login_required
def atender_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)

    if request.user.rol != "VET":
        messages.error(request, "No tienes permiso para atender esta cita.")
        return redirect('dashboard')

    if request.method == "POST":
        diagnostico = request.POST.get("diagnostico")
        tratamiento = request.POST.get("tratamiento")
        notas = request.POST.get("notas")
        peso = request.POST.get("peso") or None
        temperatura = request.POST.get("temperatura") or None
        examenes = request.POST.get("examenes")
        proximo_control = request.POST.get("proximo_control") or None

        # Crear historial médico asociado al paciente
        historial = HistorialMedico.objects.create(
            paciente=cita.paciente,
            veterinario=request.user,
            diagnostico=diagnostico,
            tratamiento=tratamiento,
            notas=notas,
            peso=peso,
            temperatura=temperatura,
            examenes=examenes,
            proximo_control=proximo_control
        )

        # Actualizar estado de la cita
        cita.estado = "atendida"
        cita.save()

        messages.success(request, "Cita de {} atendida correctamente ✅".format(cita.paciente.nombre))
        return redirect('detalle_cita', cita_id=cita.id)

    return render(request, "core/atender_cita.html", {'cita': cita})


@login_required
def mis_historiales(request):
    if request.user.rol != "VET":
        messages.error(request, "No tienes permiso para ver esta página.")
        return redirect('dashboard')

    historiales = HistorialMedico.objects.filter(veterinario=request.user).order_by('-fecha')
    return render(request, "core/mis_historiales.html", {'historiales': historiales})



@login_required
def detalle_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)

    # Permisos
    if request.user.rol == "OWNER" and cita.paciente.propietario.user != request.user:
        messages.error(request, "No tienes permiso para ver esta cita.")
        return redirect('dashboard')

    # Obtener el último historial del paciente
    historial = HistorialMedico.objects.filter(paciente=cita.paciente).order_by('-fecha').first()

    return render(request, "core/detalle_cita.html", {
        'cita': cita,
        'historial': historial
    })


@login_required
def agendar_cita_admin(request):
    if request.user.rol != "ADMIN":
        messages.error(request, "No tienes permiso para agendar citas.")
        return redirect('dashboard')

    mascotas = Paciente.objects.all().order_by('nombre')
    veterinarios = User.objects.filter(rol="VET").order_by('first_name', 'last_name')
    paciente_seleccionado = None

    if request.method == "POST":
        paciente_id = request.POST.get("paciente")
        veterinario_id = request.POST.get("veterinario")
        fecha_hora_raw = request.POST.get("fecha_hora")
        notas = request.POST.get("notas", "").strip()

        paciente = get_object_or_404(Paciente, id=paciente_id)
        veterinario = get_object_or_404(User, id=veterinario_id, rol="VET")

        try:
            fecha_hora_dt = datetime.fromisoformat(fecha_hora_raw)
        except (TypeError, ValueError):
            messages.error(request, "Selecciona una fecha y hora válidas.")
        else:
            if timezone.is_naive(fecha_hora_dt):
                fecha_hora_dt = timezone.make_aware(
                    fecha_hora_dt, timezone.get_current_timezone()
                )

            if fecha_hora_dt < timezone.now():
                messages.error(request, "No puedes programar una cita en el pasado.")
            else:
                Cita.objects.create(
                    paciente=paciente,
                    veterinario=veterinario,
                    fecha_hora=fecha_hora_dt,
                    notas=notas,
                    estado="programada"
                )
                nombre_vet = veterinario.get_full_name() or veterinario.username
                messages.success(
                    request,
                    f"Cita para {paciente.nombre} asignada a {nombre_vet} ✅",
                )
                return redirect('dashboard')

    return render(request, "core/agendar_cita_admin.html", {
        'mascotas': mascotas,
        'veterinarios': veterinarios,
        'paciente_seleccionado': paciente_seleccionado
    })


@login_required
def crear_propietario_admin(request):
    if request.user.rol != "ADMIN":
        messages.error(request, "No tienes permiso para esta acción.")
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        telefono = request.POST.get("telefono")
        direccion = request.POST.get("direccion")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                rol="OWNER"
            )
            Propietario.objects.create(user=user, telefono=telefono, direccion=direccion)
            messages.success(request, "Propietario creado correctamente ✅")
            return redirect('dashboard')

    return render(request, "core/crear_propietario_admin.html")


# ----------------------------
# CREAR MASCOTA (ADMIN)
# ----------------------------
@login_required
def crear_mascota_admin(request):
    if request.user.rol != "ADMIN":
        messages.error(request, "No tienes permiso para esta acción.")
        return redirect('dashboard')

    propietarios = Propietario.objects.all()
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        especie = request.POST.get("especie")
        raza = request.POST.get("raza")
        sexo = request.POST.get("sexo")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        propietario_id = request.POST.get("propietario")  # puede estar vacío

        propietario = Propietario.objects.filter(id=propietario_id).first() if propietario_id else None

        Paciente.objects.create(
            nombre=nombre,
            especie=especie,
            raza=raza,
            sexo=sexo,
            fecha_nacimiento=fecha_nacimiento or None,
            propietario=propietario
        )
        messages.success(request, "Mascota creada correctamente ✅")
        return redirect('dashboard')

    return render(request, "core/crear_mascota_admin.html", {'propietarios': propietarios})

from django.shortcuts import render, get_object_or_404
from Core.models import Propietario, Paciente, Cita, HistorialMedico
from django.db.models import Q

def buscar_propietarios(request):
    q = request.GET.get('q', '')
    resultados = []

    if q:
        resultados = Propietario.objects.filter(
            Q(user__first_name__icontains=q) |
            Q(user__last_name__icontains=q) |
            Q(user__username__icontains=q) |
            Q(telefono__icontains=q) |
            Q(direccion__icontains=q)
        )

    return render(request, 'core/buscar_propietarios.html', {
        'resultados': resultados,
        'query': q
    })

def detalle_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    mascotas = Paciente.objects.filter(propietario=propietario)
    citas = Cita.objects.filter(paciente__in=mascotas)
    citas_pendientes = citas.filter(estado='programada')
    informes = HistorialMedico.objects.filter(paciente__in=mascotas)

    return render(request, 'core/detalle_propietario.html', {
        'propietario': propietario,
        'mascotas': mascotas,
        'citas': citas,
        'citas_pendientes': citas_pendientes,
        'informes': informes
    })

from django.shortcuts import render, get_object_or_404
from Core.models import Paciente, Cita, HistorialMedico

def detalle_mascota(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    # Traemos todas las citas de esa mascota
    citas = Cita.objects.filter(paciente=paciente).order_by('-fecha_hora')
    
    # Historial médico de la mascota
    historiales = HistorialMedico.objects.filter(paciente=paciente).order_by('-fecha')
    
    context = {
        'paciente': paciente,
        'citas': citas,
        'historiales': historiales,
    }
    return render(request, 'core/detalle_mascota_admin.html', context)



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()


@login_required
def gestionar_veterinarios(request):
    if request.user.rol != "ADMIN":
        messages.error(request, "No tienes permiso para gestionar veterinarios.")
        return redirect('dashboard')

    # Traer usuarios que NO son veterinarios
    usuarios_no_vet = User.objects.exclude(rol="VET")

    if request.method == "POST":
        user_id = request.POST.get("usuario")
        usuario = get_object_or_404(User, id=user_id)
        usuario.rol = "VET"
        usuario.save()
        messages.success(request, f"{usuario.get_full_name()} ahora es Veterinario ✅")
        return redirect("gestionar_veterinarios")

    return render(request, "core/asignar_veterinario_admin.html", {
        "usuarios": usuarios_no_vet
    })


from django.shortcuts import render
from django.contrib.auth import get_user_model
from Core.models import Cita

User = get_user_model()

def dashboard_veterinarios(request):
    if request.user.rol != "ADMIN":
        return redirect("dashboard")  # redirigir si no es admin

    # Todos los veterinarios
    veterinarios = User.objects.filter(rol="VET")

    vet_stats = []
    for vet in veterinarios:
        citas_totales = Cita.objects.filter(veterinario=vet).count()
        citas_pendientes = Cita.objects.filter(veterinario=vet, estado="programada").count()
        citas_atendidas = Cita.objects.filter(veterinario=vet, estado="atendida").count()
        proximas_citas = Cita.objects.filter(veterinario=vet, estado="programada").order_by("fecha_hora")[:5]

        vet_stats.append({
            "veterinario": vet,
            "citas_totales": citas_totales,
            "citas_pendientes": citas_pendientes,
            "citas_atendidas": citas_atendidas,
            "proximas_citas": proximas_citas,
        })

    return render(request, "core/dashboard_veterinarios.html", {
        "vet_stats": vet_stats
    })


from django.shortcuts import render
from Core.models import HistorialMedico
from django.db.models import Q

def historial_medico_vet(request):
    query = request.GET.get("q", "")
    fecha_desde = request.GET.get("desde", "")
    fecha_hasta = request.GET.get("hasta", "")

    historiales = HistorialMedico.objects.all()

    if query:
        historiales = historiales.filter(
            Q(paciente__nombre__icontains=query) |
            Q(paciente__propietario__first_name__icontains=query) |
            Q(paciente__propietario__last_name__icontains=query) |
            Q(diagnostico__icontains=query)
        )

    if fecha_desde:
        historiales = historiales.filter(fecha__gte=fecha_desde)
    if fecha_hasta:
        historiales = historiales.filter(fecha__lte=fecha_hasta)

    return render(request, "core/historial_medico_vet.html", {
        "historiales": historiales,
        "query": query,
        "fecha_desde": fecha_desde,
        "fecha_hasta": fecha_hasta
    })




from django.shortcuts import render, get_object_or_404
from Core.models import HistorialMedico

def detalle_historial(request, historial_id):
    historial = get_object_or_404(HistorialMedico, id=historial_id)
    return render(request, "core/detalle_historial.html", {
        "historial": historial
    })

