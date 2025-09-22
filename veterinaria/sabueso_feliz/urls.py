from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # --- home ---
    path('', views.HomeView.as_view(), name='home'),

    # --- Sucursales ---
    path('sucursales/', views.SucursalListView.as_view(), name='sucursales_list'),
    path('sucursales/<int:pk>/', views.SucursalDetailView.as_view(),
         name='sucursales_detail'),
    path('sucursales/nuevo/', views.SucursalCreateView.as_view(),
         name='sucursales_create'),
    path('sucursales/<int:pk>/editar/',
         views.SucursalUpdateView.as_view(), name='sucursales_update'),
    path('sucursales/<int:pk>/eliminar/',
         views.SucursalDeleteView.as_view(), name='sucursales_delete'),

    # --- Empleados ---
    path('empleados/', views.EmpleadoListView.as_view(), name='empleados_list'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(),
         name='empleados_detail'),
    path('empleados/nuevo/', views.EmpleadoCreateView.as_view(),
         name='empleados_create'),
    path('empleados/<int:pk>/editar/',
         views.EmpleadoUpdateView.as_view(), name='empleados_update'),
    path('empleados/<int:pk>/eliminar/',
         views.EmpleadoDeleteView.as_view(), name='empleados_delete'),

    # --- Razas ---
    path('razas/', views.RazaListView.as_view(), name='razas_list'),
    path('razas/<str:pk>/', views.RazaDetailView.as_view(), name='razas_detail'),
    path('razas/nuevo/', views.RazaCreateView.as_view(), name='razas_create'),
    path('razas/<str:pk>/editar/',
         views.RazaUpdateView.as_view(), name='razas_update'),
    path('razas/<str:pk>/eliminar/',
         views.RazaDeleteView.as_view(), name='razas_delete'),

    # --- Dueños ---
    path('duenios/', views.DuenioListView.as_view(), name='duenios_list'),
    path('duenios/<int:pk>/', views.DuenioDetailView.as_view(),
         name='duenios_detail'),
    path('duenios/nuevo/', views.DuenioCreateView.as_view(), name='duenios_create'),
    path('duenios/<int:pk>/editar/',
         views.DuenioUpdateView.as_view(), name='duenios_update'),
    path('duenios/<int:pk>/eliminar/',
         views.DuenioDeleteView.as_view(), name='duenios_delete'),

    # --- Perros ---
    path('perros/', views.PerroListView.as_view(), name='perros_list'),
    path('perros/<int:pk>/', views.PerroDetailView.as_view(), name='perros_detail'),
    path('perros/nuevo/', views.PerroCreateView.as_view(), name='perros_create'),
    path('perros/<int:pk>/editar/',
         views.PerroUpdateView.as_view(), name='perros_update'),
    path('perros/<int:pk>/eliminar/',
         views.PerroDeleteView.as_view(), name='perros_delete'),

    # --- Vacunas ---
    path('vacunas/', views.VacunaListView.as_view(), name='vacunas_list'),
    path('vacunas/nuevo/', views.VacunaCreateView.as_view(), name='vacunas_create'),

    # --- Calendario Vacunas ---
    path('calendario/', views.CalendarioVacunasListView.as_view(),
         name='calendario_list'),
    path('calendario/nuevo/', views.CalendarioVacunasCreateView.as_view(),
         name='calendario_create'),

    # --- Consultas ---
    path('consultas/', views.ConsultaListView.as_view(), name='consultas_list'),
    path('consultas/<int:pk>/', views.ConsultaDetailView.as_view(),
         name='consultas_detail'),
    path('consultas/nuevo/', views.ConsultaCreateView.as_view(),
         name='consultas_create'),
    path('consultas/<int:pk>/editar/',
         views.ConsultaUpdateView.as_view(), name='consultas_update'),
    path('consultas/<int:pk>/eliminar/',
         views.ConsultaDeleteView.as_view(), name='consultas_delete'),

    # --- Medicamentos ---
    path('medicamentos/', views.MedicamentoListView.as_view(),
         name='medicamentos_list'),
    path('medicamentos/nuevo/', views.MedicamentoCreateView.as_view(),
         name='medicamentos_create'),

    # --- Stock ---
    path('stock/', views.StockListView.as_view(), name='stock_list'),
    path('stock/nuevo/', views.StockCreateView.as_view(), name='stock_create'),

    # --- Login ---
    path("register/", views.register, name="register"),
]
