"""
Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""
#Importar random para generar números aleatorios en las variables comi y serp
import random

comi = random.randint(1, 5)
serp = random.randint(1, 5)

#Ciclos if que definirán el color de la comida y serpiente dependiendo del número aleatorio que toca.
color = ['green', 'orange', 'blue', 'purple', 'yellow']
if color[serp] != color[comi]:
    color1 = color[serp]
    color2 = color[comi]
else: 
    color1="orange"
    color2="green"

#Importar la libería freegames y random
from random import randrange
from turtle import *

from freegames import square, vector

#Ceación de vectores para cada uno de los elementos
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Cambio de dirección de la serpiente
def change(x, y):
    
    aim.x = x
    aim.y = y

#La cabeza de la serpiente dentro de los límites de la cuadrícula
def inside(head):

    return -200 < head.x < 190 and -200 < head.y < 190

#Mover la serpiente hacia adelante un segmento.
def move():
  
    head = snake[-1].copy()
    head.move(aim)
#Si la serpiente se sale de los límites se acaba el juego y la cabeza se ilumina de rojo
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #Ciclo if que define que la cómida se moverá un paso a la vez después de ser consumida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-1, 1) * 10
        food.y = randrange(-1, 1) * 10
    else:
        snake.pop(0)

    clear()
    #Definición de los colores para los elementos snake y food dependiente de los valores aleatorios definidos al inicio
    for body in snake:
        square(body.x, body.y, 9, color1)

    square(food.x, food.y, 9, color2)
    update()

    #Velocidad del juego GENERAL
    ontimer(move, 100)

#Definición de las dimensiones de la ventana emergente
setup(420, 420, 370, 0)

#Ocultar el cursor
hideturtle()
tracer(False)
listen()

#Definición de los controles que manejaran a la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
