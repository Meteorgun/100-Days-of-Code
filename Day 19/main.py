from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="which colour do you pick?")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=100-i*30)
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_colour:
                print("Hurray! You won")
            else:
                print(f"Too bad! The winning colour is {winning_colour}")
        r = random.randint(0, 10)
        turtle.fd(r)
screen.exitonclick()
