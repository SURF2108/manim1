from typing_extensions import runtime
from manim import *

class ImageExample(Scene):
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 18.0
    config.frame_width = 32.0

    def construct(self):
        self.slide1()
        self.slide2()
        self.clear()
        self.slide3()
    
    def slide1(self):
        header = Text('Differentiation',font_size=150).move_to(0)
        
        self.play(Write(header))
        
        self.play(FadeOut(header),run_time = 3)



    def slide2(self):
        # Load image (make sure it's in the same folder or provide full path)
        image = SVGMobject("images-samples\\rocket1.svg")
        lens = SVGMobject("images-samples\\telesc-lens.svg")
        stand = SVGMobject("images-samples\\telesc-stand.svg")

        self.height_start = np.array([12,-4,0])

        image.rotate(PI/4)
        image.scale(scale_factor=2)
        self.play(FadeIn(image), run_time=2)
        image.move_to([0])
        self.play(image.animate.scale(scale_factor=0.7).move_to([12,-4,0]),run_time=2)

        lens.rotate(-PI/10)
        lens.move_to([-12,-6,0])
        stand.move_to([-11.8,-7.5,0])
        

        angle_tracker = ValueTracker(-PI/10)

        def update_watcher(mob):
            direction = image.get_center() - mob.get_center()
            new_angle = angle_of_vector(direction)
            current_angle = angle_tracker.get_value()

            # Compute shortest rotation direction
            delta = (new_angle - current_angle + PI) % TAU - PI

            # Rotate and update tracker
            mob.rotate(delta)
            angle_tracker.set_value(current_angle + delta)

        lens.add_updater(update_watcher)

        self.play(FadeIn(lens,stand),run_time = 3)

        path = TracedPath(image.get_bottom, stroke_color=YELLOW, stroke_width=4)
        s = image.get_bottom()
        
        l = lambda: Line(start=lens.get_right(), end=image.get_bottom(), color=GREY)
        connection_line = always_redraw(l) 

        self.add(path)
        self.add(connection_line)

        a = lens.get_right()

        rotation_center = (a)

        base = Line([-12,-4.5,0],[-12,-2,0])
        line_ref = Line(connection_line.get_start(),connection_line.get_end())

        line_ref.rotate(
            angle_tracker.get_value() * DEGREES, about_point=rotation_center
        )


        a = Angle(base,  line_ref, radius=0.5 + MED_LARGE_BUFF, other_angle=True)
        tex = MathTex(r"\theta").move_to(
            Angle(
                base, line_ref , radius=0.5 + 1 * MED_LARGE_BUFF, other_angle=True
            ).point_from_proportion(0.5)
        )

        self.add(base, line_ref,a, tex)
        self.wait()

        

        self.play(image.animate.move_to([12,4,0]), run_time=10)

        st = path.get_start()
        ed = path.get_end()
        p = Line(ed,st, color = YELLOW)
        
        path_b = Brace(p,direction=RIGHT)
        path_txt = path_b.get_text('h',buff = 0.2 )

        self.add(p,path_b,path_txt)

        # Wait to display
        self.wait(2)

    def slide3(self):

        g1 = Text('The question is.....',font_size=80).move_to(0)
        g2 = Text('How fast does the camera need to move to track the rocket?',font_size=70)
        g2.next_to(g1,direction = DOWN,buff = 0.2)
        
        self.play(Write(g1))
        self.wait()
        self.play(Write(g2))
        
        self.play(FadeOut(g1,g2),run_time = 2)
'''
    def slide4(self):

        image = SVGMobject("images-samples\\rocket1.svg")
        lens = SVGMobject("images-samples\\telesc-lens.svg")
        stand = SVGMobject("images-samples\\telesc-stand.svg")

        image.rotate(PI/4)
        image.move_to([12,4,0])
        #lens.rotate(-PI/10)
        lens.move_to([-12,-4.5,0])
        stand.move_to([-11.8,-6,0])




        script = [
        MathTex('Assuming horizontal distance between the camera and the rocket be 5000 m'),
        MathTex('at atmosphere, assuming')
        ]


'''