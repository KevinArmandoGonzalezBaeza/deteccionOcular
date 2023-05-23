# deteccionOcular.
desarollo del proyecto de I.A

## Requerimientos

Para poder utilizar el codigo de este repositorio es necesario tener los siguinetes requisitos

- Python a partir de la version 3 en adelante

Las siguientes librerias:

- opncv

- media pipe

- pyautogui

### Intrucciones de instalacion

## Instalacion de python 

### WINDOWS
descargar de la pagina oficial.
https://www.python.org/downloads/

En Windows, puede usar el py.exeprograma para ejecutar la última versión de Python,
comandos: 

- py -m pip install pyautogui


Si tiene varias versiones de Python instaladas, puede seleccionar cuál con un argumento de línea de comando para py. 

Por ejemplo, para Python 3.8, ejecute:

- py -3.8 -m pip install pyautogui

(probamos con varias versiones).


instalacion de open cv:

- pip install opencv-python, para instalar los módulos principales.
- pip install opencv-contrib-python, para instalar módulos principales y extras (contrib).
- pip install opencv-python-headless, instala módulos principales sin funcionalidad GUI.
- pip install opencv-contrib-python-headless, instala módulos principales y extras (contrib) sin funcionalidad GUI.

Se recomienda usar el comando pip install opencv-contrib-python

Una vez tengas todo instalado puedes continuar sin problemas.


## DEBIAN O UBUNTU
sudo apt install python3

para la instalacion de paquetes de python se recomienda usar su gesto de paquetes que es pip 

instalacion de mediapipe

comandos : 

- pip install mediapipe

instalacion de libreria  pyautogui:

- pip install pyautogui

instalacion de opencv

- pip install opencv-contrib-python

### Clonar el repositorio.

Ir al directorio dondefue guardado y una vez dentro podras ejecutar el programa:

Windows:

-py ./mouse.py

Ubuntu / Debian:

-python3 mouse.py

## Importante

si se esta ejecuntando el programa en un sistema operativo de linux se debe establecer como servidor grafico xorg ya que otros servidores como wayland no permiten el correcto funcionamiento de la libreria pyautogui






