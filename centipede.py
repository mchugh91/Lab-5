__author__ = 'Ciaran'

from turtle import *

def centipede(length, step, life):
    penup()
    theta = 0 #angle at which rotation occurs
    dtheta = 1 #angle at which second rotation occurs
    for i in range(life):
        forward(step)
        left(theta) #turns left theta degrees
        theta += dtheta # increases the rotation each loop
        stamp() #leaves a trail
        if i > length:
            clearstamps(1) # clears the trail
        if theta > 10 or theta < -10:
            dtheta = -dtheta #if the angle goes without above range, decrease the angle
        if ycor() > 200 or ycor() < -200:
            left(30)

def main():
    setworldcoordinates(-400, -400, 400, 400)
    centipede(14, 10, 300)
    exitonclick()

main()