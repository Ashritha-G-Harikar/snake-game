from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.new_food()

    def new_food(self):
        new_x = random.randint(-260, 260)
        new_y = random.randint(-260, 260)
        self.goto(new_x, new_y)
