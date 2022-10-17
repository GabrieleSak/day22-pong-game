from random import randint
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.angle = randint(0, 360)
        self.ball_speed = 10

    def move(self):
        self.setheading(self.angle)
        self.forward(self.ball_speed)

    def bounce(self):
        self.angle = 360 - self.angle

    def bounce_paddle(self):
        self.angle = 180 - self.angle

    def restart(self):
        self.goto(0, 0)
        self.angle = 180 - self.angle

    def speed_up(self):
        if self.ball_speed <= 55:
            self.ball_speed += 1
