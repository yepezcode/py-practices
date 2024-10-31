import random
#import colorgram
#
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#
#for color in colors:
#    rgb_colors.append(( color.rgb.r, color.rgb.g, color.rgb.b ))
#
#
#print(rgb_colors)

import turtle as turtle_module

turtle_module.colormode(255)

art = turtle_module.Turtle()

color_list = [(215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]

art.hideturtle()
art.penup()
art.setheading(225)
art.forward(300)
art.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    art.dot(20, random.choice(color_list))
    art.forward(50)

    if dot_count % 10 == 0:
        art.setheading(90)
        art.forward(50)
        art.setheading(180)
        art.forward(500)
        art.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()