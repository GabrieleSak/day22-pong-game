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

    def move(self):
        self.setheading(self.angle)
        self.forward(10)

    def bounce(self):
        self.angle = 360 - self.angle


