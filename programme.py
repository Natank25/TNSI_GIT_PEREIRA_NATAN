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
    
def swap_color(num_ligne, num_colone):
    if (num_ligne + num_colone) % 2 == 0:
        color("black")
    else:
        color("white")


def draw_checkboard(taille):
    for num_ligne in range(8):
        for num_colone in range(8):
            swap_color(num_ligne, num_colone)
            up()
            offset_colone = (num_ligne - 4) * taille
            goto(offset_colone, num_colone * taille - taille * 4)
            down()
            draw_square(taille)
    

hideturtle()
taille = 50
speed(0)

draw_checkboard(taille)