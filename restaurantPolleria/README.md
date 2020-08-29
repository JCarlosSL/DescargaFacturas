# Aplicación para la Gestión de Facturas y Administración de Galpones
Este sistema se divide en 2 subproyectos. El modulo polleria es para administrar facturas de la empresa y el segundo para Administrar un Galpon de Cerdos.

## Pre-Requisitos
Para su intalacion del proyecto, debe tener las siguientes librerias

* Python en Window [Descargalo desde la pagina oficial](https://www.python.org/downloads/)

* Python en Linux
```sh
$ sudo apt-get install python3
```

* Dependencias en Linux
```sh
$ pip install django
$ pip install djangorestframework
$ pip install selenium
$ pip install django-crispy-forms
$ pip install Pillow
$ pip install django-selenium
```

## intalación

1. Clonar Repositorio
```sh
git Clone https://github.com/JCarlosSL/DescargaFacturas.git
```
## Compilación

1. Ingresar a la Carpeta restaurantPolleria y realizar los siguientes comandos en consola
```sh
python manage.py makemigrations home
python manage.py makemigrations cuenta

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```
2. Dirigete a el navegador y escribe la siguiente dirección
```sh
http://127.0.0.1:8000/
```

## Construido con

_Herramientas usadas en el proyecto_

* [Python](https://www.python.org/) - Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código
* [Django](https://www.djangoproject.com/) - Django es un framework de desarrollo web de código abierto, escrito en Python,
* [SQL](https://es.wikipedia.org/wiki/SQL) - SQL es un lenguaje de dominio específico utilizado en programación, diseñado para administrar, y recuperar información de sistemas de gestión de bases de datos relacionales
* [Selenium](https://www.selenium.dev/) - Selenium es un entorno de pruebas de software para aplicaciones basadas en la web. Selenium provee una herramienta de grabar/reproducir para crear pruebas sin usar un lenguaje de scripting para pruebas.

## Desarrolladores

- Barrionuevo Paredes, Fabricio Jose
- Mamani Panibra, Thales 
- Mamani Sucacahua, Rodrigo
- Oxa Cacya, Shirley
- Soncco Lupa, Jean Carlos
- Villanueva Sanchez, Fernando Thomas
