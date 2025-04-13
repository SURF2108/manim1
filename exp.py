from manim import *

class TraceExponential(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[0, 8, 2],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": True}
        )

        # Create the e^x graph
        graph = axes.plot(lambda x: np.exp(x), color=BLUE)

        # Label it
        label = axes.get_graph_label(graph, label="e^x")

        # Create a moving dot
        moving_dot = Dot(color=RED).move_to(axes.c2p(-2, np.exp(-2)))
        moving_line = Line([-3,0,0],[-1,0,0],color = RED).move_to(axes.c2p(-2,np.exp(-2)))
        alpha = ValueTracker(0)

        # Add everything to the scene
        self.play(Create(axes), Create(graph), Write(label))
        self.play(FadeIn(moving_dot),FadeIn(moving_line))

        

        # Animate the dot along the graph
        self.play(
            MoveAlongPath(moving_dot, graph, rate_func=linear, run_time=4),
            MoveAlongPath(moving_line, graph, rate_func=linear, run_time=4)

        )

        self.wait(1)
