from turtle import Turtle, Screen



tim = Turtle()

screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_clockwise():
    tim.right(15)

def rotate_couterclockwise():
    tim.left(15)

screen.listen()


actions = [('w', move_forwards), ('s', move_backwards), ('a', rotate_couterclockwise), ('d', rotate_clockwise)]


for action in actions:
    screen.onkey(key=action[0], fun=action[1])



screen.exitonclick()