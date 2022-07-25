from turtle import Turtle, Screen
import random


COLORS = ['Aquamarine', 'Gold', 'Green', ]


class Wall:
    def __init__(self):
        self.rt_walls = []
        self.lt_walls = []
        self.random_walls = [[-325, -140], [-325, 150], [-50, 150], [50, -150], [25, 150], [325, -150], ]
        self.screen = Screen()
        self.make_rt_wall()
        self.make_lt_wall()

    def make_rt_wall(self):
        wall_color = random.choice(COLORS)
        spawn_point = self.random_walls[random.choice(range(0, 6))]
        for part in range(4):
            rt_wall = Turtle('square')
            rt_wall.penup()
            rt_wall.color(wall_color)
            rt_wall.shapesize(stretch_wid=.5)
            rt_wall.goto(x=spawn_point[0], y=spawn_point[1] + (part * 10))
            self.rt_walls.append(rt_wall)

    def make_lt_wall(self):
        wall_color = random.choice(COLORS)
        spawn_point = self.random_walls[random.choice(range(0, 6))]
        for part in range(4):
            lt_wall = Turtle('square')
            lt_wall.penup()
            lt_wall.color(wall_color)
            lt_wall.shapesize(stretch_wid=.5)
            lt_wall.goto(x=spawn_point[0], y=spawn_point[1] + (part * 10))
            self.lt_walls.append(lt_wall)

    def rt_connect(self):
        wall_color = random.choice(COLORS)
        spawn_point = self.random_walls[random.choice(range(0, 6))]
        for parts in range(0, 4):
            self.rt_walls[parts].color(wall_color)
            self.rt_walls[parts].goto(x=spawn_point[0], y=spawn_point[1] + (parts * 10))

    def lt_connect(self):
        wall_color = random.choice(COLORS)
        spawn_point = self.random_walls[random.choice(range(0, 6))]
        for parts in range(0, 4):
            self.lt_walls[parts].color(wall_color)
            self.lt_walls[parts].goto(x=spawn_point[0], y=spawn_point[1] + (parts * 10))
