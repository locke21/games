from turtle import Turtle
import time

FONT1 = ('ariel', 12, 'bold')
FONT2 = ('courier', 24, 'normal')
COLOR = ['grey', 'purple', 'red']


class Scorer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(COLOR[0])
        self.rt_score = 0
        self.lt_score = 0
        self.set_scoreboard()

    def update_score(self):
        self.goto(-408, 174)
        self.color(COLOR[2])
        self.write(f'{self.lt_score}', font=FONT1)
        self.color(COLOR[2])
        self.goto(472, 174)
        self.write(f'{self.rt_score}', font=FONT1)

    def set_scoreboard(self):
        self.clear()
        self.color(COLOR[0])
        self.goto(-485, 175)
        self.write(f'P1 Score: ', font=FONT1)
        self.goto(395, 175)
        self.write(f'P2 Score: ', font=FONT1)
        self.update_score()

    def add_score(self):
        self.goto(-25, 0)
        self.write('Score!!', font=FONT2)
        time.sleep(.7)
        self.set_scoreboard()

    def declare_winner(self):
        self.add_score()
        self.color(COLOR[1])
        self.goto(-65, 0)
        self.write('Game over!', font=FONT2)
