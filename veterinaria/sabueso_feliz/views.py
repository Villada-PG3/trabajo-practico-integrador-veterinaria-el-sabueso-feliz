import os
import csv
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.hashers import make_password

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


def register(request):
    if request.method == "GET":
        # Mostramos el formulario
        return render(request, "register.html")

    # Si es POST, procesamos el formulario
    usuario = request.POST.get("usuario")
    email = request.POST.get("email")
    password = request.POST.get("password")

    if not usuario or not email or not password:
        return JsonResponse({"status": "error", "message": "Faltan datos en el formulario"})

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({"status": "error", "message": "Formato de email inválido"})

    file_path = os.path.join(os.path.dirname(__file__), "usuarios.csv")
    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["usuario", "email", "password"])
        writer.writerow([usuario, email, password])

    return JsonResponse({
        "status": "success",
        "message": "Usuario registrado correctamente",
        "usuario": usuario,
        "email": email
    })
