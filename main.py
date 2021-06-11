from turtle import Turtle, Screen

def createTurtle():

    def move_forward():
        leo.forward(10)
    def move_backward():
        leo.back(10)

    def move_right():
        new_heading = leo.heading() + 10
        leo.setheading(new_heading)
    def move_left():
        new_heading = leo.heading() - 10
        leo.setheading(new_heading)
    def clear():
        leo.clear()
        leo.penup()
        leo.home()
        leo.pendown()

    leo = Turtle()
    screen = Screen()

    screen.listen()
    screen.onkey(key = "a", fun = move_left)
    screen.onkey(key = "d", fun = move_right)
    screen.onkey(key = "s", fun = move_backward)
    screen.onkey(key = "w", fun = move_forward)
    screen.onkey(key = "c", fun = clear)

    screen.exitonclick()


if __name__ == '__main__':
    createTurtle()

