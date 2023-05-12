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

## Modificaciones hechas 🛠️
### Juego-Paint 
Para este juego las modificaciones hechas fueron:
<ul>
<li>Un color nuevo</li>
<li>Dibujar un círculo</li>
<li>Completar el rectangulo</li>
<li>Completar el triángulo</li>
</ul>

### Juego-Sanke
Para este juego las modificaciones hechas fueron:
<ul>
<li>La comida se puede mover un paso a la vez al ser comida y  no deberá de salirse de la ventana</li>
<li>Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo.</li>
</ul>

### Juego-Memory 
Para este juego las modificaciones hechas fueron:
<ul>
<li>Contar y desplegar el numero de taps</li>
<li>Detectar cuando todos los cuadros se han destapado</li>
<li>Centrar el dígito en el cuadro</li>
<li>Como un elmento de innovación al juego, podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria?</li>
</ul>

### Juego-PacMan 
Para este juego las modificaciones hechas fueron:
<ul>
<li>Los fantasmas sean más listos</li>
<li>Cambiar el tablero</li>
<li>Hacer que los fantasmas sean más rápidos</li>
</ul>

### Juego-Tiro Parabólico 
Para este juego las modificaciones hechas fueron:
<ul>
<li>La velocidad del movimiento para el proyectil y los balones sea más rápida</li>
<li>Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen.</li>
</ul>

## Despliegue 📦

Para el despliegue de los videjuegos se requiere que se le haga un clone a este repositorio, de esta manera deberás acceder a la carpeta del repositorio clonado y mediante los siguiente comandos podrás correr los videojuegos.

```
cd Carpeta_clon_repositorio
python3 nombre_archivo.py
```

![Comando para correr el videojuego snake](https://github.com/Perez-Mendez-Yael0804/JueguitosPy/assets/72780700/97a28cac-11ab-4ab5-aeee-bf8ca1480cb4)

## Autores ✒️
Los autores que hicieron posible este proyecto fueron:

* **Marco Antonio González Fernández** - *Trabajo General* - [Markechy](https://github.com/Markechy)
* **Yael Octavio Pérez Méndez** - *Trabajo General* - [Yalk](https://github.com/Perez-Mendez-Yael0804)

