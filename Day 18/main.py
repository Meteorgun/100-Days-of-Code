# from colorgram import colorgram

# part1
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)

# for i in colors:
#     rgb_colors.append(tuple(i.rgb))

# print(rgb_colors)
from turtle import Turtle, Screen
import random

# part2
timmy = Turtle()
screen = Screen()
screen.colormode(255)

l = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
     (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

timmy.ht()
timmy.speed(10)
timmy.penup()
timmy.setheading(225)
timmy.fd(300)
timmy.setheading(0)

for i in range(1, 101):
    timmy.dot(20, random.choice(l))
    timmy.fd(50)
    if i % 10 == 0:
        timmy.setheading(90)
        timmy.fd(50)
        timmy.setheading(180)
        timmy.fd(500)
        timmy.setheading(0)
screen.exitonclick()
