import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create()
    cars.move()

    # Turtle reaches the finish line
    if player.reached_finish():
        player.reset()
        score.level_up()
        cars.increase_speed()

    # Turtle collides with a car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()

















screen.exitonclick()