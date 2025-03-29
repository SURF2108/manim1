from manim import *

class transformtext(Scene):
	def construct(self):
		circle=Circle()
		text=Text("Hello World",font_size=72)
		text.to_edge(UP)
		self.play(Write(text,run_time=2))
		self.play(Transform(text["H"],circle), run_time=10,rate_func=linear)
		