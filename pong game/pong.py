from turtle import Turtle
import random


class Pongball(Turtle):
    def __init__(self):
        super(Pongball, self).__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.x_move = .6
        self.y_move = .6
        self.random_starts = [3, 5, 7, -3, -5, -7, ]

    def start_game(self):
        starting_trajectory = {360: 0, 180: 0}
        for steps in range(1, 6):
            rand_circle = random.choice([360, 180])
            starting_trajectory[rand_circle] += 1
            self.circle(random.choice(self.random_starts) * steps, rand_circle)
        if starting_trajectory[180] % 2 != 0:
            self.x_move *= -1
        if random.randint(0, 1) == 0:
            self.y_move *= -1

    def reset_start(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.check_speed()
        self.start_game()

    def check_speed(self):
        if -2.5 < self.x_move > 2.5:
            self.x_move = 1 if self.x_move > 0 else -1
        elif -1.8 < self.x_move > 1.8:
            self.x_move = self.x_move - .2 if self.x_move > 0 else + .2
        if -2.5 < self.y_move > 2.5:
            self.y_move = 1 if self.y_move > 0 else -1
        elif -1.8 < self.y_move > 1.8:
            self.y_move = self.y_move - .2 if self.y_move > 0 else + .2
        return

    def movement(self):
        self.check_speed()
        self.wall_bounce()
        move_x = self.xcor() + self.x_move
        move_y = self.ycor() + self.y_move
        self.goto(move_x, move_y)

    def wall_bounce(self):
        if self.ycor() >= 190 or self.ycor() <= -190:
            self.check_speed()
            self.y_move *= -1.15
        return

    def paddle_bounce(self):
        self.check_speed()
        self.x_move *= -1.15

    def teleport(self, wall_coord):
        self.goto(wall_coord[0] * -1, wall_coord[1])
        self.x_move *= -1
