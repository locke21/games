from turtle import Turtle


class Paddle:

    def __init__(self):
        self.rt_pad_parts = []
        self.lt_pad_parts = []
        self.right_paddle()
        self.left_paddle()

    def right_paddle(self):
        for parts in range(8):
            paddle_part = Turtle('square')
            paddle_part.penup()
            paddle_part.color('red')
            paddle_part.shapesize(stretch_wid=.5)
            paddle_part.goto(x=455, y=parts * 10)
            self.rt_pad_parts.append(paddle_part)

    def left_paddle(self):
        for parts in range(8):
            paddle_part = Turtle('square')
            paddle_part.penup()
            paddle_part.color('red')
            paddle_part.shapesize(stretch_wid=.5)
            paddle_part.goto(x=-455, y=parts * 10)
            self.lt_pad_parts.append(paddle_part)

    def rt_move_up(self):
        if self.rt_pad_parts[-1].ycor() <= 175:
            for parts in range(len(self.rt_pad_parts) - 1, -1, -1):
                self.rt_pad_parts[parts].setheading(90)
                self.rt_pad_parts[parts].forward(33)

    def rt_move_down(self):
        if self.rt_pad_parts[0].ycor() >= -170:
            for parts in range(0, len(self.rt_pad_parts)):
                self.rt_pad_parts[parts].setheading(270)
                self.rt_pad_parts[parts].forward(33)

    def lt_move_up(self):
        if self.lt_pad_parts[-1].ycor() <= 175:
            for parts in range(len(self.lt_pad_parts) - 1, -1, -1):
                self.lt_pad_parts[parts].setheading(90)
                self.lt_pad_parts[parts].forward(33)

    def lt_move_down(self):
        if self.lt_pad_parts[0].ycor() >= -170:
            for parts in range(0, len(self.lt_pad_parts)):
                self.lt_pad_parts[parts].setheading(270)
                self.lt_pad_parts[parts].forward(33)
