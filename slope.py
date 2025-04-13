from manim import *

class diff_slope(Scene):
    def construct(self):
        # Axes
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 9, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False},
        )
        axes.add_coordinates()
        self.play(Create(axes))

        # Plot parabola
        parabola = axes.plot(lambda x: x**2, x_range=[0, 3], color=BLUE)
        self.play(Create(parabola))

        # Constants and tracker
        x = 1
        h_tracker = ValueTracker(1)

        # Dot 1 (static)
        dot1 = Dot(axes.c2p(x, x**2), color=YELLOW)

        # Dot 2 (moves with h_tracker)
        dot2 = always_redraw(lambda: Dot(
            axes.c2p(x + h_tracker.get_value(), (x + h_tracker.get_value())**2),
            color=YELLOW
        ))

        # Dashed lines for dot1
        dl_x1 = DashedLine(axes.c2p(x, 0), axes.c2p(x, x**2), color=WHITE)
        dl_y1 = DashedLine(axes.c2p(0, x**2), axes.c2p(x, x**2), color=WHITE)

        # Dashed lines for dot2
        dl_x2 = always_redraw(lambda: DashedLine(
            axes.c2p(x + h_tracker.get_value(), 0),
            dot2.get_center(), color=WHITE
        ))
        dl_y2 = always_redraw(lambda: DashedLine(
            axes.c2p(0, (x + h_tracker.get_value())**2),
            dot2.get_center(), color=WHITE
        ))

        
        def get_extended_secant():
            p1 = dot1.get_center()
            p2 = dot2.get_center()
            direction = p2 - p1
            if np.linalg.norm(direction) == 0:
                direction = np.array([1e-6, 0, 0])  # Avoid divide-by-zero
            unit_dir = direction / np.linalg.norm(direction)
            length = 6  # Total visual length of the secant line
            center = (p1 + p2) / 2
            start = center - unit_dir * (length / 2)
            end = center + unit_dir * (length / 2)
            return Line(start, end, color=RED)

        secant = always_redraw(get_extended_secant)

        # Horizontal line between the x-coordinates of the two dots 
        h_line_for_brace = always_redraw(lambda: Line(
            start=axes.c2p(x, 0),
            end=axes.c2p(x + h_tracker.get_value(), 0),
            color=GREY
        ))

        # Dynamic brace 
        brace = always_redraw(lambda: (
            Brace(h_line_for_brace, direction=UP, color=WHITE,buff = 0)
            if h_tracker.get_value() > 0.02 else VGroup()
        ))

        

        brace_label = Text('h').next_to(brace,UP*0.3)
        brace_label.scale(0.4)

        lx = Text('x').next_to(dot1,RIGHT*0.5)
        lfx = Text('f(x)').next_to(dot1,(LEFT+UP)*0.5)

        lx.scale(0.4)
        lfx.scale(0.4)

        lxh = Text('x+h').next_to(dot2,RIGHT*0.5)
        lfxh = Text('f(x+h)').next_to(dot2,(LEFT+UP)*0.5)

        lxh.scale(0.4)
        lfxh.scale(0.4)


        # After all creations and animations
        everything = VGroup(axes, parabola, dot1, dot2, dl_x1, dl_y1, dl_x2, dl_y2, secant, h_line_for_brace, brace, brace_label,lx,lfx,lxh,lfxh)
        self.play(everything.animate.shift(UP * 1.5))  # Shift up by 1.5 units


        # Animation sequence
        self.play(Create(secant))                                           # 1. Secant appears
        self.wait(0.5)
        self.play(FadeIn(dot1), FadeIn(dot2))                               # 2. Dots appear
        self.wait(0.5)
        self.play(Create(dl_x1), Create(dl_y1))                             # 3. Dashed lines for dot1
        self.play(Create(dl_x2), Create(dl_y2))                             # 4. Dashed lines for dot2
        self.wait(0.5)
        self.add((h_line_for_brace), (brace), (brace_label))  # 5. Brace + label
        self.wait(0.5)
        self.play(FadeIn(lx),FadeIn(lfx),FadeIn(lxh),FadeIn(lfxh))
        self.wait(2)
        self.play(FadeOut(lx),FadeOut(lfx),FadeOut(lxh),FadeOut(lfxh),FadeOut(brace_label))
        self.wait(0.5)
        #self.play(h_tracker.animate.set_value(0), run_time=2)              # 6. Move dot2 toward dot1
        #self.wait()