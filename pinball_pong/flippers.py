import turtle
import time



left_xcor = -455
lt_pad_starting_pt = [(left_xcor, 10), (left_xcor, 25), (left_xcor, 40),
                      (left_xcor, 55), (left_xcor, 70), (left_xcor, 85), (left_xcor, 100), ]

screen = turtle.Screen()
screen.setup(width=1000, height=400, startx=550, starty=50)


class Flippers:

    def __init__(self):

        self.lt_main_paddle = []
        self.lt_top_flicker_windup = []
        self.lt_bot_flicker_windup = []
        self.lt_top_flicker_launch = []
        self.lt_bot_flicker_launch = []
        self.make_paddles()


    def make_paddles(self):
        # main leftside paddle #
        for part in range(7):
            make_new_part = turtle.Turtle('square')
            make_new_part.shapesize(stretch_wid=.7)
            make_new_part.penup()
            make_new_part.color('red')
            make_new_part.goto(lt_pad_starting_pt[part])
            if part == 3:
                make_new_part.hideturtle()
            self.lt_main_paddle.append(make_new_part)

        # Paddle creation for left flicker wind-up motion #
        x_cor = self.lt_main_paddle[6].xcor()
        y_cor = self.lt_main_paddle[6].ycor()
        for parts in range(4):
            make_new_part = turtle.Turtle('square')
            make_new_part.shapesize(stretch_wid=.5)
            make_new_part.penup()
            make_new_part.color('red')
            make_new_part.hideturtle()
            make_new_part.goto(x_cor - (parts * 7), y_cor - (parts * 10))
            self.lt_top_flicker_windup.append(make_new_part)
        x_cor = self.lt_main_paddle[0].xcor()
        y_cor = self.lt_main_paddle[0].ycor()
        for parts in range(4):
            make_new_part = turtle.Turtle('square')
            make_new_part.shapesize(stretch_wid=.5)
            make_new_part.penup()
            make_new_part.color('red')
            make_new_part.hideturtle()
            make_new_part.goto(x_cor + (parts * 7), y_cor + (parts * 10))
            self.lt_bot_flicker_windup.append(make_new_part)

        # Paddle creation for left flicker launch motion #
        x_cor = self.lt_main_paddle[6].xcor()
        y_cor = self.lt_main_paddle[6].ycor()
        for parts in range(4):
            make_new_part = turtle.Turtle('square')
            make_new_part.shapesize(stretch_wid=.5)
            make_new_part.penup()
            make_new_part.color('red')
            make_new_part.hideturtle()
            make_new_part.goto(x_cor + (parts * 7), y_cor - (parts * 10))
            self.lt_top_flicker_launch.append(make_new_part)
        x_cor = self.lt_main_paddle[0].xcor()
        y_cor = self.lt_main_paddle[0].ycor()
        for parts in range(4):
            make_new_part = turtle.Turtle('square')
            make_new_part.shapesize(stretch_wid=.5)
            make_new_part.penup()
            make_new_part.color('red')
            make_new_part.hideturtle()
            make_new_part.goto(x_cor + (parts * 7), y_cor + (parts * 10))
            self.lt_bot_flicker_launch.append(make_new_part)


    def default_flicker_pos(self):
        time.sleep(.3)
        screen.tracer(0)
        for parts in range(4):
            self.lt_top_flicker_launch[parts].hideturtle()
        for parts in range(4):
            self.lt_bot_flicker_launch[parts].hideturtle()
        for parts in range(6):
            self.lt_main_paddle[parts].showturtle()
        self.lt_main_paddle[3].hideturtle()
        screen.update()


    def launch_flickers(self):
        screen.tracer(0)
        for parts in range(4):
            self.lt_top_flicker_windup[parts].hideturtle()
            self.lt_bot_flicker_windup[parts].hideturtle()
        x_cor = self.lt_main_paddle[6].xcor()
        y_cor = self.lt_main_paddle[6].ycor()
        for parts in range(4):
            self.lt_top_flicker_launch[parts].goto(x_cor + (parts * 7), y_cor - (parts * 10))
            self.lt_top_flicker_launch[parts].showturtle()
        x_cor = self.lt_main_paddle[0].xcor()
        y_cor = self.lt_main_paddle[0].ycor()
        for parts in range(4):
            self.lt_bot_flicker_launch[parts].goto(x_cor + (parts * 7), y_cor + (parts * 10))
            self.lt_bot_flicker_launch[parts].showturtle()
        screen.update()
        self.default_flicker_pos()


    def show_flickers(self):
        screen.tracer(0)
        x_cor = self.lt_main_paddle[6].xcor()
        y_cor = self.lt_main_paddle[6].ycor()
        for parts in range(4):
            self.lt_top_flicker_windup[parts].goto(x_cor - (parts * 7), y_cor - (parts * 10))
            self.lt_top_flicker_windup[parts].showturtle()
        x_cor = self.lt_main_paddle[0].xcor()
        y_cor = self.lt_main_paddle[0].ycor()
        for parts in range(4):
            self.lt_bot_flicker_windup[parts].goto(x_cor - (parts * 7), y_cor + (parts * 10))
            self.lt_bot_flicker_windup[parts].showturtle()
        screen.update()


    def flicker_press(self):
        screen.tracer(0)
        for parts in range(6):
            self.lt_main_paddle[parts].hideturtle()
        self.show_flickers()


    def move_up(self):
        screen.tracer(0)
        for parts in range(7):
            x_cor = self.lt_main_paddle[parts].xcor()
            y_cor = self.lt_main_paddle[parts].ycor()
            self.lt_main_paddle[parts].goto(x_cor, y_cor + 30)
        screen.update()


    def move_down(self):
        screen.tracer(0)
        for parts in range(7):
            x_cor = self.lt_main_paddle[parts].xcor()
            y_cor = self.lt_main_paddle[parts].ycor()
            self.lt_main_paddle[parts].goto(x_cor, y_cor - 30)
        screen.update()


screen.tracer(0)
flippers = Flippers()
screen.update()

screen.listen()
screen.onkeypress(key='w', fun=flippers.move_up)
screen.onkeypress(key='s', fun=flippers.move_down)

screen.onkeypress(key='space', fun=flippers.flicker_press)
screen.onkeyrelease(key='space', fun=flippers.launch_flickers)


screen.exitonclick()
