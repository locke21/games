from turtle import Screen
from paddles import Flippers
from pong import Pongball
from walls import Wall
from scoreboard import Scorer
import random


screen = Screen()
screen.setup(width=1000, height=400, startx=150, starty=100)
screen.bgcolor('black')
screen.title('Pong')

screen.tracer(0)
pong_ball = Pongball()
flippers = Flippers()
wall_spawns = Wall()
scorer = Scorer()
screen.tracer(1)
pong_ball.start_game()
screen.tracer(0)

screen.listen()
screen.onkeypress(key='w', fun=flippers.lt_move_up)
screen.onkeypress(key='s', fun=flippers.lt_move_down)
screen.onkeypress(key='d', fun=flippers.show_lt_flickers)
screen.onkeyrelease(key='d', fun=flippers.launch_lt_flickers)

screen.onkeypress(key='Up', fun=flippers.rt_move_up)
screen.onkeypress(key='Down', fun=flippers.rt_move_down)
screen.onkeypress(key='Left', fun=flippers.show_rt_flickers)
screen.onkeyrelease(key='Left', fun=flippers.launch_rt_flickers)


game_playing = True
while game_playing:

    pong_ball.movement()

    # Checks for out of bounds and score #
    if pong_ball.xcor() >= 490:
        scorer.lt_score += 1
        scorer.add_score()
        if scorer.lt_score >= 5 or scorer.rt_score >= 5:
            scorer.declare_winner()
            game_playing = False
        screen.tracer(1)
        pong_ball.reset_start()
        screen.tracer(0)
    if pong_ball.xcor() <= -490:
        scorer.rt_score += 1
        scorer.add_score()
        if scorer.lt_score >= 5 or scorer.rt_score >= 5:
            scorer.declare_winner()
            game_playing = False
        screen.tracer(1)
        pong_ball.reset_start()
        screen.tracer(0)

    # Checks for paddle hits #
    for parts in flippers.rt_main_paddle:
        if pong_ball.distance(parts) < 15:
            if parts.xcor() < 445:
                pong_ball.flipper_hit()
            screen.tracer(0)
            pong_ball.goto(pong_ball.xcor() - 25, pong_ball.ycor())
            screen.update()
            pong_ball.paddle_bounce()
    for parts in flippers.lt_main_paddle:
        if pong_ball.distance(parts) < 15:
            if parts.xcor() > -430:
                pong_ball.flipper_hit()
            screen.tracer(0)
            pong_ball.goto(pong_ball.xcor() + 25, pong_ball.ycor())
            screen.update()
            pong_ball.paddle_bounce()

    # Random walls detection #
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

    # Changes wall spawns #
    rand = random.randint(0, 750)
    if rand == 20:
        wall_spawns.lt_connect()
        wall_spawns.rt_connect()

    screen.update()

screen.exitonclick()
