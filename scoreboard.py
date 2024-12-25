from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", False, "Center", font=("Baskerville Old Face", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", False, "Center", font=("Baskerville Old Face", 20, "normal"))
