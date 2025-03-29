from manim import *
'''
class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
'''

class DrawCircle(Scene):
    def construct(self): #this is a special method; anything with construct will be a constructor
        gola = Circle(2)
        gola.set_color(BLUE)
        gola.set_fill(RED, opacity = .1)
        self.play(
            Create(gola),
            run_time = 5
            )          
 