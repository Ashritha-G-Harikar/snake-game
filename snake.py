from turtle import Turtle
no_of_times = [3, 1]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = []
        self.x_cor = 0
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):

        for _ in range(no_of_times[0]):
            tom = Turtle(shape='square')
            tom.color('white')
            tom.turtlesize(0.95, 0.95)
            tom.penup()
            tom.speed("fastest")
            tom.goto(self.x_cor, 0)
            self.x_cor -= 10
            self.turtles.append(tom)
            if no_of_times[0] == 3:
                no_of_times.remove(3)

    def move(self):
        for number in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[number - 1].xcor()
            new_y = self.turtles[number - 1].ycor()
            self.turtles[number].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

