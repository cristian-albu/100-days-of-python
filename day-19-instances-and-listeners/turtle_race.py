from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

turtles_props = ['orange', 'red', 'blue', 'green', 'purple']
turtles = []

x = -230
y = -150

for color in turtles_props:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=x, y=y)
    y += 50
    turtles.append(turtle)


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won")
            else:
                print("You've lost")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()