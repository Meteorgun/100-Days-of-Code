# maze world answer
def right():
    turn_left()
    turn_left()
    turn_left()


def corner():
    turn_left()
    move()


while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        right()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear():
        right()
