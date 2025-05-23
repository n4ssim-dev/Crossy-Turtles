from turtle import Turtle
from player import Player

WRITING_POSITION = (-280, 260)
FONT = ("Helvetica", 24, "normal")

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.score_writer = Turtle()
        self.score_writer.color("black")
        self.score_writer.penup()
        self.score_writer.hideturtle()
        self.score_writer.goto(WRITING_POSITION)

    def increment_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.score_writer.clear()
        self.score_writer.write(f"Score : {self.score}",align="left",font=FONT)

    def game_over(self):
        self.score_writer.clear()
        self.score_writer.goto(0,0)
        self.score_writer.write(f"GAME OVER", align="center", font=FONT)

