from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0, -350)

    def move(self):
        self.forward(10)

    def reset(self):

        self.goto(0, -350)
