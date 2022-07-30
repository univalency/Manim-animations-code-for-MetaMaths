#Source code for this video: https://www.youtube.com/watch?v=aznNNCjltH8

from big_ol_pile_of_manim_imports import *
from manimlib.imports import *
import numpy as np 
from scipy.optimize import fsolve



class Lines(GraphScene):

    CONFIG = {
    "y_max" : 5,
    "y_min" : -5,
    "x_max" : 2.5,
    "x_min" : -2.5,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 700,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "axes_color" : WHITE,
    "x_axis_label" : " ",
    "y_axis_label" : " ",
    }

    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN
        
        texx = TextMobject("Lines through a point")
        infty = TextMobject("$\\infty$")
        unc = TextMobject("Uncountable infinity") 

        reals = TextMobject("$\\cong \\, \\mathds{R}$")
        
        texx.scale(0.7)
        texx.to_edge(UP)
        infty.to_edge(UP)
        unc.to_edge(UP)
        unc.scale(0.8)

        point = Dot(0*LEFT, color = WHITE)
        line1 = Line(2*LEFT, 2*RIGHT, color = BLUE)
        line2 = Line(2*LEFT+ DOWN, 2*RIGHT+UP, color = BLUE)
        line3 = Line(2*LEFT+ 0.5*DOWN, 2*RIGHT + 0.5*UP, color = BLUE)
        line4 = Line(2*LEFT+ 0.25*DOWN, 2*RIGHT + 0.25*UP, color = BLUE)

        line5 = Line(2*LEFT+ 0.75*DOWN, 2*RIGHT + 0.75*UP, color = BLUE)
        line6 = Line(2*LEFT+ 1.5*DOWN, 2*RIGHT + 1.5*UP, color = BLUE)
        line7 = Line(2*LEFT+ 1.75*DOWN, 2*RIGHT + 1.75*UP, color = BLUE)
        line9 = Line(2*LEFT+ 1.25*DOWN, 2*RIGHT + 1.25*UP, color = BLUE)

        line8 = Line(2*DOWN, 2*UP, color = BLUE)
        
        line10 = Line(UP*2 + RIGHT*5, RIGHT*5 , color = RED)
        reals.move_to(RIGHT*6 + UP)
        
        zero = TextMobject("0")
        zero.move_to(UP*2 + RIGHT*5.3)
        zero.scale(0.7)

        twop = TextMobject("$2\\pi$")
        twop.move_to(RIGHT*5.3)
        twop.scale(0.7)

        dott = Dot(UP*1.5 + RIGHT*5, color = YELLOW)

        arc = Arc(radius=1.2 , start_angle = 0, angle = 0.48 , 
             arc_center= [0, 0, 0])
        arc.set_color(YELLOW)

        arr1 = Arrow(arc , RIGHT*4.8 + UP*1.5)


        self.play(ShowCreation(point) , Write(texx))
        self.play(ShowCreation(line1))
        self.play(ShowCreation(line2))
        self.play(ShowCreation(line3) , ShowCreation(line4) , 
            ShowCreation(line5), ShowCreation(line6), ShowCreation(line9))
        self.play(ShowCreation(line7), ReplacementTransform(texx, infty))
        #self.play(ShowCreation(line8))
        self.wait()
        self.setup_axes(animate = True)
        self.play(ShowCreation(arc))
        self.play(ShowCreation(line10))
        self.play(Write(zero) , Write(twop))
        self.play(ShowCreation(arr1), Write(dott))

        self.play(Write(reals))
        self.play(ReplacementTransform(infty , unc))
        self.wait()

class eight(GraphScene , MovingCameraScene):
    CONFIG = {
    "y_max" : 5,
    "y_min" : -5,
    "x_max" : 2.5,
    "x_min" : -2.5,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 700,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "axes_color" : WHITE,
    "x_axis_label" : " ",
    "y_axis_label" : " ",
    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN

        point = Dot(0*LEFT, color = WHITE)
        point.scale(0.5)
        real1 = TextMobject("$\\mathds{R}$")
        real2 = TextMobject("$\\mathds{R}$")
        cross = TexMobject("\\mathds{R} \\times \\mathds{R}")
        cross.move_to(RIGHT*5.5)

        cong = TexMobject("\\cong \\, \\mathds{R} \\,  ", "?")
        rational = TextMobject("Rational points")
        rational.set_color(ORANGE)
        rational.to_edge(UP)

        every = TexMobject("Every\\, figure\\, \\longleftrightarrow \\, (q_{1},q_{2})\\in \\mathds{Q}^{2}")
        every.move_to(RIGHT*6 + UP*2)
        every.scale(0.7)

        count = TexMobject("\\mathds{Q}^{2} \\, is \\, countable\\, !")
        count.move_to(RIGHT*6 +UP)
        count.scale(0.7)

        cong.move_to(RIGHT*5.5 + DOWN)
        cong[1].set_color(YELLOW)

        real1.to_edge(UP)
        real2.move_to(RIGHT*3.4)

        circle1 = Circle(radius = 0.4, color = YELLOW, arc_center = [1,1.3,0])
        circle2 = Circle(radius = 0.6, color = YELLOW, arc_center = [2,1.3,0])



        l1 = Line (LEFT*3 + UP*3 , RIGHT*3 + UP*3, stroke_width = 1, color = BLUE)
        l2 = Line (LEFT*3 + UP*2 , RIGHT*3 + UP*2, stroke_width = 1, color = BLUE)
        l3 = Line (LEFT*3 + UP , RIGHT*3 + UP, stroke_width = 1, color = BLUE)

        l4 = Line (LEFT*3 + DOWN , RIGHT*3 + DOWN, stroke_width = 1, color = BLUE)
        l5 = Line (LEFT*3 + DOWN*2 , RIGHT*3 + DOWN*2, stroke_width = 1, color = BLUE)
        l6 = Line (LEFT*3 + DOWN*3 , RIGHT*3 + DOWN*3, stroke_width = 1, color = BLUE)

        l11 = Line (LEFT*3 + UP*3 , LEFT*3 + DOWN*3, stroke_width = 1, color = BLUE)
        l22 = Line (LEFT*2 + UP*3 , LEFT*2 + DOWN*3, stroke_width = 1, color = BLUE)
        l33 = Line (LEFT*1 + UP*3 , LEFT*1 + DOWN*3, stroke_width = 1, color = BLUE)
        l44 = Line (RIGHT*3 + UP*3 , RIGHT*3 + DOWN*3, stroke_width = 1, color = BLUE)
        l55 = Line (RIGHT*2 + UP*3 , RIGHT*2 + DOWN*3, stroke_width = 1, color = BLUE)
        l66 = Line (RIGHT*1 + UP*3 , RIGHT*1 + DOWN*3, stroke_width = 1, color = BLUE)

        self.play(ShowCreation(circle1) , ShowCreation(circle2))
        self.wait()

        self.setup_axes(animate = True)
        self.play(ShowCreation(l1),ShowCreation(l2),ShowCreation(l3), ShowCreation(l4),ShowCreation(l5),ShowCreation(l6))
        self.play(ShowCreation(l11),ShowCreation(l22),ShowCreation(l33), ShowCreation(l44),ShowCreation(l55),ShowCreation(l66))
        self.wait()
        self.play(Write(rational))

        for j in range(15):
            p1 = Dot(j*LEFT*0.2 + UP*2.5, radius = 0.05, color = ORANGE)
            p2 = Dot(j*RIGHT*0.2 + UP*2.5, radius = 0.05, color = ORANGE)

            p3 = Dot(j*LEFT*0.18 + UP*2.25, radius = 0.05, color = ORANGE)
            p4 = Dot(j*RIGHT*0.18 + UP*2.25, radius = 0.05, color = ORANGE)

            p5 = Dot(j*LEFT*0.2 + UP*2, radius = 0.05, color = ORANGE)
            p6 = Dot(j*RIGHT*0.2 + UP*2, radius = 0.05, color = ORANGE)

            p7 = Dot(j*LEFT*0.18 + UP*1.75, radius = 0.05, color = ORANGE)
            p8 = Dot(j*RIGHT*0.18 + UP*1.75, radius = 0.05, color = ORANGE)

            p9 = Dot(j*LEFT*0.2 + UP*1.5, radius = 0.05, color = ORANGE)
            p10 = Dot(j*RIGHT*0.2 + UP*1.5, radius = 0.05, color = ORANGE)

            p11 = Dot(j*LEFT*0.18 + UP*1.25, radius = 0.05, color = ORANGE)
            p12 = Dot(j*RIGHT*0.18 + UP*1.25, radius = 0.05, color = ORANGE)

            p13 = Dot(j*LEFT*0.2 + UP*1, radius = 0.05, color = ORANGE)
            p14 = Dot(j*RIGHT*0.2 + UP*1, radius = 0.05, color = ORANGE)

            p15 = Dot(j*LEFT*0.18 + UP*0.75, radius = 0.05, color = ORANGE)
            p16 = Dot(j*RIGHT*0.18 + UP*0.75, radius = 0.05, color = ORANGE)

            p17 = Dot(j*LEFT*0.2 + UP*0.5, radius = 0.05, color = ORANGE)
            p18 = Dot(j*RIGHT*0.2 + UP*0.5, radius = 0.05, color = ORANGE)

            p19 = Dot(j*LEFT*0.18 + UP*0.25, radius = 0.05, color = ORANGE)
            p20 = Dot(j*RIGHT*0.18 + UP*0.25, radius = 0.05, color = ORANGE)

            self.play(ShowCreation(p1), ShowCreation(p2) ,ShowCreation(p3) , 
                    ShowCreation(p4),ShowCreation(p5),ShowCreation(p6),
                    ShowCreation(p7),ShowCreation(p8),ShowCreation(p9),
                    ShowCreation(p10),ShowCreation(p11),ShowCreation(p12),
                    ShowCreation(p13),ShowCreation(p14),ShowCreation(p15),
                    ShowCreation(p16),ShowCreation(p17),ShowCreation(p18),
                    ShowCreation(p19),ShowCreation(p20) )

        P1 = Dot(RIGHT*1 + UP*1.5, radius = 0.075, color = GREEN)
        P2 = Dot(RIGHT*1.81 + UP*1.25, radius = 0.075, color = GREEN)

        self.play(ShowCreation(P1))
        self.play(ShowCreation(P2))
        self.wait()
        self.play(self.camera_frame.move_to , RIGHT*2.5)
        self.play(Write(every))
        self.wait()
        self.play(Write(count))
        self.wait()






class Circles(GraphScene):
    CONFIG = {
    "y_max" : 5,
    "y_min" : -5,
    "x_max" : 2.5,
    "x_min" : -2.5,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 700,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "axes_color" : WHITE,
    "x_axis_label" : " ",
    "y_axis_label" : " ",
    }

    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN

        point = Dot(0*LEFT, color = WHITE)
        point.scale(0.5)
        real1 = TextMobject("$\\mathds{R}$")
        real2 = TextMobject("$\\mathds{R}$")
        cross = TexMobject("\\mathds{R} \\times \\mathds{R}")
        cross.move_to(RIGHT*5.5)

        cong = TexMobject("\\cong \\, \\mathds{R} \\,  ", "?")

        cong.move_to(RIGHT*5.5 + DOWN)
        cong[1].set_color(YELLOW)

        real1.to_edge(UP)
        real2.move_to(RIGHT*3.4)

        circle1 = Circle(radius = 0.4, color = YELLOW)
        circle2 = Circle(radius = 0.6, color = YELLOW)
        circle3 = Circle(radius = 0.8, color = YELLOW)
        circle4 = Circle(radius = 1, color = YELLOW)

        circle11 = Circle(radius = 0.5, color = YELLOW)
        circle22 = Circle(radius = 0.7, color = YELLOW)
        circle33 = Circle(radius = 0.9, color = YELLOW)
        circle44 = Circle(radius = 1.1, color = YELLOW)

        circle5 = Circle(radius = 1.2, color = YELLOW)
        circle6 = Circle(radius = 1.3, color = YELLOW)
        circle7 = Circle(radius = 1.4, color = YELLOW)
        circle8 = Circle(radius = 1.5, color = YELLOW)
        circle9 = Circle(radius = 1.6, color = YELLOW)
        circle10 = Circle(radius = 1.7, color = YELLOW)
        circle111 = Circle(radius = 1.8, color = YELLOW)
        circle12 = Circle(radius = 1.9, color = YELLOW)
        circle13 = Circle(radius = 2, color = YELLOW)

        gr2 = VGroup(circle5, circle6, circle7, circle8, circle9, circle10, circle111, circle12, circle13)

        l1 = Line (LEFT*3 + UP*3 , RIGHT*3 + UP*3, stroke_width = 1, color = BLUE)
        l2 = Line (LEFT*3 + UP*2 , RIGHT*3 + UP*2, stroke_width = 1, color = BLUE)
        l3 = Line (LEFT*3 + UP , RIGHT*3 + UP, stroke_width = 1, color = BLUE)

        l4 = Line (LEFT*3 + DOWN , RIGHT*3 + DOWN, stroke_width = 1, color = BLUE)
        l5 = Line (LEFT*3 + DOWN*2 , RIGHT*3 + DOWN*2, stroke_width = 1, color = BLUE)
        l6 = Line (LEFT*3 + DOWN*3 , RIGHT*3 + DOWN*3, stroke_width = 1, color = BLUE)

        l11 = Line (LEFT*3 + UP*3 , LEFT*3 + DOWN*3, stroke_width = 1, color = BLUE)
        l22 = Line (LEFT*2 + UP*3 , LEFT*2 + DOWN*3, stroke_width = 1, color = BLUE)
        l33 = Line (LEFT*1 + UP*3 , LEFT*1 + DOWN*3, stroke_width = 1, color = BLUE)
        l44 = Line (RIGHT*3 + UP*3 , RIGHT*3 + DOWN*3, stroke_width = 1, color = BLUE)
        l55 = Line (RIGHT*2 + UP*3 , RIGHT*2 + DOWN*3, stroke_width = 1, color = BLUE)
        l66 = Line (RIGHT*1 + UP*3 , RIGHT*1 + DOWN*3, stroke_width = 1, color = BLUE)

        self.play(ShowCreation(point))
        self.play(ShowCreation(circle1))
        self.play(ShowCreation(circle2) , ShowCreation(circle3) , ShowCreation(circle4))
        self.wait()
        self.play(ShowCreation(circle11))
        self.play(ShowCreation(circle22),ShowCreation(circle33),ShowCreation(circle44))
        self.wait()

        self.setup_axes(animate = True)
        self.play(ShowCreation(l1),ShowCreation(l2),ShowCreation(l3), ShowCreation(l4),ShowCreation(l5),ShowCreation(l6))
        self.play(ShowCreation(l11),ShowCreation(l22),ShowCreation(l33), ShowCreation(l44),ShowCreation(l55),ShowCreation(l66))
        self.play(Write(real1), Write(real2))
        self.wait()

        gr1 = VGroup(real1, real2)
        self.play(ReplacementTransform(gr1, cross))
        self.wait()
        self.play(ShowCreation(gr2))
        self.play(Uncreate(gr2))
        self.play(Write(cong[0]))
        self.play(Write(cong[1]))
        self.wait()

class quote(Scene):
    def construct(self):
        texx = TextMobject("I see it but I do not believe it ...")

class remark(Scene):
    def construct(self):
        texx = TextMobject("* this fact")
        self.play(FadeIn(texx))
        self.play(FadeOut(texx))

class circles11(Scene):
    def construct(self):
        c1 = Circle(radius = 2)
        c2 = Circle(radius = 1, arc_center = [3,0,0])

        self.play(ShowCreation(c1) ,ShowCreation(c2))

        self.wait()

class circles12(Scene):
    def construct(self):
        c1 = Circle(radius = 2)
        c2 = Circle(radius = 1, arc_center = [3,0,0])

        c1.set_color(GREEN)
        c2.set_color(GREEN)

        self.play(ShowCreation(c1) ,ShowCreation(c2))

        self.wait()

class circles13(Scene):
    def construct(self):
        c1 = Circle(radius = 2)
        c2 = Circle(radius = 2, arc_center = [4,0,0])

        c1.set_color(BLUE)
        c2.set_color(BLUE)

        self.play(ShowCreation(c1) ,ShowCreation(c2))

        self.wait()

class circles14(Scene):
    def construct(self):
        c1 = Circle(radius = 2)
        c2 = Circle(radius = 0.5, arc_center = [2.5,0,0])

        c1.set_color(YELLOW)
        c2.set_color(YELLOW)

        self.play(ShowCreation(c1) ,ShowCreation(c2))

        self.wait()

class circles15(Scene):
    def construct(self):
        c1 = Circle(radius = 2)
        c2 = Circle(radius = 0.5, arc_center = [2.5,0,0])

        c1.set_color(RED)
        c2.set_color(RED)

        self.play(ShowCreation(c1) ,ShowCreation(c2))

        self.wait()

class square_to_circle(Scene):
    def construct(self):
        sq = Polygon(2*RIGHT + DOWN , 2*RIGHT + UP, 4*RIGHT + UP, 4*RIGHT + DOWN)
        l1 = Line(3*LEFT , 1.5*LEFT)
        equiv = TextMobject("$\\cong $")

        self.play(ShowCreation(l1))
        self.play(TransformFromCopy(l1 , sq))
        self.wait()
        self.play(Write(equiv))
        self.wait()

class titles(Scene):
    def construct(self):
        ph1 = TextMobject("Non - intersecting figures of eight")
        ph2 = TextMobject("But how much infinite ?")


        ph1.move_to(UP*2)

        self.play(Write(ph1))
        self.play(Write(ph2))
        self.wait()

class uncount1(Scene):
    def construct(self):
        tex1 = TextMobject("Uncountable", " infinity")
        tex2 = TextMobject("Countable", " infinity")

        tex3 = TexMobject("\\mathds{N}")

        self.play(Write(tex1))
        self.play(ReplacementTransform(tex1[0], tex2[0]))
        self.wait()
        self.play(Uncreate(tex1), Uncreate(tex2[0]))
        self.play(ShowCreation(tex3))
        self.wait()

class arrow(Scene):
    def construct(self):
        arr1 = TexMobject("\\longleftrightarrow")

        self.play(ShowCreation(arr1))
        self.wait()

class letter(Scene):
    def construct(self):
        tex1 = TextMobject("\\emph{In a letter to Dedekind (1877) :}")
        tex2 = TextMobject(" ' I see but I do not believe ... ' ")

        tex1.to_edge(UP)

        self.play(Write(tex1))
        self.play(Write(tex2))
        self.wait()


class CurveGraph(GraphScene):
    CONFIG = {
    "y_max" : 5,
    "y_min" : -5,
    "x_max" : 2.5,
    "x_min" : -2.5,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 700,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "axes_color" : BLACK
    }
    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN
        self.setup_axes(animate=False)
        func_graph=self.get_graph(self.func_to_graph,x_min = -0.99999, x_max = -0.00001, color=YELLOW)
        func_graph_2=self.get_graph(self.func_to_graph_2,x_min = -0.99999, x_max = -0.00001, color=YELLOW)

        graph1 = self.get_graph(self.func_to_graph,x_min = 1.0001, x_max = 2.5, color=YELLOW)
        graph2 = self.get_graph(self.func_to_graph_2,x_min = 1.0001, x_max = 2.5, color=YELLOW)
        line1 = self.get_graph(self.line1, x_min = -1, x_max = 1, color = GREEN)
        #func_graph_3=self.get_graph(self.func_to_graph,x_min=-0.6823,x_max=3, color=BLUE)
        #func_graph_4=self.get_graph(self.func_to_graph_2,x_min=-0.6823,x_max=3, color=BLUE)
        self.play(ShowCreation(func_graph),ShowCreation(func_graph_2),ShowCreation(graph1),ShowCreation(graph2))
        self.wait()
        #self.play(Uncreate(func_graph),Uncreate(func_graph_2),Uncreate(graph1),Uncreate(graph2))
        self.wait(2)
        #self.play(ShowCreation(func_graph_3),ShowCreation(func_graph_4))

    def func_to_graph(self,x):
        return(np.sqrt(x**3 - x))
    def func_to_graph_2(self,x):
        return(-1*np.sqrt(x**3 - x))
    def line1(sefl,x):
        return(0.5*x + 1)
