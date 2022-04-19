import turtle
from statetyper import Statetyper
import pandas
from turtle import Turtle
import time

attempt = 0
score = 0
game_is_on = True
screen = turtle.Screen()
screen.title("India State Guess")
data = pandas.read_csv("statecor.csv")
image = "India-locator-map-blank1.gif"
screen.addshape(image)
turtle.shape(image)
screen.bgcolor("#F7E6CA")
lt = data["State"].tolist()
score_t = Turtle()
attempt_t = Turtle()
correct_answers = []
text = Turtle()
text.hideturtle()
text.penup()
text.goto(0, -200)


def top_panel(s, a):

    score_t.hideturtle()
    attempt_t.hideturtle()
    score_t.penup()
    attempt_t.penup()
    score_t.goto(200, 290)
    attempt_t.goto(-340, 290)
    score_t.write(f"Score: {s}/29", font=('Arial', 20, 'bold'))
    attempt_t.write(f"Attempts: {a}/35", font=('Arial', 20, 'bold'))


while game_is_on:

    top_panel(score, attempt)
    movement = Statetyper()
    answer = screen.textinput(title="Guess state name", prompt="Enter state name")
    if movement.state_checker(answer, lt):
        lt.remove(answer)
        correct_answers.append(answer)
        listt = data[data.State == answer]
        s_name = listt.values[0][0]
        x = float(listt.values[0][1])
        y = float(listt.values[0][2])
        movement.statename(x, y, s_name)
        correct_answers.append(answer)
        score += 1
        text.color("green")
        text.write(arg="Correct Guess", font=('Arial', 20, 'bold'))
        time.sleep(0.5)
        text.clear()
    else:
        if movement.state_checker(answer, correct_answers):
            text.color("red")
            text.write(arg="State Already Answered", font=('Arial', 20, 'bold'))
            time.sleep(0.5)
            text.clear()
        else:
            text.color("red")
            text.write(arg="Incorrect Guess", font=('Arial', 20, 'bold'))
            time.sleep(0.5)
            text.clear()

    attempt += 1
    score_t.clear()
    attempt_t.clear()
    if attempt == 35 or score == 29:
        top_panel(score, attempt)
        game_is_on = False

turtle.color("red")
turtle.write(arg="Game Over", align="center", font=('Arial', 50, 'bold'))
screen.exitonclick()
