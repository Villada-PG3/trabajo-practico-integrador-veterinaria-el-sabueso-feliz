from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0009_historialmedico_sin_proximo_control"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sucursal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=120, unique=True)),
                ("direccion", models.CharField(max_length=255)),
                ("telefono", models.CharField(blank=True, max_length=30)),
            ],
            options={
                "ordering": ["nombre"],
            },
        ),
        migrations.AddField(
            model_name="user",
            name="sucursal",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="usuarios",
                to="Core.sucursal",
            ),
        ),
        migrations.AddField(
            model_name="cita",
            name="sucursal",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="citas",
                to="Core.sucursal",
            ),
        ),
    ]
