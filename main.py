import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Turtle")
screen.tracer(0)

screen.listen()

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkeypress(lambda: player.move_player(),"Up")

game_is_on = True

while game_is_on:
    player_item = player.player
    car_list = car.cars
    player_position = player_item.xcor()

    time.sleep(0.05)

    car.create_car()
    car.move_cars()
    scoreboard.write_score()

    screen.update()

    if player_item.ycor() >= 280:
        player.reset_position()
        scoreboard.increment_score()
        car.clear_cars()

    for car_item in car_list:
        if car_item.distance(player_item) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

screen.exitonclick()
