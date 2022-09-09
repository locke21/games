from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.color('blue')
        self.speed('fastest')
        self.spawn_food()

    def spawn_food(self):
        self.goto(random.randint(-260, 260), random.randint(-260, 260))

    def create_more_food(self):
        self.spawn_food()

