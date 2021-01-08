from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move()

    def move(self):
        x_cor = self.xcor() + self.x_cor
        y_cor = self.ycor() + self.y_cor
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_cor *= -1

    def bounce_x(self):
        self.x_cor *= -1



