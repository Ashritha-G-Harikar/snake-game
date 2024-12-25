from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
y = 0

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    # get the snake to move
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.scoreboard()
    # Detect collisions
    if snake.head.distance(food) < 20:
        food.new_food()
        score.score += 1
        score.scoreboard()
        snake.create_snake()

    # Detect collisions with the wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    # Detect collisions with its own head
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 15:
            game_on = False
            score.game_over()


screen.exitonclick()
