from turtle import Turtle, Screen
# challenge to make an etch-a-sketch program
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)


def move_backward():
    tim.back(10)


def turn_left():
    tim.lt(10)


def turn_right():
    tim.rt(10)


def clear_screen():
    # tim.reset()
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
