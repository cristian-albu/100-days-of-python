from turtle import Turtle, Screen


tim = Turtle()
tim.shape('turtle')
tim.color('red')

screen = Screen()

def dash_forward(turtle:Turtle, distance:int):
    for _ in range(round(distance/20)):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


for _ in range(4):
    dash_forward(tim, 100)
    tim.right(90)

screen.exitonclick()