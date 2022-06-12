from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.reset_ball()
        self.move_speed = 0.1

    #move the ball in a diagonal position
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    #change the direction of the y coordiante
    def bounce_y(self):
        self.y_move *= -1


    #chance direction of the x coordinate
    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()

