'''
from manim import *

class ShiftAndTransform(Scene):
    def construct(self):
        # Create a red square
        square = Square(color=RED)
        square.move_to(LEFT * 3)

        # Create a blue circle at a different position
        circle = Circle(color=BLUE)

        # Animate transformation with shifting
        self.play(Transform(square, circle.shift(RIGHT * 3)))

        # Hold the final frame
        self.wait()
'''

