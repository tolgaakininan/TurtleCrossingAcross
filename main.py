from turtle import Screen
from player import Player
from gamecar import Gamecar
from scoreboard import Scoreboard
from time import sleep

game_is_on = True
ekran = Screen()
ekran.setup(width=800, height=800)
ekran.bgcolor("white")
ekran.listen()
ekran.tracer(0)
game_object = Player()
car_object = Gamecar()
skor = Scoreboard()
ekran.onkeypress(game_object.move, "Up")
while game_is_on:
    sleep(0.03)
    ekran.update()
    car_object.createcar()
    car_object.carmove()
    for car in car_object.cars:
        if car.distance(game_object) < 20:
            game_is_on = False
            skor.gameover()
    if int(game_object.ycor()) == 400:
        game_object.reset()
        skor.levelup()
        car_object.car_increase_speed()
ekran.exitonclick()
