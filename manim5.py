from manim import *


class ax(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            axis_config={"color": RED}
        )
        curve=axes.plot(lambda y:3,color=WHITE)
        self.play(Create(axes),run_time=5)
        self.play(Create(curve),run_time=5)
        


