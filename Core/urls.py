from django.urls import path

from . import views

urlpatterns = [
    # ----------------------------
    # LOGIN / LOGOUT / REGISTRO
    # ----------------------------
    path("", views.LandingView.as_view(), name="landing"),
    path("contacto/", views.ContactoView.as_view(), name="contacto"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("registro/", views.RegistroPropietarioView.as_view(), name="registro_propietario"),
    path(
        "perfil/configuracion/",
        views.ConfiguracionPerfilView.as_view(),
        name="configuracion_perfil",
    ),
    # ----------------------------
    # DASHBOARD
    # ----------------------------
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    # ----------------------------
    # USUARIOS Y PACIENTES (ADMIN / ADMIN_OP)
    # ----------------------------
    path("usuarios/", views.ListarUsuariosView.as_view(), name="listar_usuarios"),
    path("pacientes/", views.ListarPacientesView.as_view(), name="listar_pacientes"),
    # ----------------------------
    # MASCOTAS (Propietario)
    # ----------------------------
    path("mis-mascotas/", views.MisMascotasView.as_view(), name="mis_mascotas"),
    path(
        "mis-mascotas/<int:mascota_id>/foto/",
        views.ActualizarFotoMascotaView.as_view(),
        name="actualizar_foto_mascota",
    ),
    path(
        "mis-mascotas/transferir/",
        views.TransferirMascotaView.as_view(),
        name="transferir_mascota",
    ),
    path(
        "calendario-vacunas/",
        views.CalendarioVacunasView.as_view(),
        name="calendario_vacunas",
    ),
    path(
        "mis-mascotas/registrar/",
        views.RegistrarMascotaView.as_view(),
        name="registrar_mascota",
    ),
    path(
        "mascota/<int:paciente_id>/",
        views.DetalleMascotaView.as_view(),
        name="detalle_mascota",
    ),
    path(
        "mascota/<int:paciente_id>/informes/",
        views.CitasInformesMascotaView.as_view(),
        name="citas_informes_mascota",
    ),
    # ----------------------------
    # TIENDA
    # ----------------------------
    path("tienda/", views.TiendaView.as_view(), name="tienda"),
    path(
        "tienda/<int:producto_id>/",
        views.DetalleProductoView.as_view(),
        name="detalle_producto",
    ),
    path(
        "administrador/productos/",
        views.AdminProductosListView.as_view(),
        name="admin_productos_list",
    ),
    path(
        "administrador/productos/nuevo/",
        views.AdminProductoCrearView.as_view(),
        name="admin_producto_crear",
    ),
    path(
        "administrador/productos/<int:producto_id>/editar/",
        views.AdminProductoEditarView.as_view(),
        name="admin_producto_editar",
    ),
    path(
        "administrador/inventario/farmacos/",
        views.InventarioFarmacosAdminView.as_view(),
        name="inventario_farmacos_admin",
    ),
    path(
        "administrador/analisis/",
        views.DashboardAdminAnalisisView.as_view(),
        name="dashboard_admin_analisis",
    ),
    path(
        "administrador/analisis/inventario/exportar/",
        views.ExportarInventarioExcelView.as_view(),
        name="exportar_inventario_excel",
    ),
    path(
        "administrador/analisis/propietario/<int:propietario_id>/exportar/",
        views.ExportarPropietarioExcelView.as_view(),
        name="exportar_propietario_excel",
    ),
    # ----------------------------
    # CITAS
    # ----------------------------
    path("mis-citas/", views.MisCitasView.as_view(), name="mis_citas"),
    path("agendar-cita/", views.AgendarCitaView.as_view(), name="agendar_cita"),
    path(
        "agendar-cita/<int:paciente_id>/",
        views.AgendarCitaView.as_view(),
        name="agendar_cita_paciente",
    ),
    # ----------------------------
    # HISTORIAL MÉDICO (VET)
    # ----------------------------
    path(
        "registrar-historial/<int:paciente_id>/",
        views.RegistrarHistorialView.as_view(),
        name="registrar_historial",
    ),
    # ADMIN - citas
    path(
        "administrador/citas/",
        views.ListarCitasAdminView.as_view(),
        name="listar_citas_admin",
    ),
    path(
        "administrador/citas/pendientes/",
        views.AsignarVeterinarioCitasView.as_view(),
        name="asignar_veterinario_citas",
    ),
    path(
        "cita/<int:cita_id>/asignar-vet/",
        views.AsignarVeterinarioCitaView.as_view(),
        name="asignar_veterinario_cita",
    ),
    path("atender_cita/<int:cita_id>/", views.AtenderCitaView.as_view(), name="atender_cita"),
    path("mis_historiales/", views.MisHistorialesView.as_view(), name="mis_historiales"),
    path("cita/<int:cita_id>/", views.DetalleCitaView.as_view(), name="detalle_cita"),
    path("agendar_cita_admin/", views.AgendarCitaAdminView.as_view(), name="agendar_cita_admin"),
    path(
        "crear_propietario_admin/",
        views.CrearPropietarioAdminView.as_view(),
        name="crear_propietario_admin",
    ),
    path(
        "crear_mascota_admin/",
        views.CrearMascotaAdminView.as_view(),
        name="crear_mascota_admin",
    ),
    path("buscar_propietarios/", views.BuscarPropietariosView.as_view(), name="buscar_propietarios"),
    path(
        "propietario/<int:propietario_id>/",
        views.DetallePropietarioView.as_view(),
        name="detalle_propietario",
    ),
    path(
        "asignar_veterinario/",
        views.GestionarVeterinariosView.as_view(),
        name="gestionar_veterinarios",
    ),
    path(
        "dashboard/veterinarios/",
        views.DashboardVeterinariosView.as_view(),
        name="dashboard_veterinarios",
    ),
    path(
        "dashboard/veterinarios/farmacos/",
        views.InventarioFarmacosVeterinarioView.as_view(),
        name="inventario_farmacos_veterinario",
    ),
    path(
        "dashboard/veterinarios/indicadores/",
        views.DashboardVeterinariosIndicadoresView.as_view(),
        name="dashboard_veterinarios_indicadores",
    ),
    path("vet/historial-medico/", views.HistorialMedicoVetView.as_view(), name="historial_medico_vet"),
    path(
        "vet/historial-medico/<int:historial_id>/",
        views.DetalleHistorialView.as_view(),
        name="detalle_historial",
    ),
]
