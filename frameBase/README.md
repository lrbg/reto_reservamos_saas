# Automatización de Pruebas para Reservamos SaaS

Este proyecto contiene pruebas automatizadas para el sitio web de Reservamos SaaS, utilizando Selenium con Python para simular y verificar comportamientos clave en la plataforma.

## Pre-requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Configuración del entorno

### Clonación del repositorio

Primero, clona este repositorio en tu máquina local utilizando Git:
git clone https://github.com/lrbg/reto_reservamos_saas.git
cd reto_reservamos_saas

### Instalación de dependencias

Instala las dependencias necesarias ejecutando:
pip install -r requirements.txt

Este comando instalará Selenium y PyTest, junto con cualquier otra dependencia listada en `requirements.txt`.

## Estructura del Proyecto

El proyecto se organiza de la siguiente manera:

- `conftest.py`: Configuraciones de PyTest y Selenium WebDriver para inicializar y finalizar sesiones de navegador.
- `tests/`: Carpeta que contiene los scripts de prueba.
  - `test_ticket_search.py`: Script de prueba principal que simula una búsqueda de tickets y otras acciones en el sitio.

## Ejecución de pruebas

Para ejecutar las pruebas y generar un reporte HTML, utiliza el siguiente comando:

pytest tests/test_ticket_search.py --html=report.html

Este comando ejecutará las pruebas definidas en `test_ticket_search.py` y creará un archivo `report.html` en el directorio actual, el cual puedes abrir con cualquier navegador para visualizar el resultado de las pruebas.

## Contribuir

Si estás interesado en contribuir a este proyecto, por favor, crea un fork del repositorio, realiza tus cambios y envía un Pull Request con tus mejoras o correcciones.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Para más información, revisa el archivo `LICENSE` en este repositorio.

## Contacto

Si tienes preguntas o deseas discutir más sobre este proyecto, no dudes en contactarme en: [lrbg_02@hotmail.com].
