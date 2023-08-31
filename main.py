from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
score = ScoreBoard()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.right, key="Right")
screen.onkey(snake.left, key="Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.my_score()
        score.screen.update()
        food.refresh()
        snake.extend()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.game_over()
        game_is_on= False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
