import turtle
from turtle import Turtle , Screen

class Prush():
    def __init__(self,prush=Turtle(visible=False), turtle_size=20, screen=Screen() ):
        self.prush = prush
        self.TURTLE_SIZE = turtle_size
        self.screen = screen

    def starting_position(self):
        self.prush.penup()
        self.prush.goto(self.TURTLE_SIZE / 2 - self.screen.window_width() / 2, self.screen.window_height() / 2 - self.TURTLE_SIZE / 2)
        self.prush.pendown()
        self.prush.showturtle()

