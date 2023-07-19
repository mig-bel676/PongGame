from turtle import Turtle
P_WIDTH = 0.7
P_LENGTH = 0.7
HEADING_FROM_TOP = 310
HEADING_FROM_BOTTOM = 130
BALL_SPEED = 3


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(P_WIDTH, P_LENGTH, 1.0)
        self.x_move = BALL_SPEED
        self.y_move = BALL_SPEED
        self.penup()

    # def set_launch_pong(self):
    #     if random.randint(1, 2) == 1:
    #         self.goto(0, 280)
    #         self.setheading(HEADING_FROM_TOP)
    #     else:
    #         self.goto(0, -280)
    #         self.setheading(HEADING_FROM_BOTTOM)

    def move_pong(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1

    def reset_to_left(self):
        self.goto(0, 0)
        self.xcor() - BALL_SPEED

    def reset_to_right(self):
        self.goto(0, 0)
        self.xcor() + BALL_SPEED

    def speed_up_right(self):
        self.x_move += 0.5

    def speed_up_left(self):
        self.x_move -= 0.5












