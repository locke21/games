from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
centipede_movement = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.make_segment()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def make_segment(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape='square')
        snake_segment.penup()
        snake_segment.color('white')
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def snake_movement(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            last_position = self.segments[seg - 1].xcor(), self.segments[seg - 1].ycor()
            self.segments[seg].goto(last_position)
        self.segments[0].forward(centipede_movement)

    def game_over(self):
        for seg in self.segments:
            seg.goto(800, 800)
        self.segments.clear()
        self.make_segment()
        self.head = self.segments[0]

