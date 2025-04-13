from manim import *

class Screen(Scene):
	config.pixel_height = 1080
	config.pixel_width = 1920
	config.frame_height = 18.0
	config.frame_width = 32.0

	def construct(self):
		self.slide1()


	def slide1(self):

		c = Circle(radius = 2,color = WHITE)
		c.move_to(ORIGIN)

		self.play(Create(c),run_time = 4)

		ref = Line([2,0,0],ORIGIN,color = BLUE)
		self.add(ref)

		for i in range(4):
			ref.animate.rotate_about_origin((PI/2)*(i+1))
			l = Line(ORIGIN,ref.get_end(),color = BLUE)

			self.play(Create(l))