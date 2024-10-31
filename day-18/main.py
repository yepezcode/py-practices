import random
from turtle import Turtle, Screen

# Turtle 
#timmy_the_turtle = Turtle()
#
#for _ in range(15):
#    timmy_the_turtle.forward(10)
#    timmy_the_turtle.penup()
#    timmy_the_turtle.forward(10)
#    timmy_the_turtle.pendown()

# config

def draw_figures():
    figure = Turtle()
    #figure.hideturtle()
    figure.teleport(-150,200)
    figure.speed(1)
    for no_angles in range(3,11):
        random_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        angle_degrees = 360/no_angles
        for _ in range(no_angles):
            figure.color(random_color)
            figure.forward(150)
            figure.right(angle_degrees)

def draw_random_walk():
    walk = Turtle()
    walk.speed(9)
    walk.width(9)
    random_movement=[0,90,180,270]
    for _ in range(400):
        random_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        walk.color(random_color)
        walk.setheading(random.choice(random_movement))
        walk.forward(25)

def draw_spirograph():
    circle = Turtle()
    circle.speed('fastest')

    for angle in range(360):
        random_color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))

        circle.color(random_color)
        circle.circle(100)
        circle.right(angle)


draw_spirograph()

screen = Screen()
screen.exitonclick()


