from manim import *

class curve(Scene):
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 18.0
    config.frame_width =32.0

    def construct(self):
        self.show_axis()
        self.add_x_labels()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()



    def show_axis(self):
        x_start = np.array([-5,-2,0])
        x_end = np.array([5,-2,0])

        y_start = np.array([-4,-3,0])
        y_end = np.array([-4,7,0])


        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)


        self.origin_point = np.array([-4,-2,0])
        self.curve_start = np.array([-3,-2,0])
        self.curve_start_cos = np.array([-3,-1,0])
        

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        
    def add_x_labels(self):
        x_labels = [
            MathTex(r"0"),
            MathTex(r"\pi"), 
            MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), 
            MathTex(r"4 \pi")
        ]
        y_labels = [
            MathTex(r"0"),
            MathTex(r"\pi"), 
            MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), 
            MathTex(r"4 \pi")
        ]
        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-2.8 + 2*i,-2, 3]), DOWN)
            self.add(x_labels[i])
        for i in range(len(y_labels)):
            y_labels[i].next_to(np.array([-4.5,-1.5 + 2*i, 2]), UP)
            self.add(y_labels[i])

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        self.y_offset = 0.25
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            self.y_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle1():
            return Line(origin_point, dot.get_center(), color=BLUE)
        def get_line_to_circle2():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve1():
            y = self.curve_start_cos[1] + self.t_offset * 4
            x = dot.get_center()[0]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=1 )

        def get_line_to_curve2():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=1 )


        self.curve1 = VGroup()
        self.curve1.add(Line(self.curve_start_cos,self.curve_start_cos))

        def get_curve1():
            last_line = self.curve1[-1]
            y = self.curve_start_cos[1] + self.t_offset * 4
            x = dot.get_center()[0]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve1.add(new_line)

            return self.curve1

        self.curve2 = VGroup()
        self.curve2.add(Line(self.curve_start,self.curve_start))

        def get_curve2():
            last_line = self.curve2[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve2.add(new_line)

            return self.curve2

        dot.add_updater(go_around_circle)

        origin_to_circle_line1 = always_redraw(get_line_to_circle1)
        origin_to_circle_line2 = always_redraw(get_line_to_circle2)
        dot_to_curve_line1 = always_redraw(get_line_to_curve1)
        sine_curve_line1 = always_redraw(get_curve1)
        dot_to_curve_line2 = always_redraw(get_line_to_curve2)
        sine_curve_line2 = always_redraw(get_curve2)

        self.add(dot)
        self.add(orbit, origin_to_circle_line1, dot_to_curve_line1, sine_curve_line1)
        self.add(orbit, origin_to_circle_line2, dot_to_curve_line2, sine_curve_line2)
        self.wait(8)

        dot.remove_updater(go_around_circle)