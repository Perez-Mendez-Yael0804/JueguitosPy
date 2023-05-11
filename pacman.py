"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.
"""

from random import choice
from turtle import *

from freegames import floor, vector

# Se inicializa el state como un diccionario con una key llamada score de valor 0
# Este es el puntaje que empieza en 0 y luego se irá modificando
state = {'score': 0}
# Almacena el camino que sigue el pacman
path = Turtle(visible=False)
#
writer = Turtle(visible=False)
# Indica la dirección en la que se mueve el pacman 
aim = vector(5, 0)
# Es la coordenada donde se encuentra
pacman = vector(-40, -80)
# Es la posición donde se encuentran los fantasmas 
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
# fmt: off
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on

# Pinta los cuadros azules 
def square(x, y):
    """Dibuja el cuadrado usando la función path - Recibe coordenadas (x,y)"""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Devuelve el desplazamiento del punto en mosaicos. - Recibe point"""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Valida el punto 
def valid(point):
    """Retorna True si el punto es válido en mosaicos. - ecibe point"""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Dibuja la cuadrícula de Pacman deacuerdo a los parámetros establecidos"""
    # Color del fondo
    bgcolor('black')
    # Color del camino
    path.color('blue')

    # index en el rango del tamaño del tablero
    for index in range(len(tiles)):
        # la variable tile se le agrega el valor del tablero en la posición 1, 2, 3...
        tile = tiles[index]
        # Si la posición de tile es mayor a 0
        if tile > 0:
            # x toma el valor de index modulo de 20 por 20 menos 200
            x = (index % 20) * 20 - 200
            # y toma el valor de 180 - el indice entre 20 tomando el número entero multilpicado por 20
            y = 180 - (index // 20) * 20
            # manda a llamar a la función square dandole las coordenadas x y
            square(x, y)

            # Si tile es 1
            if tile == 1:
                # El camino azul sube
                path.up()
                # a x se le suma 10 y a y se le suma 10
                path.goto(x + 10, y + 10)
                # en el camino se hace un punto de tamaño 2 y blancos
                path.dot(2, 'white')


def move():
    """Función que define el movimiento de PacMan y los fantasmas"""
    writer.undo()
    writer.write(state['score'])

    clear()
    """Pacman + la posición inicial"""
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            #Ciclos if que definen la inteligencia de los fantasmas al tener a Pacman cerca y priorizar el camino mas cercano aumentando su velocidad
            if pacman.x > point.x and pacman.y > point.y: 
                options = [
                vector(10, 0),
                vector(10, 0),
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, 10),
                vector(0, 10),
                vector(0, -10),
            ]
            elif pacman.x < point.x and pacman.y > point.y:
                options = [
                vector(10, 0),
                vector(-10, 0),
                vector(-10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, 10),
                vector(0, 10),
                vector(0, -10),
            ]
            elif pacman.x > point.x and pacman.y < point.y:
                options = [
                vector(10, 0),
                vector(10, 0),
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
                vector(0, -10),
                vector(0, -10),
            ]
            elif pacman.x < point.x and pacman.y < point.y:
                options = [
                vector(10, 0),
                vector(-10, 0),
                vector(-10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
                vector(0, -10),
                vector(0, -10),
                ]

            else:
                options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            # Se eleije un fantasma al que mover
            plan = choice(options)

            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    # Cuando el pacman se topa con el fantasma no deja que pase mas allá del fantasma
    for point, course in ghosts:
        if abs(pacman - point) < 25:
            return

    ontimer(move, 35)


def change(x, y):
    """Cambia la dirección del pacman con las coordenadas x y recibidas - Recibe (x,y)"""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Tamaño de la ventana emergente 
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
# escribe la posición
writer.goto(160, 160)
# Escribe el color de los puntos 
writer.color('white')
# Escribe el score del jugador 
writer.write(state['score'])
listen()
# Cambia la dirección en la que se mueve el pacman llamando a la función change
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
