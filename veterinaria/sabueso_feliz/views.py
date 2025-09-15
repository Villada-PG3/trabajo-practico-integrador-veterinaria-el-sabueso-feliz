from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

# Clase base para vistas de lista
class BaseListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name_plural'] = self.model._meta.verbose_name_plural
        return context

# ─────────────────────────────
# Sucursal
# ─────────────────────────────
class SucursalListView(BaseListView):
    model = Sucursal
    template_name = 'generic/list.html'

class SucursalDetailView(DetailView):
    model = Sucursal
    template_name = 'generic/detail.html'

class SucursalCreateView(CreateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('sucursales_list')

class SucursalUpdateView(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('sucursales_list')

class SucursalDeleteView(DeleteView):
    model = Sucursal
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('sucursales_list')

# ─────────────────────────────
# Empleado
# ─────────────────────────────
class EmpleadoListView(BaseListView):
    model = Empleado
    template_name = 'generic/list.html'

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'generic/detail.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('empleados_list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('empleados_list')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('empleados_list')

# ─────────────────────────────
# Raza
# ─────────────────────────────
class RazaListView(BaseListView):
    model = Raza
    template_name = 'generic/list.html'

class RazaDetailView(DetailView):
    model = Raza
    template_name = 'generic/detail.html'

class RazaCreateView(CreateView):
    model = Raza
    form_class = RazaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('razas_list')

class RazaUpdateView(UpdateView):
    model = Raza
    form_class = RazaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('razas_list')

class RazaDeleteView(DeleteView):
    model = Raza
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('razas_list')

# ─────────────────────────────
# Dueño
# ─────────────────────────────
class DuenioListView(BaseListView):
    model = Duenio
    template_name = 'generic/list.html'

class DuenioDetailView(DetailView):
    model = Duenio
    template_name = 'generic/detail.html'

class DuenioCreateView(CreateView):
    model = Duenio
    form_class = DuenioForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('duenios_list')

class DuenioUpdateView(UpdateView):
    model = Duenio
    form_class = DuenioForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('duenios_list')

class DuenioDeleteView(DeleteView):
    model = Duenio
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('duenios_list')

# ─────────────────────────────
# Perro
# ─────────────────────────────
class PerroListView(BaseListView):
    model = Perro
    template_name = 'generic/list.html'

class PerroDetailView(DetailView):
    model = Perro
    template_name = 'generic/detail.html'

class PerroCreateView(CreateView):
    model = Perro
    form_class = PerroForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('perros_list')

class PerroUpdateView(UpdateView):
    model = Perro
    form_class = PerroForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('perros_list')

class PerroDeleteView(DeleteView):
    model = Perro
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('perros_list')

# ─────────────────────────────
# Vacunas / Calendario de Vacunas
# ─────────────────────────────
class VacunaListView(BaseListView):
    model = Vacuna
    template_name = 'generic/list.html'

class VacunaCreateView(CreateView):
    model = Vacuna
    form_class = VacunaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('vacunas_list')

class CalendarioVacunasListView(BaseListView):
    model = Calendario_Vacunas
    template_name = 'generic/list.html'

class CalendarioVacunasCreateView(CreateView):
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

class ConsultaDetailView(DetailView):
    model = Consultas
    template_name = 'generic/detail.html'

class ConsultaCreateView(CreateView):
    model = Consultas
    form_class = ConsultaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('consultas_list')

class ConsultaUpdateView(UpdateView):
    model = Consultas
    form_class = ConsultaForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('consultas_list')

class ConsultaDeleteView(DeleteView):
    model = Consultas
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('consultas_list')

# ─────────────────────────────
# Medicamentos / Stock
# ─────────────────────────────
class MedicamentoListView(BaseListView):
    model = Medicamentos
    template_name = 'generic/list.html'

class MedicamentoCreateView(CreateView):
    model = Medicamentos
    form_class = MedicamentoForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('medicamentos_list')

class StockListView(BaseListView):
    model = Stock
    template_name = 'generic/list.html'

class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'generic/form.html'
    success_url = reverse_lazy('stock_list')