from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.printLevel()

    def printLevel(self):
        self.penup()
        self.hideturtle()
        self.goto(-245, 360)
        self.write(f"Level: {self.level}", align="center", font=("Arial", 20, "normal"))

    def gameover(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))

    def levelup(self):
        self.level += 1
        self.reset()
        self.printLevel()
