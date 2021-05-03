#This code was used for my video on elliptic curves: https://youtu.be/qCafMW4OG7s
#It is not too tidy but you can run and see what it generates !


from big_ol_pile_of_manim_imports import *
from manimlib.imports import *
import numpy as np 
from scipy.optimize import fsolve


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



class tangent(GraphScene,MovingCameraScene):
    CONFIG = {
    "y_max" : 6,
    "y_min" : -6,
    "x_max" : 4, #2
    "x_min" : -4, #-2
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 6000,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "axes_color" : GREY
    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,x_min=-0.6823, x_max=73, color=BLUE)
        func_graph_2=self.get_graph(self.func_to_graph_2,x_min=-0.6823, x_max=73, color=BLUE)
        line1 = self.get_graph(self.line1, x_min = -2, x_max = 2, color = GREEN)
        line2 = self.get_graph(self.line2, x_min = -3, x_max = 73, color = GREEN)
        #func_graph_3=self.get_graph(self.func_to_graph,x_min=-0.6823,x_max=3, color=BLUE)
        #func_graph_4=self.get_graph(self.func_to_graph_2,x_min=-0.6823,x_max=3, color=BLUE)
        point1 = Dot(self.coords_to_point(0,self.func_to_graph(0)), radius = 0.04)
        point2 = Dot(self.coords_to_point(0.25,self.func_to_graph(0.25)), radius = 0.04)
        point3 = Dot(self.coords_to_point(0.25,self.func_to_graph_2(0.25)),radius = 0.04)
        point4 = Dot(self.coords_to_point(72,self.func_to_graph_2(72)),radius = 10)
        point5 = Dot(self.coords_to_point(72,self.func_to_graph(72)),radius = 10) #-611

        p1label=TextMobject("P")
        p1label.scale(0.9)
        p1label.set_color(YELLOW)
        p1label.next_to(point1,LEFT)

        p11label = TextMobject("(0,1)")
        p11label.scale(0.8)
        p11label.set_color(YELLOW)
        p11label.next_to(point1,LEFT)

        p2label=TextMobject("2P")
        p2label.scale(0.9)
        p2label.set_color(YELLOW)
        p2label.next_to(point3,RIGHT)

        p22label=TextMobject("(0.25,-1.125)")
        p22label.scale(0.8)
        p22label.set_color(YELLOW)
        p22label.next_to(point3,RIGHT)

        p4label = TextMobject("3P")
        p4label.scale(80)
        p4label.set_color(YELLOW)
        p4label.next_to(point5,RIGHT*6)

        eqn=TextMobject("$y^2=x^3 + x + 1$")
        eqn.scale(1)
        eqn.move_to(LEFT*3 + UP*3)


        self.play(ShowCreation(func_graph),ShowCreation(func_graph_2))
        self.play(ShowCreation(point1),ShowCreation(p1label))
        self.play(self.camera_frame.move_to,UP)
        self.play(
            self.camera_frame.scale,.4,
            )
        self.play(ShowCreation(line1))
        self.play(ShowCreation(point2))
        self.wait()
        self.play(
            self.camera_frame.scale,2.5,
            #self.camera_frame.move_to,DOWN*0.8
            )
        self.play(self.camera_frame.move_to,DOWN*0.1)
        self.wait()
        self.play(ShowCreation(point3), ShowCreation(p2label))
        #self.play(ShowCreation(func_graph_3),ShowCreation(func_graph_4))
        self.wait()
        self.play(ShowCreation(line2))
        self.play(self.camera_frame.scale,85)
        self.play(ShowCreation(point4))
        self.play(ShowCreation(point5),Write(p4label))
        self.wait(2)
        self.play(self.camera_frame.scale,0.011)
        self.wait(2)
        self.play(Write(eqn))
        self.wait()
        self.play(ReplacementTransform(p1label,p11label))
        self.play(ReplacementTransform(p2label,p22label))
        self.wait(2)

    def func_to_graph(self,x):
        return(np.sqrt(x**3 + 1*x + 1))
    def func_to_graph_2(self,x):
        return(-1*np.sqrt(x**3 + 1*x + 1))
    def line1(sefl,x):
        return(0.5*x + 1)
    def line2(self,x):
        return(-8.5*x + 1)


class SecondOrder(Scene):
    def construct(self):
        tex = TextMobject("Associativity:")
        texx = TexMobject("nP \\, + mP \\, =\\, (n\\, +\\, m)P")
        tex.move_to(UP)
        self.play(Write(tex))
        self.play(Write(texx))
        self.wait(2)



class Parabola(GraphScene):
    CONFIG = {
    "y_max" : 3,
    "y_min" : -3,
    "x_max" : 2,
    "x_min" : -2,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 600,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "axes_color" : GREY
    }
    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN
        self.setup_axes(animate=True)
        parabola = self.get_graph(self.parabola,x_min= -0.6, x_max = 0.85, color=BLUE)
        #func_graph_2=self.get_graph(self.func_to_graph_2,x_min=-0.6823, x_max=2, color=BLUE)
        line1 = self.get_graph(self.line1, x_min = -2, x_max = 2, color = GREEN)
        line2 = self.get_graph(self.line2, x_min = -2, x_max = 2, color = YELLOW)
        line3 = self.get_graph(self.line3, x_min = 0.38, x_max = 0.42, color = RED)
        #func_graph_3=self.get_graph(self.func_to_graph,x_min=-0.6823,x_max=3, color=BLUE)
        #func_graph_4=self.get_graph(self.func_to_graph_2,x_min=-0.6823,x_max=3, color=BLUE)
        eqn=TextMobject("$y=0.2x^2 + 1$")
        eqn.scale(0.75)
        eqn.shift(4*RIGHT + 3*UP)
        self.play(ShowCreation(parabola))
        self.wait(2)
        self.play(ShowCreation(line2))
        self.play(Uncreate(line2) , ShowCreation(line3))
        self.play(Uncreate(line3) , ShowCreation(line1))
        self.wait(2)
        self.play(ShowCreation(line3) , ShowCreation(line2))
        #self.play(ShowCreation(func_graph_3),ShowCreation(func_graph_4))
        #self.play(Write(eqn))
        self.wait(2)

    def parabola(self,x):
        return(4*x**2 - 1*x - 0.5)
    def line1(sefl,x):
        return(0.2*x + 1)
    def line2(self,x):
        return(-x - 1)
    def line3(self,x):
        return(100*x - 40)



class ThirdOrder(GraphScene):
    CONFIG = {
    "y_max" : 3,
    "y_min" : -3,
    "x_max" : 2,
    "x_min" : -2,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 600,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "axes_color" : GREY
    }
    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN
        self.setup_axes(animate=True)
        func1 = self.get_graph(self.func1,x_min= -0.6823, x_max = 2, color=BLUE)
        func2 = self.get_graph(self.func2,x_min= -0.6823, x_max = 2, color=BLUE)
        line = self.get_graph(self.line,x_min= -1, x_max = 2, color=BLUE)
        vertical = self.get_graph(self.vertical, x_min= 1.435, x_max = 1.468, color=BLUE)
        #func_graph_2=self.get_graph(self.func_to_graph_2,x_min=-0.6823, x_max=2, color=BLUE)
        #func_graph_3=self.get_graph(self.func_to_graph,x_min=-0.6823,x_max=3, color=BLUE)
        #func_graph_4=self.get_graph(self.func_to_graph_2,x_min=-0.6823,x_max=3, color=BLUE)
        eqn=TextMobject("$y^2 = x^3 + Ax + B$")
        ell = TextMobject("Elliptic curve")
        #point1=Dot(0.243*UP + 0.657*LEFT)
        #point2=Dot(1.098*UP + 0.198*RIGHT)

        point1=Dot(self.coords_to_point(-0.657,self.func1(-0.657)))
        point2=Dot(self.coords_to_point(0.198,self.func1(0.198)))
        point3=Dot(self.coords_to_point(1.459,self.func1(1.459)))
        point4=Dot(self.coords_to_point(1.459,self.func2(1.459)))

        p1label=TextMobject("P")
        p1label.scale(0.55)
        p1label.next_to(point1,LEFT)

        p2label=TextMobject("Q")
        p2label.scale(0.55)
        p2label.next_to(point2,UP)

        p3label=TextMobject("P + Q")
        p3label.scale(0.55)
        p3label.next_to(point3,LEFT)

        p4label=TextMobject("P + Q")
        p4label.scale(0.65)
        p4label.set_color(YELLOW)
        p4label.next_to(point4,LEFT)




        eqn.scale(0.75)
        eqn.move_to(UP*3 + LEFT*3)
        ell.scale(0.75)
        ell.move_to(UP*3 + LEFT*3)
        ell.set_color(YELLOW)
        #eqn.shift(4*RIGHT + 3*UP)
        self.play(Write(eqn))
        self.wait()
        self.play(ShowCreation(func1),ShowCreation(func2))
        self.wait()
        self.play(ReplacementTransform(eqn,ell))
        self.wait()
        self.play(Write(point1))
        self.play(Write(point2))
        self.play(ShowCreation(line))
        self.play(Write(point3))
        self.wait(2)
        self.play(Write(p1label))
        self.play(Write(p2label))
        self.play(Write(p3label))
        self.wait()
        self.play(ShowCreation(vertical))
        self.play(Uncreate(p3label))
        self.play(Write(point4))
        self.wait()
        self.play(ShowCreation(p4label))
        #self.play(ShowCreation(func_graph_3),ShowCreation(func_graph_4))
        #self.play(Write(eqn))
        self.wait(2)

    def func1(self,x):
        return(np.sqrt(x**3 + 1*x + 1))
    def func2(self,x):
        return(-1*np.sqrt(x**3 + 1*x + 1))
    def line(self,x):
        return(x + 0.9)
    def vertical(self,x):
        return(200*x - 290)




class Hyperbola(GraphScene):
    CONFIG = {
    "y_max" : 3,
    "y_min" : -3,
    "x_max" : 2,
    "x_min" : -2,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 600,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "axes_color" : GREY
    }
    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN
        self.setup_axes(animate=True)
        hyper1 = self.get_graph(self.hyper1,x_min= 0.317, x_max = 2, color=BLUE)
        hyper2 = self.get_graph(self.hyper2,x_min= 0.317, x_max = 2, color=BLUE)
        hyper3 = self.get_graph(self.hyper3,x_min= -0.317, x_max = -2, color=BLUE)
        hyper4 = self.get_graph(self.hyper4,x_min= -0.317, x_max = -2, color=BLUE)
        #func_graph_2=self.get_graph(self.func_to_graph_2,x_min=-0.6823, x_max=2, color=BLUE)
        line1 = self.get_graph(self.line1, x_min = -2, x_max = 2, color = GREEN)
        line2 = self.get_graph(self.line2, x_min = -2, x_max = 2, color = YELLOW)
        line3 = self.get_graph(self.line3, x_min = -2, x_max = 2, color = RED)
        #func_graph_3=self.get_graph(self.func_to_graph,x_min=-0.6823,x_max=3, color=BLUE)
        #func_graph_4=self.get_graph(self.func_to_graph_2,x_min=-0.6823,x_max=3, color=BLUE)
        eqn=TextMobject("$y=0.2x^2 + 1$")
        eqn.scale(0.75)
        eqn.shift(4*RIGHT + 3*UP)
        self.play(ShowCreation(hyper1), ShowCreation(hyper2), ShowCreation(hyper3),ShowCreation(hyper4))
        self.wait(2)
        self.play(ShowCreation(line2))
        self.play(Uncreate(line2) , ShowCreation(line1))
        self.play(Uncreate(line1) , ShowCreation(line3))
        self.wait(2)
        #self.play(ShowCreation(line3) , ShowCreation(line2))
        #self.play(ShowCreation(func_graph_3),ShowCreation(func_graph_4))
        #self.play(Write(eqn))
        self.wait(2)

    def hyper1(self,x):
        return(np.sqrt(x**2 - 0.1))
    def hyper2(self,x):
        return(-np.sqrt(x**2 - 0.1))
    def hyper3(self,x):
        return(np.sqrt(x**2 - 0.1))
    def hyper4(self,x):
        return(-np.sqrt(x**2 - 0.1))
    def line1(sefl,x):
        return(x - 1)
    def line2(self,x):
        return(2*x)
    def line3(self,x):
        return(0.5*x + 0.5)




class Points(Scene):
    def construct(self):
        title=TextMobject("Consecutive points on our elliptic curve:")
        title.scale(0.9)
        title.to_edge(UP)

        p1 = TextMobject("$P = (0,1)$")
        p2 = TextMobject("$2P = (\\frac{1}{4},\\frac{-9}{8})$")
        p3 = TextMobject("$3P = (\\frac{-287}{1296},\\frac{40879}{46656})$")
        p4 = TextMobject("$4P = (\\frac{43992}{82369},\\frac{-30699397}{23639903})$")
        p5 = TextMobject("$5P = (\\frac{26862913}{1493284},\\frac{139455877527}{1824793048})$")
        p6 = TextMobject("$6P = (\\frac{-3596697936}{8760772801},\\frac{591456591665497}{819999573400799})$")

        p1.scale(0.7)
        p2.scale(0.7)
        p3.scale(0.7)
        p4.scale(0.7)
        p5.scale(0.7)
        p6.scale(0.7)

        p1.move_to(UP*2)
        p2.move_to(UP)
        p4.move_to(DOWN)
        p5.move_to(DOWN*2)
        p6.move_to(DOWN*3)


        self.play(Write(title))

        self.play(Write(p1),Write(p2),Write(p3),Write(p4),Write(p5),Write(p6))


class cryp(Scene):
    def construct(self):
        title = TextMobject("Cryptography")
        priv = TextMobject("Private key")
        pub = TextMobject("Public key")
        receiver = TextMobject("Receiver")
        principle = TextMobject("\\textit{It should be computationally hard}",
                                "\\textit{to derive private key from public}")

        principle[0].move_to(DOWN*2)
        principle[1].move_to(DOWN*3)

        title.to_edge(UP)
        priv.move_to(LEFT*4.5)
        pub.move_to(UP*2.5 + LEFT*4.5)
        receiver.move_to(UP*2.5 + RIGHT*4.5)

        self.play(Write(title))
        self.wait(2)
        self.play(Write(priv))
        self.wait(2)
        self.play(Write(pub))
        self.wait()
        self.play(Write(receiver))
        self.wait()
        self.play(Write(principle))
        self.wait(2)


class ell(Scene):
    def construct(self):
        title = TextMobject("Elliptic curve cryptogrpahy")
        point = TextMobject("Take P $\\in \\mathds{Q}^{2}$")
        add = TextMobject("P + P + P + ... + P =",
            "n", "P",
            " = $(\\frac{26862913}{1493284},\\frac{139455877527}{1824793048})$")
        priv = TextMobject("Private key")
        pub = TextMobject("Public key")
        n = TextMobject("n")
        nn = TextMobject("n")
        frac = TextMobject("$$(\\frac{26862913}{1493284},\\frac{139455877527}{1824793048})$$")

        title.to_edge(UP)
        point.move_to(UP*2)
        add.move_to(UP)
        priv.move_to(DOWN + LEFT*3)
        pub.move_to(DOWN + RIGHT*3)
        n.move_to(LEFT*3 + DOWN*2)
        nn.move_to(UP + LEFT*0.3)
        frac.move_to(DOWN*2 + RIGHT*3)


        add[1].set_color(YELLOW)
        n.set_color(YELLOW)
        nn.set_color(YELLOW)
        frac.scale(0.7)

        self.play(Write(title))
        self.wait()
        self.play(Write(point))
        self.wait()
        self.play(Write(add[0]))
        self.wait()
        self.play(Write(add[1]),Write(add[2]))
        self.wait()
        self.play(Write(add[3]))
        self.wait()
        self.play(Write(priv))
        self.wait()
        self.play(Write(pub))
        self.wait()
        self.play(Transform(add[1],n),Write(nn))
        self.wait()
        self.play(Write(frac))
        self.wait(3)


class FiniteField(Scene):
    def construct(self):
        title = TextMobject("Finite field " , "$\\,  (\\mathds{F}_{p})$")
        p1 = TextMobject("$P = (0,1)$")
        p2 = TextMobject("$2P = (\\frac{1}{4},\\frac{-9}{8})$")
        p3 = TextMobject("$3P = (\\frac{-287}{1296},\\frac{40879}{46656})$")
        p4 = TextMobject("$4P = (\\frac{43992}{82369},\\frac{-30699397}{23639903})$")
        p5 = TextMobject("$5P = (\\frac{26862913}{1493284},\\frac{139455877527}{1824793048})$")
        p6 = TextMobject("$6P = (\\frac{-3596697936}{8760772801},\\frac{591456591665497}{819999573400799})$")
        eq = TextMobject("$y^2 = x^3 + Ax + B$ $,\\, \\,$ " , " $x,y \\in \\mathds{R}$")
        field = TexMobject("x,y \\in \\mathds{F}_{p}")
        mod = TextMobject("mod p")


        sett = TexMobject("\\{\\, a_{1},\\, a_{2}, \\, ... \\, , a_{m}\\, \\}")
        oper = TexMobject("a_{i} + a_{j}, \\,  \\," , "a_{i}  a_{j}, \\, \\," , "\\frac{a_{i}}{a_{j}} \\, \\," , "\\, \\, \\in \\mathds{F}_{p}\\, \\, \\forall \\, i,j")

        ex1 = TextMobject("$4\\, + \\, 3 \\, = \\, 2 \\, \\, \\,  mod\\, \\, 5$" )
        ex2 = TextMobject("$\\frac{4}{3}\\, =\\,$ " , "$4\\, \\cdot \\, 3^{-1}\\, = \\,$ " , "$ 4\\, \\cdot \\, 2\\,$ ", "$ =\\, 3 \\, \\, \\, mod \\, \\, 5 $ ")

        title.to_edge(UP)
        field.move_to(RIGHT*2.5 + DOWN*0.05)
        sett.move_to(UP)
        oper.move_to(DOWN*0.2)

        group = VGroup(oper[0],oper[1],oper[2])

        braces = Brace(group, DOWN)
        mod.next_to(braces, DOWN)
        ex2.move_to(DOWN)

        self.play(Write(p1))
        self.wait()
        self.play(ReplacementTransform(p1,p2))
        self.play(ReplacementTransform(p2,p3))
        self.play(ReplacementTransform(p3,p4))
        self.play(ReplacementTransform(p4,p5))
        self.play(ReplacementTransform(p5,p6))
        self.wait()
        self.play(Uncreate(p6))
        self.wait()
        self.play(Write(eq))
        self.wait()
        self.play(ReplacementTransform(eq[1], field), Write(title))
        self.play(FadeOut(eq),FadeOut(field))
        self.wait()
        self.play(Write(sett))
        self.wait()
        self.play(Write(oper[0]))
        self.play(Write(oper[1]))
        self.play(Write(oper[2]))
        self.play(Write(oper[3]))
        self.wait()
        self.play(GrowFromCenter(braces))
        self.wait()
        self.play(Write(mod))
        self.wait()

        self.play(Uncreate(mod),Uncreate(braces),Uncreate(oper),Uncreate(sett))
        self.wait()
        self.play(Write(ex1))
        self.wait()
        self.play(Write(ex2[0]))
        self.play(Write(ex2[1]))
        self.play(Write(ex2[2]))
        self.play(Write(ex2[3]))
        self.wait(3)

class fieldcurve(Scene):
    def construct(self):
        eq = TextMobject("$y^{2} = x^{3} + x + 1 \\,$ $\\, mod \\, \\, \\, p$")

        eq.to_edge(UP)

        self.play(Write(eq))



class BitCurve(Scene):
    def construct(self):
        title = TextMobject("Bitcoin curve")
        title2 = TextMobject("secp256k1")
        prime = TexMobject("p\\, =\\, 2^{256}\\, - \\, 2^{32}\\, - \\, 977")
        sec = TextMobject("same level of security as 3072 bit keys in",
            "RSA and Diffie- Hellman protocols")

        eq = TexMobject("y^{2}\\, =\\, x^{3}\\, +\\, 7")
        eqq = TexMobject("y^{2}\\, =\\, x^{3}\\, +\\, 7\\, \\, mod \\, \\, p")

        title.to_edge(UP)
        title2.to_edge(UP)
        eq.next_to(title2, DOWN)

        prime.move_to(UP)

        sec[0].move_to(DOWN)
        sec[1].move_to(DOWN*2)

        self.play(Write(title))
        self.wait()
        self.play(ReplacementTransform(title, title2))
        self.wait()
        self.play(Write(eq))
        self.wait()
        self.play(Write(prime))
        self.wait()
        self.play(Write(sec[0]))
        self.wait()
        self.play(Write(sec[1]))
        self.wait()


class base(Scene):
    def construct(self):
        title = TextMobject("Base point for Bitcoin curve")
        pt = TextMobject("0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", " (Hexadecimal)")
        conv = TextMobject("Decimal: 76751168793442242021316642153937790282562248148484193353443515174504851600675307116192347320074217636505817912891152280")
        n = TexMobject("0\\, \\leq \\, n\\, \\leq \\, 2^{256}")
        pt.scale(0.6)
        conv.scale(0.4)
        n.scale(0.8)

        title.to_edge(UP)
        pt.move_to(UP*2)
        conv.move_to(UP)

        self.play(Write(title))
        self.play(Write(pt[0:1]))
        self.play(Write(pt[1]))
        self.play(Write(conv))
        self.play(Uncreate(conv))
        self.play(Write(n))



class Adversary(Scene):
    def construct(self):
        eq = TexMobject("y^2 =  x^3 + x + 1")
        pt = TextMobject("P = $(0,1)$")
        end = TextMobject("nP = $(\\frac{26862913}{1493284},\\frac{139455877527}{1824793048})$")
        arr = Arrow(LEFT, RIGHT)
        n = TextMobject("n"," ?")

        end.scale(0.7)
        eq.move_to(LEFT*2 + UP)
        pt.move_to(LEFT*2)
        end.move_to(LEFT*2 + DOWN)
        n.move_to(RIGHT*1.2 + UP*0.1)
        n[0].set_color(YELLOW)

        group = VGroup(eq, pt, end)
        braces = Brace(group, RIGHT)

        self.play(Write(eq))
        self.play(Write(pt))
        self.play(Write(end))
        self.play(GrowFromCenter(braces))
        self.play(Write(n))




class PlotSinCos(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : -1.5,
        "x_max" : 3*PI/2,
        "x_min" : -3*PI/2,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, # Don't write y axis label
        "x_axis_label": None,
    }
    def construct(self):
        self.setup_axes()
        plotSin = self.get_graph(lambda x : (x**3 + x + 1)**(0.5), 
                                    color = GREEN,
                                    x_min=-4,
                                    x_max=4,
                                )
        plotCos = self.get_graph(lambda x : np.cos(x), 
                                    color = GRAY,
                                    x_min=-PI,
                                    x_max=0,
                                )
        plotSin.set_stroke(width=3) # width of line
        plotCos.set_stroke(width=2)
        # Animation
        for plot in (plotSin,plotCos):
            self.play(
                    ShowCreation(plot),
                    run_time = 2
                )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(RED)
        self.y_axis.set_color(YELLOW)
        # Add x,y labels
        func = TexMobject("\\sin\\theta")
        var = TexMobject("\\theta")
        func.set_color(BLUE)
        var.set_color(PURPLE)
        func.next_to(self.y_axis,UP)
        var.next_to(self.x_axis,RIGHT+UP)
        # Y labels
        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1,1])
        #Parametters of x labels
        init_val_x = -3*PI/2
        step_x = PI/2
        end_val_x = 3*PI/2
        # List of the positions of x labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x)
        # List of tex objects
        list_x=TexMobject("-\\frac{3\\pi}{2}", #   -3pi/2
                            "-\\pi", #              -pi 
                            "-\\frac{\\pi}{2}", #   -pi/2
                            "\\,", #                 0 (space)
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\pi",#                 pi
                            "\\frac{3\\pi}{2}" #     3pi/2
                          )
        #List touples (position,label)
        values_x = [(i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            x_tex.scale(0.7)
            if x_val == -PI or x_val == PI: #if x is equals -pi or pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #Put 2*Down
            else: # In another case
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)

        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    self.x_axis_labels,
                    func,var
                ]
            ],
            run_time=2
        )


