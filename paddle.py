from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(coordinates)
        self.speed("fastest")
        self.setheading(90)

    def up(self):
        if self.ycor() <= 220:
            self.setheading(90)
            self.forward(20)

    def down(self):
        if self.ycor() >= -220:
            self.setheading(270)
            self.forward(20)
