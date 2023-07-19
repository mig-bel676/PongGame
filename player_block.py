from turtle import Turtle, Screen
from pong import Pong
import random

STARTING_POSITIONS = [(-340, 0), (330, 0)]
LENGTH = 0.5
WIDTH = 2.8
HEADING = [90, 270]

MOVEMENT_INCREMENT = 50

screen = Screen()


class PlayerBlock:
    def __init__(self):
        super().__init__()
        self.players = []
        self.create_players()
        self.player_1 = self.players[0]
        self.player_2 = self.players[1]

    def create_players(self):
        for position in STARTING_POSITIONS:
            player_block = Turtle("square")
            player_block.penup()
            player_block.shapesize(WIDTH, LENGTH, 1.0)
            player_block.color("white")
            player_block.goto(position)
            self.players.append(player_block)

    def make_line(self):
        for head in HEADING:
            line_divider = Turtle()
            line_divider.hideturtle()
            line_divider.setheading(head)
            line_divider.pensize(3)
            line_divider.pencolor("white")
            for up in range(15):
                line_divider.forward(10)
                line_divider.penup()
                line_divider.forward(10)
                line_divider.pendown()

    # Player 1 Movements
    def player1_up(self):
        new_y = self.player_1.ycor() + MOVEMENT_INCREMENT
        self.player_1.sety(new_y)

    def player1_down(self):
        new_y = self.player_1.ycor() - MOVEMENT_INCREMENT
        self.player_1.sety(new_y)

    # Player 2 Movements
    def player2_up(self):
        new_y = self.player_2.ycor() + MOVEMENT_INCREMENT
        self.player_2.sety(new_y)

    def player2_down(self):
        new_y = self.player_2.ycor() - MOVEMENT_INCREMENT
        self.player_2.sety(new_y)


