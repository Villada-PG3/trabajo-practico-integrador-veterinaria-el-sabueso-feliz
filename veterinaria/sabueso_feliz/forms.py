from django import forms
from .models import (
    Sucursal, Empleado, Raza, Duenio, Perro,
    Vacuna, Calendario_Vacunas, Consultas,
    Medicamentos, Stock
)

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = '__all__'

class DuenioForm(forms.ModelForm):
    class Meta:
        model = Duenio
        fields = '__all__'

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = '__all__'

class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = '__all__'

class CalendarioVacunasForm(forms.ModelForm):
    class Meta:
        model = Calendario_Vacunas
        fields = '__all__'

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = '__all__'

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamentos
        fields = '__all__'

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
