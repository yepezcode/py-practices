from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
   
def move_backwards():
    tim.forward(-10)

def move_clockwise():
    tim.right(10)

def move_counter_clockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()




screen.onkey(key='w', fun=move_forwards)
# todo S = backwards

screen.onkey(key='s', fun=move_backwards)
# todo A Counter - Clockwise
screen.onkey(key='a', fun=move_counter_clockwise)
# todo D = clockwise
screen.onkey(key='d', fun=move_clockwise)
# todo C = clear drwaing
screen.onkey(key='c', fun=clear)

screen.exitonclick()
