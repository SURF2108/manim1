#method - fn when related to a class
from manim import *

class DrawCircle(Scene):
    def construct(self):
        circle=Circle(radius=1,color=BLUE)
        circle.set_fill(RED,opacity=0.5)
        self.play(Create(circle),run_time=5)
        self.play(FadeOut(circle),run_time=1,rate_func=smooth)

        circle2=Circle()
        circle2.set_fill(RED,opacity=0.5)

        square=Square()
        self.play(Create(square), run_time=5,rate_func=smooth)
        square.animate.rotate(-0.4)
        #self.play(square.animate.shift(RIGHT*5),run_time=1)
        #self.play(Transform(square,circle2),run_time=1)
        self.play(square.animate.shift(RIGHT*5),Transform(square,circle2),run_time=5)
        self.play(FadeOut(square),run_time=2,rate_func=smooth)       
