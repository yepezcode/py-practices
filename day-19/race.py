from turtle import Turtle, Screen
import random

class TurtleRace:

    def __init__(self, color, position_x, position_y):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.turtle = Turtle(shape="turtle")
        self.turtle.penup()
        self.turtle.color(self.color)
        self.turtle.goto(x=self.position_x, y=self.position_y)

    def run_turtle(self):
        rand_distance = random.randint(0,10)
        self.turtle.forward(rand_distance)

    def get_position_x(self):
        return self.turtle.xcor()



screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?: Enter a color: ")


colors = ["red", "orange", "yellow", "green", "blue", "purple"]


turtles_racer = []

for turtle_index in range(0,6):
    position_x = -230
    position_y = -70
    position_y += turtle_index * 30
    racer = TurtleRace(colors[turtle_index], position_x, position_y)
    turtles_racer.append(racer)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in turtles_racer:
        # stop the race in case any turtle win
        
        if turtles.get_position_x() > 230:
            is_race_on = False
            winning_color = turtles.color
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        turtles.run_turtle()

screen.exitonclick()