from turtle import Screen
from paddles import Paddle
from pong import Pongball
from walls import Wall
from scoreboard import Scorer
import random


screen = Screen()
screen.setup(width=1000, height=400, startx=150, starty=100)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddles = Paddle()
pong_ball = Pongball()
wall_spawns = Wall()
scorer = Scorer()
screen.tracer(1)
pong_ball.start_game()
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=paddles.rt_move_up)
screen.onkey(key="Down", fun=paddles.rt_move_down)
screen.onkey(key="w", fun=paddles.lt_move_up)
screen.onkey(key="s", fun=paddles.lt_move_down)


game_playing = True
while game_playing:
    pong_ball.movement()

    if pong_ball.xcor() >= 490:
        scorer.lt_score += 1
        scorer.add_score()
        screen.tracer(1)
        pong_ball.reset_start()
        screen.tracer(0)
    if pong_ball.xcor() <= -490:
        scorer.rt_score += 1
        scorer.add_score()
        screen.tracer(1)
        pong_ball.reset_start()
        screen.tracer(0)

    for parts in paddles.rt_pad_parts:
        if pong_ball.distance(parts) < 15:
            pong_ball.goto(pong_ball.xcor() - 15, pong_ball.ycor())
            pong_ball.paddle_bounce()
    for parts in paddles.lt_pad_parts:
        if pong_ball.distance(parts) < 15:
            pong_ball.goto(pong_ball.xcor() + 15, pong_ball.ycor())
            pong_ball.paddle_bounce()

    for parts in wall_spawns.rt_walls:
        if pong_ball.distance(parts) < 20:
            if wall_spawns.rt_walls[0].color()[0] == "Gold":
                wall_coord = pong_ball.xcor(), pong_ball.ycor()
                screen.tracer(0)
                pong_ball.teleport(wall_coord)
                screen.update()
            elif wall_spawns.rt_walls[0].color()[0] == "Aquamarine":
                pong_ball.paddle_bounce()
                wall_spawns.rt_connect()
            elif wall_spawns.rt_walls[0].color()[0] == "Green":
                pong_ball.paddle_bounce()
                wall_spawns.lt_connect()
    for parts in wall_spawns.lt_walls:
        if pong_ball.distance(parts) < 20:
            if wall_spawns.lt_walls[0].color()[0] == "Gold":
                wall_coord = pong_ball.xcor(), pong_ball.ycor()
                screen.tracer(0)
                pong_ball.teleport(wall_coord)
                screen.update()
            elif wall_spawns.lt_walls[0].color()[0] == "Aquamarine":
                pong_ball.paddle_bounce()
                wall_spawns.lt_connect()
            elif wall_spawns.lt_walls[0].color()[0] == "Green":
                pong_ball.paddle_bounce()
                wall_spawns.rt_connect()

    rand = random.randint(0, 750)
    if rand == 20:
        wall_spawns.lt_connect()
        wall_spawns.rt_connect()

    if scorer.lt_score >= 5 or scorer.rt_score >= 5:
        scorer.declare_winner()
        game_playing = False

    screen.update()

screen.exitonclick()
