![Logo del freegames](https://pypi.org/static/images/logo-small.2a411bc6.svg) 
## Repositorio Proyecto Freegames
### Herramientas computacionales: El arte de la programación 

Este repositorio se caracteriza por ser una herramienta de aprendizaje para los alumnos, en la cual se trabajaron cinco códigos de la librería 'freegames' en python, 
de esta manera se pretende que los alumnos adquieran los conocimientos sobre: 

<ol>
<li>Uso de terminales para controlar tu computadora</li>
<li>Instalación de software desde la linea de comando</li>
<li>Editar, compilar y ejecutar programas desde la linea de comando</li>
<li>Uso de herramientas para control de versiones de código</li>
</ol>

## Comenzando 🚀
### Pre-requisitos 📋
<ul>
<li>Python 3.X</li>
<li>PIP instalado</li>
</ul>

Primero que nada es requisito tener el python 3.X, este lo puedes descargar directamente de la siguiente liga: https://www.python.org/downloads/

![Instalación python](https://github.com/Perez-Mendez-Yael0804/JueguitosPy/assets/72780700/7a1dd23f-2cf3-470d-98c8-671a6ccfbdb3)

Se debe de dar clic en Downloads, tomando en cuenta para que sistema operativo usas.

Normalmente en versiones de Python 2.7.9 (o superior) o Python 3.4 (o superior), PIP ya viene instalado con Python por defecto. Si está utilizando una versión anterior de Python, deberá seguir los pasos de instalación que se detallan a continuación.

<ol>
<li>Descargue el script del instalador get-pip.py. Si estás en Python 3.2, necesitarás esta versión de get-pip.py. En caso de tener Python 3.3 o 3.4 usar estas versiones de PiP correspondientemente Python 3.3 get-pip.py o Python 3.4 get-pip.py. De cualquier manera, haga clic derecho en el enlace y seleccione Guardar como y guárdelo en cualquier carpeta del pc, como su carpeta de Descargas.</li>
<li>Abra el símbolo del sistema y navegue hasta el archivo get-pip.py.</li>
<li>Ejecute el siguiente comando: python get-pip.py</li>
</ol>

📝 Nota: Ejecutar la terminal (CMD o Powershell) con privilegios de administrador
  
El anterior proceso es solo tomado en cuenta para Windows, en caso de tener otro sistema operativo puedes consultar la siguiente liga: https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/

Ahora lo que sigue es ver la instlación de la librería 'freegames'.

### Instalación 🔧

Para reafirmar que la instalación de pip haya sido correcta y completa, nos podemos apoyar del siguiente comando que rectificara la versión de pip instalada en el dispositivo:

```
pip --version
```

Tras obtener la ultima versión de Python 3.X que trae consigo el instalador "pip", se solicitó la instalación de la librería freegames que trae consigo un total de 17 juegos diferentes, esta acción se puede realizar directamente desde "Símbolo del Sistema" ó desde alguna de las distintas interfaces de manipulación de consola (Ubuntu/PowerShell/Git Bash), haciendo uso del siguiente comando:

```
python3 -m pip install freegames
```

## Ejecutando las pruebas - Librería freegames ⚙️

Para consultar el contenido de la librería es posible usar este comando que desplegará la lista de todos los juegos incluidos en la librería:
```
python3 -m freegames list
```
Tras seleccionar cualquier juego de interés, es posible correr el juegos desde la consola con el siguiente comando:
```
python3 -m freegames.snake
```
Los juegos se pueden modificar copiando su código fuente, este se puede obtener a partir del siguiente comando que creará una copia del archivo en nuestro directorio local:
```
python3 -m freegames copy snake
python3 snake.py
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Modificaciones hechas 🛠️


## Autores ✒️
Los autores que hicieron posible este proyecto fueron:

* **Marco Antonio González Fernández** - *Trabajo General* - [Markechy](https://github.com/Markechy)
* **Yael Octavio Pérez Méndez** - *Trabajo General* - [Yalk](https://github.com/Perez-Mendez-Yael0804)

