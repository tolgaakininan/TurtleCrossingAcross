from turtle import Turtle
from random import choice, randint

colors = ["yellow", "green", "red", "blue", "black"]


class Gamecar():
    def __init__(self):
        self.cars = []
        self.carspeed=10

    def createcar(self):
        if randint(1, 5) == 3:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1.5, 3)
            new_car.color(choice(colors))
            y_cor = randint(-250, 250)
            new_car.goto(400, y_cor)
            self.cars.append(new_car)

    def carmove(self):
        for car in self.cars:
            car.backward(self.carspeed)

    def car_increase_speed(self):
        self.carspeed+=2

