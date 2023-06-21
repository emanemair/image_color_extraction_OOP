import turtle

from prepareprush import Prush
from turtle import Turtle , Screen

class Display(Prush):
    def __init__(self ,colors ,prush=Turtle(visible=False), turtle_size=20, screen=Screen() ):
         Prush.__init__(self ,prush, turtle_size, screen )
         self.colors=colors
    def start_drawing(self):
        turtle.colormode(255)
        for color in range(0, len(self.colors)):
            self.prush.color(self.colors[color])
            self.prush.fillcolor(self.colors[color])
            self.prush.begin_fill()
            for _ in range(4):
                self.prush.forward(40)
                self.prush.right(360 / 4)
            self.prush.end_fill()
            self.prush.forward(40)
    def draw(self):
        self.starting_position()
        self.start_drawing()
        self.screen.exitonclick()





