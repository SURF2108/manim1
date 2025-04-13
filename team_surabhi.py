from manim import *
from manim.gui.gui import configure_pygui

class SAS_rule(Scene):

					

	def construct(self):

		# Grid for reference
		'''
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
		'''
		# Objects:

		statements = {
			"Heading" : Text("Problem Statement:",font_size=50).move_to([-12,8,0]),
			"Problem_statement" : Text("To prove that the two given triangles are Congruent using the SAS Congruency Rule.",font_size=45).move_to([-1.5,7,0])

		}

		self.play(Write(statements["Heading"]))
		self.play(Write(statements["Problem_statement"]))

		# triangle 1

		tri_abc_data = {
			"Coordinates" : [[-14,-1,0],[-14,-7,0],[-6,-7,0]],
			"Labels" : [Text("A"),Text("B"),Text("C")],
		}

		Angle1 = RightAngle(
				Line(tri_abc_data["Coordinates"][1],tri_abc_data["Coordinates"][2]),
				Line(tri_abc_data["Coordinates"][0],tri_abc_data["Coordinates"][1]),
				length=0.5,
				quadrant=(1,-1)
			)

		tri_abc = Polygon(
			tri_abc_data["Coordinates"][0],
			tri_abc_data["Coordinates"][1],
			tri_abc_data["Coordinates"][2],
			color=BLUE
		)

		tri_abc_labels = VGroup(
			tri_abc_data["Labels"][0].next_to(tri_abc_data["Coordinates"][0] + UP*0.5 + LEFT),
			tri_abc_data["Labels"][1].next_to(tri_abc_data["Coordinates"][1] + DOWN*0.5 + LEFT),
			tri_abc_data["Labels"][2].next_to(tri_abc_data["Coordinates"][2] + DOWN*0.5),
		)

		self.play(Create(tri_abc))
		self.play(Create(Angle1))
		self.play(Write(tri_abc_labels))

		# triangle 2

		tri_def_data = {
			"Coordinates" : [[-11,3,0],[-3,3,0],[-3,-3,0]],
			"Labels" : [Text("D"),Text("E"),Text("F")],
		}

		Angle2 = RightAngle(
				Line(tri_def_data["Coordinates"][1],tri_def_data["Coordinates"][2]),
				Line(tri_def_data["Coordinates"][0],tri_def_data["Coordinates"][1]),
				length=0.5,
				quadrant=(1,-1)
			)

		tri_def = Polygon(
			tri_def_data["Coordinates"][0],
			tri_def_data["Coordinates"][1],
			tri_def_data["Coordinates"][2],
			color=RED
		)

		tri_def_labels = VGroup(
			tri_def_data["Labels"][2].next_to(tri_def_data["Coordinates"][0] + LEFT + UP*0.5),
			tri_def_data["Labels"][1].next_to(tri_def_data["Coordinates"][1] + UP*0.5),
			tri_def_data["Labels"][0].next_to(tri_def_data["Coordinates"][2] + DOWN*0.5),
		)

		self.play(Create(tri_def))
		self.play(Create(Angle2))
		self.play(Write(tri_def_labels))

		# Explanation

		lines = [
			Text("Given:",font_size=45).move_to([3,5,0]),
			Text("In ∆ ABC and ∆ DEF,",font_size=45).move_to([5,3,0]),
			Text("∠ABC  = ∠DEF = 90°  \t   ............(i)",font_size=45).move_to([8.65,2,0]),
			Text("AB = DE           \t\t\t\t\t   ............(ii)",font_size=45).move_to([8.7,1,0]),
			Text("BC = EF            \t\t\t\t\t  ............(iii)",font_size=45).move_to([8.8,0,0]),
			Text("Comparing (i),(ii) & (iii)",font_size=45).move_to([5.5,-2,0]),
			Text("And, Using the SAS Congruency Rule,",font_size=45).move_to([8.5,-3,0]),
			Text("We come to conclusion that ∆ ABC ≅ ∆ DEF.",font_size=45).move_to([8,-5,0])
		]

		v1 = tri_abc.get_vertices()
		v2 = tri_def.get_vertices()

		AB = Line(v1[0], v1[1], color = YELLOW)
		BC = Line(v1[1],v1[2],color = YELLOW)
		EF = Line(v2[0],v2[1],color = YELLOW) 
		DE = Line(v2[1],v2[2],color = YELLOW)
		
		a1 = RightAngle(
				Line(tri_abc_data["Coordinates"][1],tri_abc_data["Coordinates"][2]),
				Line(tri_abc_data["Coordinates"][0],tri_abc_data["Coordinates"][1]),
				length=0.5,
				quadrant=(1,-1)
			)
		a2 = RightAngle(
				Line(tri_def_data["Coordinates"][1],tri_def_data["Coordinates"][2]),
				Line(tri_def_data["Coordinates"][0],tri_def_data["Coordinates"][1]),
				length=0.5,
				quadrant=(1,-1)
			)

		b_AB = Brace(AB, direction=LEFT)
		AB_text =  b_AB.get_text('4 cm')

		b_BC = Brace(BC)
		BC_text =  b_BC.get_text('6 cm')

		b_DE = Brace(DE, direction=RIGHT)
		DE_text =  b_DE.get_text('4 cm')

		b_EF = Brace(EF, direction=UP)
		EF_text =  b_EF.get_text('6 cm')

		self.play(
			FadeIn(b_AB,AB_text),
			FadeIn(b_BC,BC_text),
			FadeIn(b_DE,DE_text),
			FadeIn(b_EF,EF_text)
			)

		for i in range(len(lines)):
			self.play(Write(lines[i]))
			if i == 2:
				a1.set_stroke(width = 10)
				a2.set_stroke(width=10)
				self.play(
					Indicate(a1,scale_factor=1.75),
					Indicate(a2,scale_factor=1.75)
					)
				self.play(
					FadeOut(a1),
					FadeOut(a2)
					)
				
			elif i == 3:
				AB.set_stroke(width = 10)
				DE.set_stroke(width=10)
				self.play(
					Indicate(AB,scale_factor=1.5),
					Indicate(DE,scale_factor=1.5)
					)
				self.play(
					FadeOut(AB),
					FadeOut(DE)
					)
				
			elif i == 4:
				BC.set_stroke(width = 10)
				EF.set_stroke(width=10)
				self.play(
					Indicate(BC,scale_factor=1.5),
					Indicate(EF,scale_factor=1.5)
					)
				self.play(
					FadeOut(BC),
					FadeOut(EF)
					)
				
			

		self.wait(2)