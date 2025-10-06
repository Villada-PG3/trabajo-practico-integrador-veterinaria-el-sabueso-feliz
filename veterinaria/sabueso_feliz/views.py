import os
import csv
# render = mostrar template, redirect = redirigir a otra vista
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# sistema de mensajes de Django (para avisos en pantalla)
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# funciones de autenticación de Django
from django.contrib.auth import authenticate, login, logout
# formulario ya hecho para login
from django.contrib.auth.forms import AuthenticationForm
# tu formulario personalizado de registro
from .forms import RegistroUsuarioForm


from .models import (
    Sucursal, Empleado, Raza, Duenio, Perro,
    Vacuna, Calendario_Vacunas, Consultas,
    Medicamentos, Stock
)

from .forms import (
    SucursalForm, EmpleadoForm, RazaForm, DuenioForm, PerroForm,
    VacunaForm, CalendarioVacunasForm, ConsultaForm,
    MedicamentoForm, StockForm
)

# Clase base para todas las vistas genéricas


class BaseGenericView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        context['model_name_plural'] = self.model._meta.verbose_name_plural
        return context

# Clases específicas para cada tipo de vista


class BaseListView(BaseGenericView, ListView):
    pass


class BaseDetailView(BaseGenericView, DetailView):
    pass


class BaseCreateView(BaseGenericView, CreateView):
    pass


class BaseUpdateView(BaseGenericView, UpdateView):
    pass


class BaseDeleteView(BaseGenericView, DeleteView):
    pass

# ─────────────────────────────
# Sucursal
# ─────────────────────────────


class SucursalListView(BaseListView):
    model = Sucursal
    template_name = 'generic/list.html'


class SucursalDetailView(BaseDetailView):
    model = Sucursal
    template_name = 'generic/detail.html'


class SucursalCreateView(BaseCreateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('sucursales_list')


class SucursalUpdateView(BaseUpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('sucursales_list')


class SucursalDeleteView(BaseDeleteView):
    model = Sucursal
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('sucursales_list')

# ─────────────────────────────
# Empleado
# ─────────────────────────────


class EmpleadoListView(BaseListView):
    model = Empleado
    template_name = 'generic/list.html'


class EmpleadoDetailView(BaseDetailView):
    model = Empleado
    template_name = 'generic/detail.html'


class EmpleadoCreateView(BaseCreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('empleados_list')


class EmpleadoUpdateView(BaseUpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('empleados_list')


class EmpleadoDeleteView(BaseDeleteView):
    model = Empleado
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('empleados_list')

# ─────────────────────────────
# Raza
# ─────────────────────────────


class RazaListView(BaseListView):
    model = Raza
    template_name = 'generic/list.html'


class RazaDetailView(BaseDetailView):
    model = Raza
    template_name = 'generic/detail.html'


class RazaCreateView(BaseCreateView):
    model = Raza
    form_class = RazaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('razas_list')


class RazaUpdateView(BaseUpdateView):
    model = Raza
    form_class = RazaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('razas_list')


class RazaDeleteView(BaseDeleteView):
    model = Raza
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('razas_list')

# ─────────────────────────────
# Dueño
# ─────────────────────────────


class DuenioListView(BaseListView):
    model = Duenio
    template_name = 'generic/list.html'


class DuenioDetailView(BaseDetailView):
    model = Duenio
    template_name = 'generic/detail.html'


class DuenioCreateView(BaseCreateView):
    model = Duenio
    form_class = DuenioForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('duenios_list')


class DuenioUpdateView(BaseUpdateView):
    model = Duenio
    form_class = DuenioForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('duenios_list')


class DuenioDeleteView(BaseDeleteView):
    model = Duenio
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('duenios_list')

# ─────────────────────────────
# Perro
# ─────────────────────────────


class PerroListView(BaseListView):
    model = Perro
    template_name = 'generic/list.html'


class PerroDetailView(BaseDetailView):
    model = Perro
    template_name = 'generic/detail.html'


class PerroCreateView(BaseCreateView):
    model = Perro
    form_class = PerroForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('perros_list')


class PerroUpdateView(BaseUpdateView):
    model = Perro
    form_class = PerroForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('perros_list')


class PerroDeleteView(BaseDeleteView):
    model = Perro
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('perros_list')

# ─────────────────────────────
# Vacunas / Calendario de Vacunas
# ─────────────────────────────


class VacunaListView(BaseListView):
    model = Vacuna
    template_name = 'generic/list.html'


class VacunaCreateView(BaseCreateView):
    model = Vacuna
    form_class = VacunaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('vacunas_list')


class CalendarioVacunasListView(BaseListView):
    model = Calendario_Vacunas
    template_name = 'generic/list.html'


class CalendarioVacunasCreateView(BaseCreateView):
    model = Calendario_Vacunas
    form_class = CalendarioVacunasForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('calendario_list')

# ─────────────────────────────
# Consultas
# ─────────────────────────────


class ConsultaListView(BaseListView):
    model = Consultas
    template_name = 'generic/list.html'


class ConsultaDetailView(BaseDetailView):
    model = Consultas
    template_name = 'generic/detail.html'


class ConsultaCreateView(BaseCreateView):
    model = Consultas
    form_class = ConsultaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('consultas_list')


class ConsultaUpdateView(BaseUpdateView):
    model = Consultas
    form_class = ConsultaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('consultas_list')


class ConsultaDeleteView(BaseDeleteView):
    model = Consultas
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('consultas_list')

# ─────────────────────────────
# Medicamentos / Stock
# ─────────────────────────────


class MedicamentoListView(BaseListView):
    model = Medicamentos
    template_name = 'generic/list.html'


class MedicamentoCreateView(BaseCreateView):
    model = Medicamentos
    form_class = MedicamentoForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('medicamentos_list')


class StockListView(BaseListView):
    model = Stock
    template_name = 'generic/list.html'


class StockCreateView(BaseCreateView):
    model = Stock
    form_class = StockForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('stock_list')

# ─────────────────────────────
# Home
# ─────────────────────────────


class HomeView(TemplateView):
    template_name = 'home.html'

# ─────────────────────────────
# Login
# ─────────────────────────────


# 🏠 Vista de inicio de sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        # Si el usuario mandó un formulario (apretó "Iniciar sesión")
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Si los datos son correctos → el usuario existe
            user = form.get_user()     # obtenemos al usuario validado
            login(request, user)       # guardamos su sesión (queda "logueado")
            messages.success(request, f"Bienvenido {user.username}!")
            return redirect('home')    # lo mandamos a la página principal
    else:
        # Si entró por primera vez a la URL /login/
        form = AuthenticationForm()   # se crea un formulario vacío
    return render(request, 'login.html', {'form': form})
    # Mostramos la plantilla login.html, pasándole el formulario


# 📝 Vista de registro
def registro(request):
    if request.method == 'POST':
        # Si el usuario mandó datos (apretó "Registrarse")
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Si todo está bien (contraseñas coinciden, usuario no existe, etc.)
            form.save()   # creamos el nuevo usuario en la base de datos
            messages.success(
                request, "Cuenta creada con éxito. Ahora puedes iniciar sesión.")
            return redirect('login')  # lo mandamos a la página de login
    else:
        # Si entró por primera vez a la URL /register/
        form = RegistroUsuarioForm()  # creamos un formulario vacío
    return render(request, 'register.html', {'form': form})
    # ⚠️ antes apuntaba a login.html → ahora apunta a register.html ✅


# 🚪 Vista para cerrar sesión
def cerrar_sesion(request):
    logout(request)  # borramos la sesión del usuario
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect("login")
    # ⚠️ antes intentaba renderizar login.html con un form que no existía →
    # mejor redirigir directo a la vista de login ✅

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RegistroUsuarioForm, SucursalForm, EmpleadoForm, RazaForm, DuenioForm, PerroForm, VacunaForm, CalendarioVacunasForm, ConsultaForm, MedicamentoForm, StockForm
from .models import Sucursal, Empleado, Raza, Duenio, Perro, Vacuna, Calendario_Vacunas, Consultas, Medicamentos, Stock

# ─────────────────────────────
# BASE
# ─────────────────────────────
class BaseGenericView(LoginRequiredMixin):
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        context['model_name_plural'] = self.model._meta.verbose_name_plural
        return context


class BaseListView(BaseGenericView, ListView): pass
class BaseDetailView(BaseGenericView, DetailView): pass
class BaseCreateView(BaseGenericView, CreateView): pass
class BaseUpdateView(BaseGenericView, UpdateView): pass
class BaseDeleteView(BaseGenericView, DeleteView): pass

# ─────────────────────────────
# HOME
# ─────────────────────────────
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'

# ─────────────────────────────
# LOGIN / REGISTER / LOGOUT
# ─────────────────────────────
def iniciar_sesion(request):
    # Si ya está logueado → al home
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenido {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def registro(request):
    # Si ya está logueado → al home
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada con éxito. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'register.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect("login")
