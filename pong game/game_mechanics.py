from turtle import Screen
from paddles import Paddle
from pong import Pongball
from walls import Wall
from scoreboard import Scorer
import random

# screen = Screen()
# paddles = Paddle()
# pong_ball = Pongball()
# wall_spawns = Wall()
# scorer = Scorer()

# screen.setup(width=1000, height=400, startx=150, starty=100)
# screen.bgcolor('black')
# screen.title('Pong')
# screen.tracer(0)


class Mechanics:

    def __init__(self):
        pass


    def out_of_bounds(self, pong_ball):
        if pong_ball >= 490:
            return True
        if pong_ball <= -490:
            return True
        else:
            return




    # def ball_hit(self):
    #     for parts in paddles.rt_pad_parts:
    #         if pong_ball.distance(parts) < 15:
    #             pong_ball.goto(pong_ball.xcor() - 15, pong_ball.ycor())
    #             pong_ball.paddle_bounce()
    #     for parts in paddles.lt_pad_parts:
    #         if pong_ball.distance(parts) < 15:
    #             pong_ball.goto(pong_ball.xcor() + 15, pong_ball.ycor())
    #             pong_ball.paddle_bounce()
    #
    # def small_wall_hit(self):
    #     for parts in wall_spawns.rt_walls:
    #         if pong_ball.distance(parts) < 20:
    #             if wall_spawns.rt_walls[0].color()[0] == "Gold":
    #                 wall_coord = pong_ball.xcor(), pong_ball.ycor()
    #                 screen.tracer(0)
    #                 pong_ball.teleport(wall_coord)
    #                 screen.update()
    #             elif wall_spawns.rt_walls[0].color()[0] == "Aquamarine":
    #                 pong_ball.paddle_bounce()
    #                 wall_spawns.rt_connect()
    #             elif wall_spawns.rt_walls[0].color()[0] == "Green":
    #                 pong_ball.paddle_bounce()
    #                 wall_spawns.lt_connect()
    #     for parts in wall_spawns.lt_walls:
    #         if pong_ball.distance(parts) < 20:
    #             if wall_spawns.lt_walls[0].color()[0] == "Gold":
    #                 wall_coord = pong_ball.xcor(), pong_ball.ycor()
    #                 screen.tracer(0)
    #                 pong_ball.teleport(wall_coord)
    #                 screen.update()
    #             elif wall_spawns.lt_walls[0].color()[0] == "Aquamarine":
    #                 pong_ball.paddle_bounce()
    #                 wall_spawns.lt_connect()
    #             elif wall_spawns.lt_walls[0].color()[0] == "Green":
    #                 pong_ball.paddle_bounce()
    #                 wall_spawns.rt_connect()

    # def check_everything(self):
    #     self.out_of_bounds()


    # if scorer.lt_score >= 1 or scorer.rt_score >= 1:
    #     scorer.declare_winner()
