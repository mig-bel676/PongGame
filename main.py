import random
from turtle import Screen
from score_board import ScoreBoard
from player_block import PlayerBlock
from pong import Pong

screen = Screen()
screen.title("Miguel's Ping Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

player_block = PlayerBlock()
player_block.make_line()
score = ScoreBoard()
pong = Pong()
game_on = True

# Player 1
screen.onkey(key="w", fun=player_block.player1_up)
screen.onkey(key="s", fun=player_block.player1_down)
# Player 2
screen.onkey(key="Up", fun=player_block.player2_up)
screen.onkey(key="Down", fun=player_block.player2_down)

while game_on:
    screen.listen()
    screen.update()
    # Ball Hits wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce()
    # Ball Hitting Paddle
    if pong.distance(player_block.player_2) < 50 and pong.xcor() > 320:
        pong.hit()
    if pong.distance(player_block.player_1) < 50 and pong.xcor() < -330:
        pong.hit()
    # Player 1 makes score
    if pong.xcor() > 390:
        pong.speed_up_right()
        pong.reset_to_right()
        score.point_for_player1()
    # Player 2 makes score
    if pong.xcor() < -390:
        pong.speed_up_left()
        pong.reset_to_left()
        score.point_for_player2()
    pong.move_pong()

screen.exitonclick()




