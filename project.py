from manim import *

class CosineWaveY(Scene):
    def construct(self):
        # Define the circle (orbit) centered at the origin
        orbit = Circle(radius=2, color=WHITE)
        origin_point = ORIGIN

        # Create the moving dot
        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        
        # Animation parameters
        self.t_offset = 0
        rate = 0.25  # Speed of movement

        # Function to move the dot along the vertical circle
        def go_around_circle(mob, dt):
            self.t_offset += dt * rate
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        # Line from origin to the moving dot
        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        # Line projecting the dot's movement along the Y-axis to form a cosine wave
        def get_line_to_curve():
            x = dot.get_center()[0]
            y = self.curve_start[1] + self.t_offset * 4
            return Line(dot.get_center(), np.array([x, y, 0]), color=YELLOW_A, stroke_width=2)

        # Create the curve that traces the motion
        self.curve_start = np.array([dot.get_center()[0], -3, 0])
        self.curve = VGroup()
        self.curve.add(Line(self.curve_start, self.curve_start))

        def get_curve():
            last_line = self.curve[-1]
            x = dot.get_center()[0]
            y = self.curve_start[1] + self.t_offset * 4
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.curve.add(new_line)
            return self.curve

        # Attach the updater to move the dot
        dot.add_updater(go_around_circle)

        # Always redraw the components
        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        cosine_curve_line = always_redraw(get_curve)

        # Add everything to the scene
        self.add(orbit, dot, origin_to_circle_line, dot_to_curve_line, cosine_curve_line)
        self.wait(8.5)

        # Remove the updater after animation
        dot.remove_updater(go_around_circle)
