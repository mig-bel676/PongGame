from turtle import Turtle
FONT = "Comic Sans MS"
FONTSIZE = 60
L_SCORE_POSITION = (-80, 220)
R_SCORE_POSITION = (39, 220)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.left_number = 0
        self.penup()
        self.left_score()
        self.right_number = 0
        self.penup()
        self.right_score()

    def left_score(self):
        self.goto(L_SCORE_POSITION)
        self.pendown()
        self.write(f"{self.left_number}", font=(FONT, FONTSIZE, 'normal'))

    def right_score(self):
        self.goto(R_SCORE_POSITION)
        self.write(f"{self.right_number}", font=(FONT, FONTSIZE, 'normal'))

    def point_for_player1(self):
        self.left_number += 1
        self.update_score()

    def point_for_player2(self):
        self.right_number += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(L_SCORE_POSITION)
        self.write(f"{self.left_number}", font=(FONT, FONTSIZE, 'normal'))
        self.goto(R_SCORE_POSITION)
        self.write(f"{self.right_number}", font=(FONT, FONTSIZE, 'normal'))





