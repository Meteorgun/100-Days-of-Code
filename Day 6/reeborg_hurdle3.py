# Hurdle 3 Answer

def right():
    turn_left()
    turn_left()
    turn_left()


def corner():
    turn_left()
    move()


while not at_goal():
    if front_is_clear() and right_is_clear():
        right()
        if front_is_clear():
            move()
    elif not front_is_clear() and not right_is_clear():
        turn_left()
        if not front_is_clear() and not right_is_clear():
            turn_left()
            move()
    elif wall_in_front():
        corner()
    elif front_is_clear():
        move()
