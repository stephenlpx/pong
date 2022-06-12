from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    #updates and sets position of the score for the left and write player
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, font=("Courier", 60, "normal"))


    #increases the score for the left player
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    #increase the score of the right player
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    