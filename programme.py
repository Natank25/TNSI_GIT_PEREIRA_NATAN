from turtle import *

def draw_square(taille):
    begin_fill()
    forward(taille)
    left(90)
    forward(taille)
    left(90)
    forward(taille)
    left(90)
    forward(taille)
    left(90)
    end_fill()
    
    
hideturtle()
taille = 50
speed(0)
for b in range(8):
    for c in range(8):
        if (b + c) % 2 == 0:
            color("black")
        else:
            color("white")
        up()
        d = (b - 4) * taille
        goto(d, c * taille - taille * 4)
        down()
        draw_square(taille)
        

