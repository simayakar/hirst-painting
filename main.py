# import colorgram
#
#
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
#
# def get_colors():
#     for color in colors:
#         rgb = color.rgb
#         color_t = (rgb[0], rgb[1], rgb[2])
#         print(color_t)
#         color_list.append(color_t)
#     print(color_list)
#
# get_colors()

import turtle as tur
import random

t = tur.Turtle()
tur.colormode(255)
t.speed('fastest')

color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (26, 108, 164), (193, 38, 81), (237, 161, 50),
              (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
              (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
              (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
              (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

t.penup()
t.setposition(-250,-250)


for i in range(10):
    current_pos = t.pos()
    for j in range(10):
        t.pendown()
        rgb_color = random.choice(color_list)
        t.color(rgb_color)
        t.dot(20)
        t.penup()
        t.forward(50)
    t.setposition(current_pos[0], current_pos[1] + 50)



s = tur.Screen()
s.exitonclick()