import turtle
import time
import random
from playsound import playsound
posponer = 0.09
import sounddevice as sd
import soundfile as sf
import pickle
from turtle import *




#marcador
coins = 0

high_coins = 0


high_coins = pickle.load(open("HighCoins.dat", "rb"))


#ventana
wn = turtle.Screen()
wn.title("this is not a snake game")
wn.bgpic("background.png")
wn.setup(width=1024, height=600)
wn.tracer(0)


turtle.register_shape('coin1.gif')
turtle.register_shape('coin2.gif')
turtle.register_shape('coin3.gif')
turtle.register_shape('snakehead.gif')
turtle.register_shape('snakeheadR.gif')
turtle.register_shape('snakeheadL.gif')
turtle.register_shape('snakeheadD.gif')



#monedas
moneda = turtle.Turtle()
moneda.speed(1)
moneda.shape('coin1.gif')
moneda.penup()
moneda.goto(30,70)
moneda.direction =  "stop"
moneda.color("gold")

moneda2 = turtle.Turtle()
moneda2.speed(1)
moneda2.shape('coin2.gif')
moneda2.penup()
moneda2.color("white")
moneda2.goto(2000,2000)
moneda2.direction =  "stop"
moneda2.hideturtle()


moneda3 = turtle.Turtle()
moneda3.speed(1)
moneda3.shape('coin3.gif')
moneda3.penup()
moneda3.color("Red")
moneda3.goto(2000,2000)
moneda3.direction =  "stop"
moneda3.hideturtle()



#cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("snakehead.gif")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction =  "stop"
cabeza.color("gray")



#segmentos

segmentos=[]


#texto

texto = turtle.Turtle()
texto.speed(0)
texto.color("White")
texto.penup()
texto.hideturtle()
texto.goto(0,240)
texto.write("Coins: 0                                   High coins: 0", align = "center", font = ("Times new roman", 24, "normal"))

#funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def derecha():
    cabeza.direction = "right"
def izquierda():
    cabeza.direction = "left"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety (y + 20)
        cabeza.shape('snakehead.gif')
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        cabeza.shape('snakeheadD.gif')

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        cabeza.shape('snakeheadR.gif')
       
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
        cabeza.shape('snakeheadL.gif')
       

#teclado
wn.listen()
wn.onkeypress(arriba, "w")
wn.onkeypress(izquierda, "a")
wn.onkeypress(abajo, "s")
wn.onkeypress(derecha, "d")
wn.onkeypress(arriba, "Up")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(abajo, "Down")
wn.onkeypress(derecha, "Right")



#bucle
while True:
    wn.update()
    wn.tracer(0)
    

    if coins == 50:
        moneda2.showturtle()
        moneda2.goto(60,-10)

    if coins == 100 or coins == 110:
        moneda3.showturtle()
        moneda3.goto(-100,50)

    pickle.dump(high_coins, open("HighCoins.dat", "wb"))
    
    texto.clear()
    texto.write("Coins: {}                                   High coins: {}".format(coins, high_coins), align = "center", font = ("Times new roman", 24, "normal"))
    

   

    #colisiones bordes


    if cabeza.xcor() > 435 or cabeza.xcor() < -440 or cabeza.ycor() > 205 or cabeza.ycor() < -220:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        playsound('death.wav')
        #resetear marcador
        coins = 0
        texto.clear()
        texto.write("Coins: {}                                   High coins: {}".format(coins, high_coins), align = "center", font = ("Times new roman", 24, "normal"))
        x = random.randint(-400, 400)
        y = random.randint(-205, 205)
        moneda.goto(x,y)
        moneda2.ht()
        moneda2.goto(2000,2000)
        moneda3.ht()
        moneda3.goto(2000,2000)
        #esconder segmentos

        for segmento in segmentos:
            segmento.goto(2000,2000)

        #limpiar lista
        segmentos.clear()


    if cabeza.distance(moneda) < 20:
        x = random.randint(-400, 400)
        y = random.randint(-205, 205)
        moneda.goto(x,y)
        playsound('coin.wav')
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0) 
        nuevo_segmento.shape("circle")
        nuevo_segmento.penup()
        nuevo_segmento.color("#2B5F2C")
        segmentos.append(nuevo_segmento)

        #marcador puntos

        coins+= 10

        if coins > high_coins:
            high_coins = coins

        texto.clear()
        texto.write("Coins: {}                                   High coins: {}".format(coins, high_coins), align = "center", font = ("Times new roman", 24, "normal"))

    if cabeza.distance(moneda2) < 20:
        a = random.randint(-400, 400)
        b = random.randint(-205, 205)
        moneda2.goto(a,b)
        playsound('coin2.wav')
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0) 
        nuevo_segmento.shape("circle")
        nuevo_segmento.penup()
        nuevo_segmento.color("#2B5F2C")
        segmentos.append(nuevo_segmento)





        #marcador puntos

        coins+= 20

        if coins > high_coins:
            high_coins = coins

        texto.clear()
        texto.write("Coins: {}                                   High coins: {}".format(coins, high_coins), align = "center", font = ("Times new roman", 24, "normal"))

    if cabeza.distance(moneda3) < 20:
        a = random.randint(-400,400)
        b = random.randint(-200,200)
        moneda3.goto(a,b)
        playsound('coin3.wav')

        #marcador puntos

        coins+= 30

        if coins > high_coins:
            high_coins = coins

        texto.clear()
        texto.write("Coins: {}                                   High coins: {}".format(coins, high_coins), align = "center", font = ("Times new roman", 24, "normal"))

# colision con cuerpo

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            playsound('death.wav')
            x = random.randint(-400, 400)
            y = random.randint(-205, 205)
            moneda.goto(x,y)
            moneda2.ht()
            moneda2.goto(2000,2000)
            moneda3.ht()
            moneda3.goto(2000,2000)
            for segmento in segmentos:
                segmento.ht()

            segmentos.clear()
       
            coins = 0
            texto.clear()
            texto.write("Coins: {}                                   High coins: {}".format(coins, high_coins), align = "center", font = ("Times new roman", 24, "normal"))
            



    #mover el cuerpo     
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

        
    mov()
    time.sleep(posponer)
turtle.done()