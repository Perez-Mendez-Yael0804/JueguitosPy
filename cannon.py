"""
Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""
#Importación de librerías
from random import randrange
from turtle import *

from freegames import vector
#Definición de los vectores de cada elemento
ball = vector(-200, -200)
speed = vector(2, 2)
targets = []

#El programa responde ante los taps/clics hechos en la ventana
def tap(x, y):
    #Asignación de posición y velocidad si la pelota se encuentra fuera de los límites
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

#Duevuelve true en caso de que el vector se encuentre dentro de los límites establecidos
def inside(xy):
    
    return -250 < xy.x < 250 and -250 < xy.y < 250

#Función que dibujo los elementos correspondientes a la pelota y los distintos objetivos
def draw():
    
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

#Función que define el movimiento de la pelota simuando el tiro parabólico así como el de los objetivos teneindo movimiento constante hacia la izquierda
#Teniendno en cuenta la desaparición de los objetivos en cuando entran en contacto con la pelota
def move():
  
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(250, y)
        targets.append(target)

    #JUEGO INFINITO - Si los objetivos salen de los límites el juego no termina
    for target in targets:
        target.x -= 0.5
    
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    #Verificar distancia entre bola y obbjetivo
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    #Dibujar los objetivos
    draw()

    for target in targets:
        if not inside(target):
            # Eliminamos el return
            pass

    #Velocidad General del Juego
    ontimer(move, 20)

#Definimos las dimenciones de la ventana para que salgan y entren los objetivos
setup(520, 520, 370, 0) 
hideturtle()
up()
tracer(False)

#Se manda a llamar la función correpondiente al funcionamiento de los clicks
onscreenclick(tap)

#Poder mover la bala de cañon y mantener abierta la ventana
move()
done()
