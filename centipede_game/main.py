import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600, startx=300, starty=30)
screen.bgcolor('black')
screen.title('~Centipede~')
screen.tracer(0)

snake = Snake()
food = Food()

try:
    with open("data.txt", "x") as f:
        f.write("0")
except FileExistsError:
    pass

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='d', fun=snake.right)

keep_moving = True
while keep_moving:
    time.sleep(0.1)
    screen.update()
    snake.snake_movement()

    if snake.head.distance(food) < 20:
        food.create_more_food()
        scoreboard.add_score()
        snake.extend()

    if 300 < abs(snake.head.xcor()) or 300 < abs(snake.head.ycor()):
        snake.game_over()
        scoreboard.game_over()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 15:
            snake.game_over()
            scoreboard.game_over()


screen.exitonclick()
