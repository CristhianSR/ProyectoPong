import os
import turtle
import pygame

#Variables pausar el juego, puntaje máximo y el ganador de la partida
paused = False
max_points=5
winner=None

#Llame a la libreria pygame porque me daba error al instalar desde pip, simplesound de tkinter
pygame.init()
window= turtle.Screen()

#Ventana
window.title("Atari Pong")
window.setup(width=1420, height=720)
window.bgcolor("#008080")
window.tracer(0)

#Sonido al momento de la pelota golpear con la paleta
collision_sound = pygame.mixer.Sound("Bonk.mp3")  
background_music = pygame.mixer.Sound("sweden-minecraft.mp3") 

#Creación de rectángulos para jugador 1 y 2

player1=turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("#E0FFFF")
player1.penup()
player1.goto(-660,0)
player1.shapesize(stretch_wid=9,stretch_len=1)

player2=turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("#E0FFFF")
player2.penup() 
player2.goto(660,0)
player2.shapesize(stretch_wid=9,stretch_len=1)

#Creación de la pelota con sus características
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#E0FFFF")
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_wid=2,stretch_len=2)
ball.dx =4                  #Velocidad de la pelota en el eje x
ball.dy =4                  #Velocidad de la pelota en el eje y

#Creación del marcador de la partida
score1=0
score2=0
score = turtle.Turtle()
score.speed()
score.color("#E0FFFF")
score.penup()
score.hideturtle()

#Marcador en la pantalla del juego
score.goto(0,300)
score.write("Jugador 1: 0               Jugador 2:0", align="center", font=("San Francisco",20))

#Creación de la línea de la mitad del juego
red=turtle.Turtle()
red.color("#E0FFFF")
red.goto(0,400)
red.goto(0,-400)

#Mostrar mensaje por pantalla
text= turtle.Turtle()
text.color("#E0FFFF")
text.penup()
text.hideturtle()

text2= turtle.Turtle()
text2.color("#E0FFFF")
text2.penup()
text2.hideturtle()

#Funciones del jugador 1 para arriba y abajo, velocidad con la que se mueven los rectángulos
def player1_up():
    y=player1.ycor()
    y+=30
    if y < 275:
     player1.sety(y)

def player1_down():
    y=player1.ycor()
    y-=30
    if y >-275:
     player1.sety(y)

#Asignación de teclas para el jugador 1
window.listen()
window.onkeypress(player1_up,"w") 
window.onkeypress(player1_down,"s")

#Funciones del jugador 2
def player2_up():
    y=player2.ycor()
    y+=30
    if y < 275:
      player2.sety(y)

def player2_down():
    y=player2.ycor()
    y-=30
    if y > -275:
      player2.sety(y)
    
#Asignación de teclas para el jugador 2
window.listen()
window.onkeypress(player2_up,"Up")
window.onkeypress(player2_down,"Down")

#Función para ver el ganador
def check_winner():
    global winner
    if score1 >= max_points:
        winner = "Jugador 1"
        show_winner_screen()
        
    elif score2 >= max_points:
        winner = "Jugador 2"
        show_winner_screen()
        

# Función para enseñar el ganador por pantalla
def show_winner_screen():
    winner_window = turtle.Screen()
    winner_window.title("¡Tenemos un ganador!")
    winner_window.bgcolor("#E0FFFF")
    winner_text = turtle.Turtle()
    winner_text.speed(0)
    winner_text.color("#5F1741")
    winner_text.penup()
    winner_text.hideturtle()
    winner_text.goto(0, 0)
    winner_text.write("¡{} es el ganador!".format(winner), align="center", font=("San Francisco", 30))
    winner_window.mainloop()

#Función para pausar el juego
def game_pause():
    global paused
    paused=not paused
    if paused:
        window.title("Juego en Pausa")
        text.goto(0, 0)
        text.write("Juego en Pausa", align="center", font=("San Francisco", 30))
        text.goto(0, -50)
        text.write("Presiona la barra espaciadora para continuar", align="center", font=("San Francisco", 30))
        ball.dx, ball.dy = 4,4
        text.penup()
    else:
        ball.dx,ball.dy=4,4
        text.clear()
        window.title("Atari Pong")
        
#Función para salir del juego
def game_exit():
    global paused
    paused = True
    os._exit(0)

#Función para que las paletas regresen a su lugar despues de cada punto
def reset_window():
   ball.goto(0,0)
   ball.dx *=-1
   player1.goto(-660,0)
   player2.goto(660,0)


# Registrar teclas para, pausar y salir el juego
window.listen()
window.onkeypress(game_pause, "space")
window.onkeypress(game_exit, "Escape")


#Bucle while para ejecutar la mecánica del juego
while True:
  window.update() 
  if not paused:
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Bordes en y
    if ball.ycor() > 345:
        ball.dy *= -1

    if ball.ycor() < -345:
        ball.dy *= -1

    #Bordes en x
    if ball.xcor() > 710:
        ball.goto(0,0)
        ball.dx =4
        #Marcador para el jugador 1 
        score1 += 1
        score.clear()
        score.write("Jugador 1: {}                  Jugador 2: {}".format(score1,score2), align="center", font=("San Francisco",20))
        check_winner() 
        reset_window()

    if ball.xcor() < -710:
        ball.goto(0,0)
        ball.dx =-4
        #Marcador para el jugador 2
        score2 +=1
        score.clear()
        score.write("Jugador 1: {}                  Jugador 2: {}".format(score1,score2), align="center", font=("San Francisco",20))
        check_winner() 
        reset_window()

#Relación de aspecto de la pelota y paletas al momento de golpear

    if ((ball.xcor() < - 620 and ball.xcor() > -630)
          and (ball.ycor() < player1.ycor() + 100 and ball.ycor() > player1.ycor() - 100)):
        ball.dx *= -1
        collision_sound.play()
  
    if((ball.xcor() > 620 and ball.xcor() < 630)
          and(ball.ycor() < player2.ycor()+100 and ball.ycor() > player2.ycor()-100)):
        ball.dx *= -1
        collision_sound.play()
   

    
    