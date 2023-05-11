""""
Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
import math
from turtle import *

from freegames import vector


def line(start, end):
    """Dibuja la línea dado un punto 'star' y 'end' mostrados en los paramteros"""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Dibuja un cuadrado dado un punto 'star' y 'end' mostrados en los paramteros"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Dibuja un círculo dado un punto 'star' mostrados en los paramteros"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(360):
        forward(1)
        left(1)
    end_fill()

def rectangle(start, end):
    """Dibuja un rectangulo dado un punto 'star' y 'end' mostrados en los paramteros"""
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


def triangle(start, end):
    """Dibuja un triángulo dado un punto 'star' y 'end' mostrados en los paramteros"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(70)

    end_fill()



def tap(x, y):
    """Detecta cuando se ha hecho un clic y guarda el punto inicial y luego al hacer un segundo
    clic guarda el 2do punto para realizar la forma de la figura, por lo que recibe coordenadas (x,y)"""
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
    """Es una función que indica que figura se hará recibiendo como parametros:
    1. Key: La cual es el indice que busca en el diccionario state
    2. Value: Es el valor de la key en el diccionario"""
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
