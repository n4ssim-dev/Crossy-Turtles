from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player:
    def __init__(self):
        self.move_distance = MOVE_DISTANCE
        self.player_color = "orange"
        self.player = Turtle("turtle")
        self.create_player()

    def create_player(self):
        self.player.color(self.player_color)
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)

    def move_player(self):
        self.player.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.player.goto(STARTING_POSITION)
