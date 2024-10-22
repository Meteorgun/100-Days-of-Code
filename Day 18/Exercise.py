from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)
# answer 1

# for i in range(4):
#     timmy.fd(100)
#     timmy.rt(90)


# answer 2
# for i in range(4):
#     timmy.fd(100)
#     timmy.penup()
#     timmy.rt(90)
#     timmy.fd(100)
#     timmy.pendown()

# answer 3
# l = ["blue", "dark slate gray", "cyan", "firebrick", "medium violet red",
#      "blue violet", "medium purple", "light green", "yellow", "dodger blue"]
# for i in range(3, 11):
#     r = random.randrange(10)
#     for j in range(i):
# timmy.color(l[r])
#         timmy.fd(100)
#         timmy.rt(360/i)


# print(random_colour())

# answer 4

# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# direction = [0, 90, 180, 270]

# for i in range(200):
#     rand_dir = random.choice(direction)
#     timmy.color(random_colour())
#     timmy.width(20)
#     timmy.speed(random.randrange(11))
#     timmy.fd(50)
#     timmy.rt(rand_dir)

# answer 5

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for i in range(360//size_of_gap):
        timmy.color(random_colour())
        timmy.speed(10)
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.circle(100)


draw_spirograph(90)
screen.exitonclick()
