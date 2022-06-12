from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_position, y_position)

    #functions below move the paddles up and down and is called in the main class
    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    # resets the paddles to the original position which is defined in the main class
    def reset_position(self, x, y):
        self.goto(x=x, y=y)







