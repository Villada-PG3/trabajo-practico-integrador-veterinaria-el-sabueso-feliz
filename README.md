<p align="center">
  <img src="https://i.imgur.com/uYeDNLF.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>





<p align="center">
  <img src="https://i.imgur.com/RVGaecC.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>


<p align="center">
  <img src="https://i.imgur.com/cap2sCd.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>






![Python](https://custom-icon-badges.demolab.com/badge/Python-3.11-3776AB.svg?logo=python&logoColor=white)
![Django](https://custom-icon-badges.demolab.com/badge/Django-5.2-092E20.svg?logo=django&logoColor=white)
![SQLite](https://custom-icon-badges.demolab.com/badge/SQLite-Database-07405E.svg?logo=sqlite&logoColor=white)
![Bootstrap](https://custom-icon-badges.demolab.com/badge/Bootstrap-UI-7952B3.svg?logo=bootstrap&logoColor=white)
![GitHub](https://custom-icon-badges.demolab.com/badge/Repo-GitHub-181717.svg?logo=github&logoColor=white)
![License](https://custom-icon-badges.demolab.com/badge/License-MIT-FFCC00.svg?logo=law&logoColor=black)
![Status](https://custom-icon-badges.demolab.com/badge/Status-Activo-28A745.svg?logo=check-circle&logoColor=white)
![Version](https://custom-icon-badges.demolab.com/badge/Version-1.0.0-007BFF.svg?logo=tag&logoColor=white)
![Tests](https://custom-icon-badges.demolab.com/badge/Tests-Pasados-17A2B8.svg?logo=checklist&logoColor=white)
![Contribuidores](https://custom-icon-badges.demolab.com/badge/Contribuidores-4-6F42C1.svg?logo=people&logoColor=white)
![Entorno](https://custom-icon-badges.demolab.com/badge/Entorno-Produccion-FD7E14.svg?logo=gear&logoColor=white)


<p align="center">
  <img src="https://i.imgur.com/RVGaecC.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>


# DIAGRAMA MMD

```mermaid
erDiagram

    Sucursal {
        int id PK
        string nombre
        string direccion
        string ciudad
        string telefono
        string imagen
    }

    User {
        int id PK
        string username
        string password
        string first_name
        string last_name
        string email
        string rol 
        string telefono
        string direccion
        bool activo
        string avatar
        string especialidad
        int sucursal_id FK
    }

    Propietario {
        int id PK
        int user_id FK
        string telefono
        string direccion
        string ciudad
        text notas
    }

    Paciente {
        int id PK
        string nombre
        string especie
        string raza
        string sexo
        date fecha_nacimiento
        int propietario_id FK
        text vacunas
        text alergias
        string foto
    }

    Cita {
        int id PK
        int paciente_id FK
        int veterinario_id FK
        int sucursal_id FK
        date fecha_solicitada
        datetime fecha_hora
        int duracion
        string tipo
        string estado
        text notas
    }

    HistorialMedico {
        int id PK
        int paciente_id FK
        int veterinario_id FK
        int cita_id FK
        datetime fecha
        text diagnostico
        text tratamiento
        text notas
        decimal peso
        decimal temperatura
        text examenes
        string imagenes
        date proximo_control
        bool sin_proximo_control
    }

    Farmaco {
        int id PK
        int sucursal_id FK
        string nombre
        string categoria
        text descripcion
        int stock
        datetime creado
        datetime actualizado
    }

    CitaFarmaco {
        int id PK
        int cita_id FK
        int farmaco_id FK
        int cantidad
        datetime registrado
    }

    VacunaRecomendada {
        int id PK
        string nombre
        string especie
        text descripcion
        int edad_recomendada
        string unidad_tiempo
        string refuerzo
        int orden
    }

    VacunaRegistro {
        int id PK
        int paciente_id FK
        int vacuna_id FK
        date fecha_aplicacion
        text notas
        datetime creado
        datetime actualizado
    }

    Producto {
        int id PK
        string nombre
        text descripcion
        string categoria
        decimal precio
        string imagen
        string telefono_contacto
        bool disponible
        datetime creado
        datetime actualizado
    }

    Sucursal ||--o{ User : "tiene"
    Sucursal ||--o{ Farmaco : "almacena"
    Sucursal ||--o{ Cita : "recibe"
    Sucursal ||--o{ Producto : "vende"

    User ||--|| Propietario : "representa"
    User ||--o{ Cita : "atiende"
    User ||--o{ HistorialMedico : "registra"

    Propietario ||--o{ Paciente : "posee"

    Paciente ||--o{ Cita : "genera"
    Paciente ||--o{ HistorialMedico : "tiene"
    Paciente ||--o{ VacunaRegistro : "recibe"

    Cita ||--|| HistorialMedico : "origina"
    Cita ||--o{ CitaFarmaco : "usa"

    Farmaco ||--o{ CitaFarmaco : "participa"

    VacunaRecomendada ||--o{ VacunaRegistro : "asociada"
```


<p align="center">
  <img src="https://i.imgur.com/zDTIHyR.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>


## 🌐 Sitio web (desactualizado ) (version anterior) (demo y preview desactualizada)
**https://sabuesofeliz.sbs**

<p align="center">
  <img src="https://i.imgur.com/zDTIHyR.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>


## Descripción
Sabueso Feliz es una plataforma web para la gestión integral de una veterinaria.  
Permite a administradores, veterinarios y propietarios de mascotas interactuar dentro de un mismo sistema, optimizando la atención y el control clínico de los pacientes.

<p align="center">
  <img src="https://i.imgur.com/zDTIHyR.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>

## Funcionalidades principales
- Panel de control por roles (Administrador, Veterinario, Propietario)
- Registro y gestión de mascotas y propietarios
- Agenda y asignación de citas médicas
- Registro del historial clínico digital
- Control de vacunas y recordatorios
- Módulo de tienda veterinaria
- Dashboard con indicadores e informes

<p align="center">
  <img src="https://i.imgur.com/zDTIHyR.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>


## Tecnologías utilizadas
- Python / Django (backend)
- HTML5, CSS3, JavaScript (frontend)
- SQLite (base de datos)
- Bootstrap 5 (interfaz)
- GitHub Pages + Hostinger (hosting)

<p align="center">
  <img src="https://i.imgur.com/zDTIHyR.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>


## Autores
Proyecto académico desarrollado por estudiantes del Instituto Técnico Salesiano Villada,  
como parte del Proyecto Integrador 2025.

<p align="center">
  <img src="https://i.imgur.com/zDTIHyR.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>


## Instalación y Configuración

1. Requisitos Previos:
  ```diff
  -   Python 3.11 o superior
  -   pip (gestor de paquetes de Python)
  -   virtualenv
```
2. Clonar el Repositorio:
  ```bash
  git clone https://github.com/Villada-PG3/trabajo-practico-integrador-veterinaria-el-sabueso-feliz.git
```
```bash
  cd trabajo-practico-integrador-veterinaria-el-sabueso-feliz-main
```
3. Crear Entorno Virtual:
```bash
  python -m venv venv
 ```
```bash
  source venv/bin/activate # En Windows: venv\Scripts\activate
```
4. Instalar Dependencias:
```bash
  pip install -r requirements.txt
```
6. Ejecutar Migraciones:
```bash
 python manage.py makemigrations
 ```
```bash
 python manage.py migrate
```
```bash
 python manage.py createsuperuser
```
7. Iniciar Servidor:
```bash
   python manage.py runserver
```
8. Acceder a: **http://localhost:8000**

<p align="center">
  <img src="https://i.imgur.com/zDTIHyR.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>


## Licencia
Proyecto de uso educativo y académico.  
© 2025 Sabueso Feliz – Todos los derechos reservados.












<p align="center">
  <img src="https://i.imgur.com/zDTIHyR.png" width="100%" alt="Banner Proyecto Integrador 2025">
</p>

# Contributors :



## 🔶 BRUNO SEGURA


<img src="https://img.shields.io/badge/ITSV-Instituto%20Villada-004AAD?style=for-the-badge&logo=book&logoColor=white">

[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/cromop1)  [<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg' alt='linkedin' height='40'>](https://www.linkedin.com/in/bruno-segura-1967a0315/)  [<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/discord.svg' alt='discord' height='40'>](https://discord.gg/wCjHs37Xt6)  

### ⚙️ Programador en :
<p align="left">
  <img src="https://skillicons.dev/icons?i=python,django,html,css,bootstrap,sqlite,git,github,vscode" />
</p>


![GitHub stats](https://github-readme-stats.vercel.app/api?username=cromop1&show_icons=true)  





## 🔶 Enzo Secchi

<img src="https://img.shields.io/badge/ITSV-Instituto%20Villada-004AAD?style=for-the-badge&logo=book&logoColor=white">

[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/zaaanaaa)  

### ⚙️ Programador en :
<p align="left">
  <img src="https://skillicons.dev/icons?i=python,django,html,css,bootstrap,sqlite,git,github,vscode" />
</p>


![GitHub stats](https://github-readme-stats.vercel.app/api?username=zaaanaaa&show_icons=true)  

 



## 🔶 Facundo Ledesma

<img src="https://img.shields.io/badge/ITSV-Instituto%20Villada-004AAD?style=for-the-badge&logo=book&logoColor=white">


[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/faculedesmaa)  

### ⚙️ Programador en :
<p align="left">
  <img src="https://skillicons.dev/icons?i=python,django,html,css,bootstrap,sqlite,git,github,vscode" />
</p>


![GitHub stats](https://github-readme-stats.vercel.app/api?username=faculedesmaa&show_icons=true)  



## 🔶 Ignacio Vago

<img src="https://img.shields.io/badge/ITSV-Instituto%20Villada-004AAD?style=for-the-badge&logo=book&logoColor=white">


[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/Vago132)  

### ⚙️ Programador en :
<p align="left">
  <img src="https://skillicons.dev/icons?i=python,django,html,css,bootstrap,sqlite,git,github,vscode" />
</p>

![GitHub stats](https://github-readme-stats.vercel.app/api?username=Vago132&show_icons=true)  





























