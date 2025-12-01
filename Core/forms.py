from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.utils import timezone

from .models import Farmaco, Paciente, Producto, Propietario


User = get_user_model()


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "activo" in self.fields:
            # When creating new staff through the Django admin we want them to
            # appear as disponibles by default so they show up in assignment
            # drop-downs without extra manual steps.
            if not self.instance.pk:
                self.fields["activo"].initial = True
            self.fields["activo"].help_text = (
                "Desmarca esta opción para ocultar al usuario de los listados "
                "operativos sin necesidad de desactivarlo por completo."
            )



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "nombre",
            "descripcion",
            "categoria",
            "precio",
            "imagen",
            "telefono_contacto",
            "disponible",
        ]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs.update({"class": "form-control"})
        self.fields["categoria"].widget.attrs.update({"class": "form-select"})
        self.fields["precio"].widget.attrs.update({"class": "form-control", "step": "0.01", "min": "0"})
        self.fields["imagen"].widget.attrs.update({"class": "form-control"})
        self.fields["telefono_contacto"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Ej: +56 9 1234 5678",
            }
        )
        self.fields["disponible"].widget.attrs.update({"class": "form-check-input"})


class FarmacoForm(forms.ModelForm):
    class Meta:
        model = Farmaco
        fields = ["sucursal", "nombre", "categoria", "descripcion", "stock"]
        widgets = {
            "descripcion": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-control",
                    "placeholder": "Detalles, indicaciones y condiciones de almacenamiento",
                }
            ),
        }

    def __init__(self, *args, sucursales=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Nombre comercial o genérico"}
        )
        self.fields["categoria"].widget.attrs.update({"class": "form-select"})
        self.fields["stock"].widget.attrs.update(
            {"class": "form-control", "min": "0", "step": "1"}
        )
        self.fields["sucursal"].widget.attrs.update({"class": "form-select"})

        if sucursales is not None:
            self.fields["sucursal"].queryset = sucursales
            if not self.instance.pk and not self.fields["sucursal"].initial:
                primera = None
                try:
                    primera = sucursales.first()
                except AttributeError:
                    primera = sucursales[0] if sucursales else None
                if primera:
                    self.fields["sucursal"].initial = primera

class VacunaRegistroForm(forms.Form):
    paciente_id = forms.IntegerField(widget=forms.HiddenInput)
    vacuna_id = forms.IntegerField(widget=forms.HiddenInput)
    fecha_aplicacion = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control", "max": "9999-12-31"}),
    )
    notas = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 2,
                "class": "form-control",
                "placeholder": "Observaciones opcionales",
            }
        ),
    )

    def clean_fecha_aplicacion(self):
        fecha = self.cleaned_data.get("fecha_aplicacion")
        if fecha and fecha > timezone.localdate():
            raise forms.ValidationError(
                "La fecha de aplicación no puede ser posterior a hoy."
            )
        return fecha


class PerfilPropietarioForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=150, required=True)
    last_name = forms.CharField(label="Apellido", max_length=150, required=True)
    email = forms.EmailField(label="Email", required=False)
    telefono = forms.CharField(label="Telefono", max_length=30, required=False)
    direccion = forms.CharField(label="Direccion", max_length=200, required=False)
    avatar = forms.ImageField(label="Avatar", required=False)
    current_password = forms.CharField(
        label="Contrasena actual", widget=forms.PasswordInput, required=True
    )
    new_password = forms.CharField(
        label="Nueva contrasena", widget=forms.PasswordInput, required=False
    )
    confirm_password = forms.CharField(
        label="Confirmar nueva contrasena", widget=forms.PasswordInput, required=False
    )

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        text_fields = [
            "first_name",
            "last_name",
            "email",
            "telefono",
            "direccion",
        ]
        password_fields = ["current_password", "new_password", "confirm_password"]
        for name in text_fields:
            self.fields[name].widget.attrs.update(
                {
                    "class": "form-control rounded-3",
                    "placeholder": self.fields[name].label,
                }
            )
        for name in password_fields:
            self.fields[name].widget.attrs.update(
                {
                    "class": "form-control rounded-3",
                    "placeholder": self.fields[name].label,
                }
            )
        self.fields["avatar"].widget.attrs.update(
            {
                "class": "form-control rounded-3",
                "accept": "image/*",
            }
        )

    def clean_current_password(self):
        password = self.cleaned_data.get("current_password")
        user = getattr(self, "user", None)
        if not user or not user.check_password(password):
            raise forms.ValidationError("La contrasena actual no es correcta.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password or confirm_password:
            if not new_password or not confirm_password:
                raise forms.ValidationError(
                    "Debes completar y confirmar la nueva contrasena."
                )
            if new_password != confirm_password:
                self.add_error(
                    "confirm_password", "Las contrasenas nuevas no coinciden."
                )
            else:
                user = getattr(self, "user", None)
                password_validation.validate_password(new_password, user=user)
        return cleaned_data


class TransferirMascotaForm(forms.Form):
    mascota = forms.ModelChoiceField(
        label="Mascota a transferir",
        queryset=Paciente.objects.none(),
        required=True,
    )
    nuevo_propietario = forms.ModelChoiceField(
        label="Transferir a",
        queryset=Propietario.objects.none(),
        required=True,
    )
    password1 = forms.CharField(
        label="Contrasena",
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        label="Confirmar contrasena",
        widget=forms.PasswordInput,
        required=True,
    )

    def __init__(
        self,
        *args,
        propietario=None,
        propietarios_destino=None,
        user=None,
        **kwargs,
    ):
        self.propietario = propietario
        self.user = user or getattr(propietario, "user", None)
        super().__init__(*args, **kwargs)

        mascotas_qs = Paciente.objects.none()
        if propietario is not None:
            mascotas_qs = Paciente.objects.filter(propietario=propietario).order_by(
                "nombre"
            )
        self.fields["mascota"].queryset = mascotas_qs
        self.fields["mascota"].widget.attrs.update(
            {"class": "form-select rounded-3"}
        )

        destino_qs = Propietario.objects.none()
        if propietarios_destino is not None:
            destino_qs = propietarios_destino
        self.fields["nuevo_propietario"].queryset = destino_qs
        self.fields["nuevo_propietario"].widget.attrs.update(
            {"class": "form-select rounded-3"}
        )

        for nombre in ["password1", "password2"]:
            self.fields[nombre].widget.attrs.update(
                {"class": "form-control rounded-3"}
            )

    def clean_nuevo_propietario(self):
        destino = self.cleaned_data["nuevo_propietario"]
        if self.propietario and destino.pk == self.propietario.pk:
            raise forms.ValidationError("Debes seleccionar un propietario distinto.")
        return destino

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("password1")
        pwd2 = cleaned_data.get("password2")
        if pwd1 or pwd2:
            if pwd1 != pwd2:
                self.add_error("password2", "Las contrasenas no coinciden.")
            else:
                user = self.user
                if not user or not user.check_password(pwd1):
                    self.add_error("password1", "La contrasena ingresada es invalida.")
        return cleaned_data
