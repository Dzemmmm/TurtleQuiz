import turtle
import random

score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#c6e2ff")
F0NT=("Arial",15,"bold")
turtle_list = []
score = 0
game_over = False
def setup_score_turtle():


    score_turtle.color("blue")
    score_turtle.hideturtle()
    top_high = screen.window_height() / 2
    y = top_high * 0.9


    score_turtle.penup()
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score 0", move=False,align="center",font=(F0NT))

def make_turtle(x,y):
    t = turtle.Turtle()
    def handle_click(x,y):
        global score
        score +=1
        score_turtle.clear()
        #print(x,y)
        score_turtle.write(arg="Score {}".format(score), move=False, align="center", font=(F0NT))


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x * 10 ,y * 10)
    turtle_list.append(t)

def setup_turtles():
    x_coordinates = [-20,-10,0,10,20]
    y_coordinates = [20,10,0,-10]
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtles_ramdomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_ramdomly,500)

def countdown(time):
    global game_over
    countdown_turtle.color("blue")
    countdown_turtle.hideturtle()
    top_high = screen.window_height() / 2
    y = top_high * 0.8
    countdown_turtle.penup()
    countdown_turtle.setpos(0, y)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=(F0NT))
        screen.ontimer(lambda: countdown(time - 1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg=f"Game Over", move=False, align="center", font=(F0NT))

def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_ramdomly()
    countdown(10)
    turtle.tracer(1)



start_game_up()
turtle.mainloop()