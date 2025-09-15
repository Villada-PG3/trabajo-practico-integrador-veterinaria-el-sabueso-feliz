from django.shortcuts import render
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

### Sucursal
class SucursalListView(ListView):
    model = Sucursal
class SucursalDetailView(DetailView):
    model = Sucursal
class SucursalCreateView(CreateView):
    model = Sucursal
    form_class = SucursalForm
    success_url = reverse_lazy('sucursales_list')
class SucursalUpdateView(UpdateView):
    model = Sucursal
    form_class = SucursalForm
    success_url = reverse_lazy('sucursales_list')
class SucursalDeleteView(DeleteView):
    model = Sucursal
    success_url = reverse_lazy('sucursales_list')

### Empleado
class EmpleadoListView(ListView):
    model = Empleado
class EmpleadoDetailView(DetailView):
    model = Empleado
class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_list')
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_list')
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados_list')

### Raza
class RazaListView(ListView):
    model = Raza
class RazaDetailView(DetailView):
    model = Raza
class RazaCreateView(CreateView):
    model = Raza
    form_class = RazaForm
    success_url = reverse_lazy('razas_list')
class RazaUpdateView(UpdateView):
    model = Raza
    form_class = RazaForm
    success_url = reverse_lazy('razas_list')
class RazaDeleteView(DeleteView):
    model = Raza
    success_url = reverse_lazy('razas_list')

### Dueño
class DuenioListView(ListView):
    model = Duenio
class DuenioDetailView(DetailView):
    model = Duenio
class DuenioCreateView(CreateView):
    model = Duenio
    form_class = DuenioForm
    success_url = reverse_lazy('duenios_list')
class DuenioUpdateView(UpdateView):
    model = Duenio
    form_class = DuenioForm
    success_url = reverse_lazy('duenios_list')
class DuenioDeleteView(DeleteView):
    model = Duenio
    success_url = reverse_lazy('duenios_list')

### Perro
class PerroListView(ListView):
    model = Perro
class PerroDetailView(DetailView):
    model = Perro
class PerroCreateView(CreateView):
    model = Perro
    form_class = PerroForm
    success_url = reverse_lazy('perros_list')
class PerroUpdateView(UpdateView):
    model = Perro
    form_class = PerroForm
    success_url = reverse_lazy('perros_list')
class PerroDeleteView(DeleteView):
    model = Perro
    success_url = reverse_lazy('perros_list')

### Vacuna / CalendarioVacunas
class VacunaListView(ListView):
    model = Vacuna
class VacunaCreateView(CreateView):
    model = Vacuna
    form_class = VacunaForm
    success_url = reverse_lazy('vacunas_list')

class CalendarioVacunasListView(ListView):
    model = Calendario_Vacunas
class CalendarioVacunasCreateView(CreateView):
    model = Calendario_Vacunas
    form_class = CalendarioVacunasForm
    success_url = reverse_lazy('calendario_list')

### Consultas
class ConsultaListView(ListView):
    model = Consultas
class ConsultaDetailView(DetailView):
    model = Consultas
class ConsultaCreateView(CreateView):
    model = Consultas
    form_class = ConsultaForm
    success_url = reverse_lazy('consultas_list')
class ConsultaUpdateView(UpdateView):
    model = Consultas
    form_class = ConsultaForm
    success_url = reverse_lazy('consultas_list')
class ConsultaDeleteView(DeleteView):
    model = Consultas
    success_url = reverse_lazy('consultas_list')

### Medicamentos / Stock
class MedicamentoListView(ListView):
    model = Medicamentos
class MedicamentoCreateView(CreateView):
    model = Medicamentos
    form_class = MedicamentoForm
    success_url = reverse_lazy('medicamentos_list')

class StockListView(ListView):
    model = Stock
class StockCreateView(CreateView):
    model = Stock
    form_class = StockForm
    success_url = reverse_lazy('stock_list')
