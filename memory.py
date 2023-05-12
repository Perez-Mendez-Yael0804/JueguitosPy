"""
Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

"""
Como un elmento de innovación al juego, podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria?

Un elemento de innovación que utilizamos fue la implementación de emojis en las casillas, de esta manera
al jugador se le hará más fácil recordar cada uno de las figuras en vez de los dígitos. 
"""

from random import *
from turtle import *
from freegames import path

# Se define la imagen a utilizar 
car = path('car.gif')
# Son los símbolos mostrados al voltear las cartas
tiles = [
    '👻', '😱', '❤️', '😍', '😂', '👌', '😘', '😊',
    '😎', '😉', '😏', '🤩', '😅', '😁', '😶', '😗',
    '🤐', '😴', '🤗', '🤑', '🥱', '😤', '☹️', '😭', 
    '😵‍💫', '🤬', '🤯', '🤢', '🤠', '🤓', '🤡', '👽'
] * 2
# Marca el estado de la casilla
state = {'mark': None}
# Esconde todas las casillas
hide = [True] * 64
# Número de clics al iniciar el juego 
taps = 0

# Hace las casillas con los bordes 
def square(x, y):
    """Dibuja las casillas con bordes negros en las coordenadas (x,y) que recibe en los parametros"""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convierte a coordenadas x y las casillas en el indice marcado"""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convierte en casillas las coordenadas x y"""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Es la función que marca cuando una casillas ha sido seleccionada 
def tap(x, y):
    """Actualiza la marca de la casiila y la esconde según el tap"""
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    # imprime cuantos taps se llevan
    print(f"Llevas {taps} clics")

    # Cuando todas las casillas han sido destapadas
    if hide == [False] * 64:
        print("GANASTE")

# Dibuja la imagen cuando las casillas coinciden 
def draw():
    """Dibuja la imagen y las casillas"""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Se recorre la lista de las casillas verificando que estan ocultas o no
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    # Se muestra el valor de la ficha en la posición marcada
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 5, y +5)
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
