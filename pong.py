import os
import turtle

paused = False
max_points=2
winner=None


window= turtle.Screen()

#Ventana
window.title("Atari Pong")
window.setup(width=1420, height=720)
window.bgcolor("#48C1A6")
window.tracer(0)

#Creacion de reactangulos

player1=turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("#5F1741")
player1.penup()
player1.goto(-660,0)
player1.shapesize(stretch_wid=9,stretch_len=1)

player2=turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("#5F1741")
player2.penup() 
player2.goto(660,0)
player2.shapesize(stretch_wid=9,stretch_len=1)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#5F1741")
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_wid=2,stretch_len=2)
ball.dx =4
ball.dy =4

score1=0
score2=0

score = turtle.Turtle()
score.speed()
score.color("#5F1741")
score.penup()
score.hideturtle()

score.goto(0,300)
score.write("Jugador 1: 0               Jugador 2:0", align="center", font=("San Francisco",20))

red=turtle.Turtle()
red.color("white")
red.goto(0,400)
red.goto(0,-400)

text= turtle.Turtle()
text.color("#5F1741")
text.penup()
text.hideturtle()

#Funciones del jugador 1, velocidad
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

#Teclado para el jugador 1
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
    
#Teclado para el jugador 2
window.listen()
window.onkeypress(player2_up,"Up")
window.onkeypress(player2_down,"Down")

#Función para ver el ganador
def check_winner():
    global winner
    if score1 >= max_points:
        winner = "Jugador 1"
        show_winner_screen()
        reset_game()
    elif score2 >= max_points:
        winner = "Jugador 2"
        show_winner_screen()
        reset_game()

# Función para enseñar el ganador por pantalla
def show_winner_screen():
    winner_window = turtle.Screen()
    winner_window.title("¡Tenemos un ganador!")
    winner_window.bgcolor("#48C1A6")
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
        ball.dx, ball.dy = 3,3
        text.penup()
    else:
        ball.dx,ball.dy=3,3
        text.clear()
        window.title("Atari Pong")
        
def game_exit():
    global paused
    paused = True
    os._exit(0)


#Funcion para reiniciar el juego
def reset_game():
   global score1,score2,winner
   score1=0
   score2=0
   winner=None
   window.clear()
   ball.goto(0,0)
   ball.dx,ball.dy=3,3
   score.clear()
   score.write("Jugador 1: 0               Jugador 2:0", align="center", font=("San Francisco",20))
   #no vale esta vaina
    
# Registrar teclas para reiniciar, pausar y salir el juego
window.listen()
window.onkeypress(game_pause, "space")
window.onkeypress(game_exit, "Escape")
window.onkeypress(reset_game,"r")

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
        ball.dx =1
        score1 += 1
        score.clear()
        score.write("Jugador 1: {}                  Jugador 2: {}".format(score1,score2), align="center", font=("San Francisco",20))
        check_winner()
        
    if ball.xcor() < -710:
        ball.goto(0,0)
        ball.dx =-1
        score2 +=1
        score.clear()
        score.write("Jugador 1: {}                  Jugador 2: {}".format(score1,score2), align="center", font=("San Francisco",20))
        check_winner()
           
#Relacion de aspecto de la pelota y paletas al momento de golpear

    if ((ball.xcor() < - 620 and ball.xcor() > -630)
          and (ball.ycor() < player1.ycor() + 100 and ball.ycor() > player1.ycor() - 100)):
        ball.dx *= -1
  
    if((ball.xcor() > 620 and ball.xcor() < 630)
          and(ball.ycor() < player2.ycor()+100 and ball.ycor() > player2.ycor()-100)):
        ball.dx *= -1


    
    