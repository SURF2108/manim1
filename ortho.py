from manim import *

class OT(Scene):
	config.pixel_height = 1080
	config.pixel_width = 1920
	config.frame_height = 18.0
	config.frame_width = 32.0

	def construct(self):
		
		self.slide1()
		hsize = config.frame_height
		lsize = config.frame_width
		grid = NumberPlane(
			x_range=[-lsize/2,lsize/2,1],
			y_range=[-hsize/2,hsize/2,1],
			background_line_style={
			"stroke_color" : BLUE,
			"stroke_width" : 1,
			"stroke_opacity" : 0.7
			},
			axis_config={
			"include_numbers" : True,
			"font_size" : 36
			}
		)
		self.add(grid)


    def slide1(self):
    	circle1 = Circle(radius =2, color=YELLOW_A)
    	circle1.move_to(ORIGIN)

    	self.play(Create(circle1))
