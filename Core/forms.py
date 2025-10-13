from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "categoria", "precio", "imagen", "disponible"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs.update({"class": "form-control"})
        self.fields["categoria"].widget.attrs.update({"class": "form-select"})
        self.fields["precio"].widget.attrs.update({"class": "form-control", "step": "0.01", "min": "0"})
        self.fields["imagen"].widget.attrs.update({"class": "form-control"})
        self.fields["disponible"].widget.attrs.update({"class": "form-check-input"})
