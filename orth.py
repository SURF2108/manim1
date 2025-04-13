#to find the orthogonal trajectories using differentiation

from manim import *

class OT(Scene):
	def construct(self):

		#Grid
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

		# slides:
		self.orth()


	def orth(self):
		circle1=Circle(radius=1.8,color=BLUE)
			
		circle1.move_to(ORIGIN)
		self.play(Create(circle1),run_time=2)
			
		l= [[2,0,0],[2,2,0],[0,2,0],[-2,2,0],[-2,0,0],[-2,-2,0],[0,-2,0],[2,-2,0]]

		angle = 0
		point = circle1.point_at_angle(angle)
		tangent_dir = rotate_vector(RIGHT, angle)
		tangent = Line(point - tangent_dir, point + tangent_dir, color=YELLOW)
		self.add(tangent)
			
		num_steps = 8
		step_angle = PI / 4

		for i in range(1, num_steps + 1):
			start_angle = (i - 1) * step_angle
			end_angle = i * step_angle

			def update_func(mob, alpha):
				current_angle = interpolate(start_angle, end_angle, alpha)
				new_point = circle1.point_at_angle(current_angle)
				new_dir = rotate_vector(RIGHT, current_angle)
				mob.become(Line(new_point - new_dir, new_point + new_dir, color=YELLOW))
				b = Line(ORIGIN,l[i-1],color = YELLOW)
				self.play(Create(b))
			self.play(UpdateFromAlphaFunc(tangent, update_func), run_time=1.2)
			self.wait(0.5)

	'''		for i in range(len(l)) :
				a = Line(ORIGIN,[2,0,0],color=YELLOW)
				self.play(a.animate.rotate_about_origin((PI/4)*(i+1)))
				b = Line(ORIGIN,l[i],color = YELLOW)
				self.play(Create(b))
		'''