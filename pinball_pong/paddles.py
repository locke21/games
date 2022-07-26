import turtle
import time


left_xcor = -455
lt_pad_starting_pt = [(left_xcor, 10), (left_xcor, 25), (left_xcor, 40),
                      (left_xcor, 55), (left_xcor, 70), (left_xcor, 85), (left_xcor, 100), ]

right_xcor = 455
rt_pad_starting_pt = [(right_xcor, 10), (right_xcor, 25), (right_xcor, 40),
                      (right_xcor, 55), (right_xcor, 70), (right_xcor, 85), (right_xcor, 100), ]



class Flippers:

    def __init__(self):
        self.lt_main_paddle = []
        self.rt_main_paddle = []
        self.screen = turtle.Screen()
        self.make_paddles()


    def make_paddles(self):
        self.screen.tracer(0)
        for part in range(7):
            make_new_part = turtle.Turtle('square')
            make_new_part.shapesize(stretch_wid=.7)
            make_new_part.penup()
            make_new_part.color('red')
            make_new_part.goto(lt_pad_starting_pt[part])
            self.lt_main_paddle.append(make_new_part)


        for part in range(7):
            make_new_part = turtle.Turtle('square')
            make_new_part.shapesize(stretch_wid=.7)
            make_new_part.penup()
            make_new_part.color('red')
            make_new_part.goto(rt_pad_starting_pt[part])
            self.rt_main_paddle.append(make_new_part)

        self.lt_main_paddle[3].hideturtle()
        self.rt_main_paddle[3].hideturtle()
        self.screen.update()

    def launch_lt_flickers(self):
        self.lt_main_paddle[3].hideturtle()
        x_cor = self.lt_main_paddle[6].xcor()
        y_cor = self.lt_main_paddle[6].ycor()
        for parts in range(6, 3, -1):
            self.lt_main_paddle[parts].shapesize()
            self.lt_main_paddle[parts].goto(x_cor + (abs(parts - 6)) * 11, y_cor - (abs(parts - 6) * 10))
        x_cor = self.lt_main_paddle[0].xcor()
        y_cor = self.lt_main_paddle[0].ycor()
        for parts in range(3):
            self.lt_main_paddle[parts].shapesize()
            self.lt_main_paddle[parts].goto(x_cor + (parts * 11), y_cor + (parts * 10))
        self.screen.update()
        self.default_lt_flicker_pos()

    def default_lt_flicker_pos(self):
        time.sleep(.2)
        self.screen.tracer(0)
        x_cor = self.lt_main_paddle[0].xcor()
        y_cor = self.lt_main_paddle[0].ycor()
        for parts in range(7):
            self.lt_main_paddle[parts].goto(x_cor, y_cor + (parts * 15))
        self.lt_main_paddle[3].hideturtle()
        self.screen.update()

    def show_lt_flickers(self):
        self.screen.tracer(0)
        self.lt_main_paddle[3].hideturtle()
        x_cor = self.lt_main_paddle[6].xcor()
        y_cor = self.lt_main_paddle[6].ycor()
        for parts in range(6, 3, -1):
            self.lt_main_paddle[parts].goto(x_cor - (abs(parts - 6)) * 11, y_cor - (abs(parts - 6) * 10))
        x_cor = self.lt_main_paddle[0].xcor()
        y_cor = self.lt_main_paddle[0].ycor()
        for parts in range(3):
            self.lt_main_paddle[parts].goto(x_cor - (parts * 11), y_cor + (parts * 10))
        self.screen.update()

    def lt_move_up(self):
        self.screen.tracer(0)
        if self.lt_main_paddle[-1].ycor() <= 165:
            for parts in range(7):
                x_cor = self.lt_main_paddle[parts].xcor()
                y_cor = self.lt_main_paddle[parts].ycor()
                self.lt_main_paddle[parts].goto(x_cor, y_cor + 30)
            self.screen.update()

    def lt_move_down(self):
        self.screen.tracer(0)
        if self.lt_main_paddle[0].ycor() >= -160:
            for parts in range(7):
                x_cor = self.lt_main_paddle[parts].xcor()
                y_cor = self.lt_main_paddle[parts].ycor()
                self.lt_main_paddle[parts].goto(x_cor, y_cor - 30)
            self.screen.update()

    def launch_rt_flickers(self):
        self.rt_main_paddle[3].hideturtle()
        x_cor = self.rt_main_paddle[6].xcor()
        y_cor = self.rt_main_paddle[6].ycor()
        for parts in range(6, 3, -1):
            self.rt_main_paddle[parts].goto(x_cor - (abs(parts - 6)) * 11, y_cor - (abs(parts - 6) * 10))
        x_cor = self.rt_main_paddle[0].xcor()
        y_cor = self.rt_main_paddle[0].ycor()
        for parts in range(3):
            self.rt_main_paddle[parts].goto(x_cor - (parts * 11), y_cor + (parts * 10))
        self.screen.update()
        self.default_rt_flicker_pos()

    def default_rt_flicker_pos(self):
        time.sleep(.2)
        self.screen.tracer(0)
        x_cor = self.rt_main_paddle[0].xcor()
        y_cor = self.rt_main_paddle[0].ycor()
        for parts in range(7):
            self.rt_main_paddle[parts].goto(x_cor, y_cor + (parts * 15))
        self.rt_main_paddle[3].hideturtle()
        self.screen.update()

    def show_rt_flickers(self):
        self.screen.tracer(0)
        self.rt_main_paddle[3].hideturtle()
        x_cor = self.rt_main_paddle[6].xcor()
        y_cor = self.rt_main_paddle[6].ycor()
        for parts in range(6, 3, -1):
            self.rt_main_paddle[parts].goto(x_cor + (abs(parts - 6)) * 11, y_cor - (abs(parts - 6) * 10))
        x_cor = self.rt_main_paddle[0].xcor()
        y_cor = self.rt_main_paddle[0].ycor()
        for parts in range(3):
            self.rt_main_paddle[parts].goto(x_cor + (parts * 11), y_cor + (parts * 10))
        self.screen.update()

    def rt_move_up(self):
        self.screen.tracer(0)
        if self.rt_main_paddle[-1].ycor() <= 165:
            for parts in range(7):
                x_cor = self.rt_main_paddle[parts].xcor()
                y_cor = self.rt_main_paddle[parts].ycor()
                self.rt_main_paddle[parts].goto(x_cor, y_cor + 30)
            self.screen.update()

    def rt_move_down(self):
        self.screen.tracer(0)
        if self.rt_main_paddle[0].ycor() >= -160:
            for parts in range(7):
                x_cor = self.rt_main_paddle[parts].xcor()
                y_cor = self.rt_main_paddle[parts].ycor()
                self.rt_main_paddle[parts].goto(x_cor, y_cor - 30)
            self.screen.update()


# class Paddle:
#
    # def __init__(self):
    #     self.rt_pad_parts = []
    #     self.lt_pad_parts = []
    #     self.right_paddle()
    #     self.left_paddle()
    #
    # def right_paddle(self):
    #     for parts in range(8):
    #         paddle_part = Turtle('square')
    #         paddle_part.penup()
    #         paddle_part.color('red')
    #         paddle_part.shapesize(stretch_wid=.5)
    #         paddle_part.goto(x=455, y=parts * 10)
    #         self.rt_pad_parts.append(paddle_part)
    #
    # def left_paddle(self):
    #     for parts in range(8):
    #         paddle_part = Turtle('square')
    #         paddle_part.penup()
    #         paddle_part.color('red')
    #         paddle_part.shapesize(stretch_wid=.5)
    #         paddle_part.goto(x=-455, y=parts * 10)
    #         self.lt_pad_parts.append(paddle_part)
    #
    # def rt_move_up(self):
    #     if self.rt_pad_parts[-1].ycor() <= 175:
    #         for parts in range(len(self.rt_pad_parts) - 1, -1, -1):
    #             self.rt_pad_parts[parts].setheading(90)
    #             self.rt_pad_parts[parts].forward(33)
    #
    # def rt_move_down(self):
    #     if self.rt_pad_parts[0].ycor() >= -170:
    #         for parts in range(0, len(self.rt_pad_parts)):
    #             self.rt_pad_parts[parts].setheading(270)
    #             self.rt_pad_parts[parts].forward(33)
    #
    # def lt_move_up(self):
    #     if self.lt_pad_parts[-1].ycor() <= 175:
    #         for parts in range(len(self.lt_pad_parts) - 1, -1, -1):
    #             self.lt_pad_parts[parts].setheading(90)
    #             self.lt_pad_parts[parts].forward(33)
    #
    # def lt_move_down(self):
    #     if self.lt_pad_parts[0].ycor() >= -170:
    #         for parts in range(0, len(self.lt_pad_parts)):
    #             self.lt_pad_parts[parts].setheading(270)
    #             self.lt_pad_parts[parts].forward(33)

