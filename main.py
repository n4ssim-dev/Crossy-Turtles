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
    time.sleep(0.1)

    scoreboard.write_score()

    screen.update()
    if player_item.ycor() == 280:
        player.reset_position()
        scoreboard.increment_score()

screen.exitonclick()
