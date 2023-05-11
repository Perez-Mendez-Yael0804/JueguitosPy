""""
Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
#Importar las librerías necesarias
import math
from turtle import *

from freegames import vector

#Función que define la línea recta desde un punto inicial a un punto final definicod por cooredenadas (x,y)
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)



#Función que define la fígura cuadrado desde un punto inicial a un punto final, esta depende de los grados otorgados para que la fígura sea simétrica
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Función que define la fígura círculo donde las coordenadas (x,y) son usadas como el centro del círculo
# y la distancia entre vectores es utilizada como el radio del círculo.
def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(360):
        forward(1)
        left(1)
    end_fill()

#Función que define la fígura rectangulo desde un punto inicial a un punto final
#A diferencia del cuadrado fue necesario realizar una resta entre los distintos vertices para
#lograr la diferencia entre las dimensiones
def rectangle(start, end):

    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x  - start.x)
        left(90)
        forward(end.y  - start.y)
        left(90)

    end_fill()

#Función que define la fígura triangulon recibiendo como argumentos las coordenadas iniciales y finales
#La forma del triángulo se encuentra definida por el ángulo dado iterando la dirección en la que el lienzo dibuja
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(70)

    end_fill()



def tap(x, y):
    """Store starting point or draw shape."""
    # En la variable start se guarda el valor que se va a modificar en el diccionario de state
    start = state['start']

    # Si no hay un punto de inicio
    if start is None:
        # El diccionario state en la key 'start' sera igual al vector en coordenadas x y 
        state['start'] = vector(x, y)
    else:
        # La variable shape guarda el valor de la figura que hay en el diccionario
        shape = state['shape']
        # El punto fin es el segundo clic que se le da en las coordenadas x y
        end = vector(x, y)
        # 
        shape(start, end)
        # Cierra la figura y vuelve a ponerle un valor nulo para que no haya ningún punto 
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    # El state lo evalua en la key y le asigna el valor
    # Ejemplo: state['shape'] = line
    # lo que nos dice que la función lambda en el state trabajará sobre la figura de la línea
    state[key] = value

# Al iniciar el programa no hay punto de inicio y la figura por default es la línea
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
# Nuevo color
onkey(lambda: color('yellow'), 'Y')
# El shape es la llave(key) del diccionario y el valor es la figura
# onkey(lo que va a hacer, la tecla que debe apretar)
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
