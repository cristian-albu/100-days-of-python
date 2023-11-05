from turtle import Turtle, Screen
import random


tim = Turtle()
screen = Screen()



tim.shape('turtle')
tim.pensize(8)
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb_tuple = (r, g, b)
    return random_rgb_tuple

count = 3
DEGREES = 360

while count < 12:
    tim.color(random_color())
    for _ in range(count):
        tim.forward(100)
        tim.right(DEGREES / count)

    count += 1

screen.exitonclick()