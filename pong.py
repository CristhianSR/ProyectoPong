import turtle

window= turtle.Screen()

window.title("Atari Pong")
window.setup(width=1420, height=720)
window.bgcolor("#48C1A6")
window.tracer(0)

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
ball.dx =2
ball.dy =2

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


#Funciones del jugador 1
def player1_up():
    y=player1.ycor()
    y+=15
    player1.sety(y)

def player1_down():
    y=player1.ycor()
    y-=15
    player1.sety(y)

#Teclado para el jugador 1
window.listen()
window.onkeypress(player1_up,"w") 
window.onkeypress(player1_down,"s")

#Funciones del jugador 2
def player2_up():
    y=player2.ycor()
    y+=15
    player2.sety(y)

def player2_down():
    y=player2.ycor()
    y-=15
    player2.sety(y)
    
#Teclado para el jugador 2
window.listen()
window.onkeypress(player2_up,"Up")
window.onkeypress(player2_down,"Down")


while True:
    window.update()

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
        
        
    if ball.xcor() < -710:
        ball.goto(0,0)
        ball.dx =-1
        score2 +=1
        score.clear()
        score.write("Jugador 1: {}                  Jugador 2: {}".format(score1,score2), align="center", font=("San Francisco",20))

        
        

    if ((ball.xcor() < - 620 and ball.xcor() > -630)
          and (ball.ycor() < player1.ycor() + 100 and ball.ycor() > player1.ycor() - 100)):
        ball.dx *= -1
  
    if((ball.xcor() > 620 and ball.xcor() < 630)
          and(ball.ycor() < player2.ycor()+100 and ball.ycor() > player2.ycor()-100)):
        ball.dx *= -1



  


    


    





 