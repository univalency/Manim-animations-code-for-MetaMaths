#this code was used in this video: https://youtu.be/QOZQjpLz6WY

from big_ol_pile_of_manim_imports import *
from manimlib.mobject.coordinate_systems import ThreeDAxes

class Hex1(Scene):
    def construct(self):
        hexagon = Polygon(LEFT + 1.732*UP, RIGHT + 1.732*UP, 2*RIGHT, RIGHT+1.732*DOWN, LEFT+1.732*DOWN, LEFT*2)
        
        point = Dot(LEFT*0.2 + UP*0.6)

        triangle1 = Polygon(LEFT*0.988 + 1.732*UP, RIGHT*0.99 + 1.732*UP,LEFT*0.2 + UP*0.6, fill_opacity=0.5, color = RED)
        triangle2 = Polygon(RIGHT + 1.73*UP, 1.985*RIGHT, LEFT*0.2 + UP*0.6, fill_opacity=0.5,color = BLUE)
        triangle3 = Polygon(1.99*RIGHT, RIGHT+1.73*DOWN, LEFT*0.2 + UP*0.6,fill_opacity=0.5, color = RED)
        triangle4 = Polygon(0.99*RIGHT+1.732*DOWN, LEFT+1.732*DOWN,LEFT*0.2 + UP*0.6,fill_opacity=0.5, color = BLUE)
        triangle5 = Polygon(LEFT+1.732*DOWN, LEFT*2,LEFT*0.2 + UP*0.6, fill_opacity=0.5, color = RED)
        triangle6 = Polygon(LEFT*1.99,LEFT + 1.73*UP,LEFT*0.2 + UP*0.6, fill_opacity=0.5, color = BLUE)

        tex = TextMobject("Area(","Blue",") = Area(","Red", ")")
        tex[1].set_color(BLUE)
        tex[3].set_color(RED)
        tex.move_to(UP*2.5)
        
        self.play(ShowCreation(hexagon))
        self.play(ShowCreation(point))
        self.play(ShowCreation(triangle1))
        self.play(ShowCreation(triangle2))
        self.play(ShowCreation(triangle3))
        self.play(ShowCreation(triangle4))
        self.play(ShowCreation(triangle5))
        self.play(ShowCreation(triangle6))
        self.play(Write(tex))
        self.wait(2)


class Hex2(Scene):
    def construct(self):
        hexagon = Polygon(LEFT + 1.732*UP, RIGHT + 1.732*UP, 2*RIGHT, RIGHT+1.732*DOWN, LEFT+1.732*DOWN, LEFT*2)
        
        point = Dot(RIGHT*0.7 + DOWN*0.65)

        triangle1 = Polygon(LEFT + 1.732*UP, RIGHT + 1.732*UP,RIGHT*0.7 + DOWN*0.65, fill_opacity=0.5, color = RED)
        triangle2 = Polygon(RIGHT + 1.715*UP, 1.989*RIGHT, RIGHT*0.7 + DOWN*0.65, fill_opacity=0.5,color = BLUE)
        triangle3 = Polygon(1.982*RIGHT, RIGHT+1.732*DOWN, RIGHT*0.7 + DOWN*0.65,fill_opacity=0.5, color = RED)
        triangle4 = Polygon(RIGHT+1.732*DOWN, LEFT+1.732*DOWN,RIGHT*0.7 + DOWN*0.65,fill_opacity=0.5, color = BLUE)
        triangle5 = Polygon(LEFT+1.732*DOWN, LEFT*2,RIGHT*0.7 + DOWN*0.65, fill_opacity=0.5, color = RED)
        triangle6 = Polygon(LEFT*2,LEFT + 1.732*UP,RIGHT*0.7 + DOWN*0.65, fill_opacity=0.5, color = BLUE)

        diag = Polygon(LEFT + 1.732*UP,2*RIGHT, color = RED)
        
        self.play(ShowCreation(hexagon))
        self.play(ShowCreation(point))
        self.play(ShowCreation(triangle1))
        self.play(ShowCreation(triangle2))
        self.play(ShowCreation(triangle3))
        self.play(ShowCreation(triangle4))
        self.play(ShowCreation(triangle5))
        self.play(ShowCreation(triangle6))
        self.wait(2)

class Hex_coor(Scene):
    def construct(self):

        area = TextMobject("$area_{\\triangle}$ = $\\frac{1}{2}$ h $\\cdot$ base")
        a1 = TexMobject("a_{1}")
        a2 = TexMobject("a_{2}")
        a3 = TexMobject("a_{3}")
        summ = TexMobject("a_{1}\\,+\\, a_{2}\\, + \\,a_{3} \\, = \\, const")
        summ1 = TexMobject("a_{1}\\,+\\, a_{2}\\, + \\,a_{3} \\, = \\, \\frac{3}{2} h")

        hexagon = Polygon(LEFT + 1.732*UP, RIGHT + 1.732*UP, 2*RIGHT, RIGHT+1.732*DOWN, LEFT+1.732*DOWN, LEFT*2)
        hexagon_pale = Polygon(LEFT + 1.732*UP, RIGHT + 1.732*UP, 2*RIGHT, RIGHT+1.732*DOWN, LEFT+1.732*DOWN, LEFT*2,stroke_width=0.3)
        
        point = Dot(LEFT*0.2 + UP*0.6)

        triangle_line1 = Line(LEFT*3 + UP*1.732, RIGHT*3 + 1.732*UP)
        triangle_line2 = Line(RIGHT*3 + 1.732*UP, 3.468*DOWN)
        triangle_line3 = Line(3.468*DOWN, LEFT*3 + UP*1.732)


        line1 = Line(LEFT*0.2 + UP*0.6, LEFT + 1.732*UP)
        line2 = Line(LEFT*0.2 + UP*0.6, RIGHT + 1.732*UP)
        line3 = Line(LEFT*0.2 + UP*0.6, 2*RIGHT )
        line4 = Line(LEFT*0.2 + UP*0.6, RIGHT+1.732*DOWN)
        line5 = Line(LEFT*0.2 + UP*0.6, LEFT+1.732*DOWN)
        line6 = Line(LEFT*0.2 + UP*0.6, LEFT*2)

        side1 = Line(LEFT + 1.732*UP, RIGHT + 1.732*UP)
        side2 = Line(LEFT+1.732*DOWN, LEFT*2)

        height1 = Line(LEFT*0.2 + UP*0.6, LEFT*0.2 + 1.732*UP)
        height2 = Line(LEFT*0.2 + UP*0.6, RIGHT*1.13 + 1.47*UP)
        height3 = Line(LEFT*0.2 + UP*0.6, RIGHT*1.71 + 0.47*DOWN)
        height4 = Line(LEFT*0.2 + UP*0.6, LEFT*0.2 + 1.732*DOWN)
        height5 = Line(LEFT*0.2 + UP*0.6, LEFT*1.79 + 0.33*DOWN)
        height6 = Line(LEFT*0.2 + UP*0.6, LEFT*1.35 + 1.15*UP)

        height11 = Line(LEFT*0.2 + UP*0.6, LEFT*0.2 + 1.732*UP)
        height22 = Line(LEFT*0.2 + UP*0.6, RIGHT*1.13 + 1.47*UP)
        height33 = Line(LEFT*0.2 + UP*0.6, RIGHT*1.71 + 0.47*DOWN)
        height44 = Line(LEFT*0.2 + UP*0.6, LEFT*0.2 + 1.732*DOWN)
        height55 = Line(LEFT*0.2 + UP*0.6, LEFT*1.79 + 0.33*DOWN)
        height66 = Line(LEFT*0.2 + UP*0.6, LEFT*1.35 + 1.15*UP)

        height222 = Line(LEFT*0.2 + UP*0.6, RIGHT*1.13 + 1.47*UP,stroke_width=0.3)
        height444 = Line(LEFT*0.2 + UP*0.6, LEFT*0.2 + 1.732*DOWN,stroke_width=0.3)
        height666 = Line(LEFT*0.2 + UP*0.6, LEFT*1.35 + 1.15*UP,stroke_width=0.3)


        paral1 = Line(2.5*LEFT + 1.732*UP,2.5*RIGHT + 1.732*UP)
        paral2 = Line(2.5*LEFT + 1.732*DOWN,2.5*RIGHT + 1.732*DOWN)

        triangle1 = Polygon(LEFT*0.988 + 1.732*UP, RIGHT*0.99 + 1.732*UP,LEFT*0.2 + UP*0.6, fill_opacity=0.2, color = RED)
        triangle2 = Polygon(RIGHT + 1.73*UP, 1.985*RIGHT, LEFT*0.2 + UP*0.6, fill_opacity=0.2,color = BLUE)
        triangle3 = Polygon(1.99*RIGHT, RIGHT+1.73*DOWN, LEFT*0.2 + UP*0.6,fill_opacity=0.2, color = RED)
        triangle4 = Polygon(0.99*RIGHT+1.732*DOWN, LEFT+1.732*DOWN,LEFT*0.2 + UP*0.6,fill_opacity=0.2, color = BLUE)
        triangle5 = Polygon(LEFT+1.732*DOWN, LEFT*2,LEFT*0.2 + UP*0.6, fill_opacity=0.2, color = RED)
        triangle6 = Polygon(LEFT*1.99,LEFT + 1.73*UP,LEFT*0.2 + UP*0.6, fill_opacity=0.2, color = BLUE)

        diag1 = Line(LEFT*0.2 + UP*0.6,LEFT*3 + UP*1.732)
        diag2 = Line(LEFT*0.2 + UP*0.6,RIGHT*3 + 1.732*UP)
        diag3 = Line(LEFT*0.2 + UP*0.6,3.468*DOWN)

        triangle_int1 = Polygon(LEFT*0.2 + UP*0.6,LEFT*3 + UP*1.732,RIGHT*3 + 1.732*UP, fill_opacity = 0.2, color = GOLD_C)
        triangle_int2 = Polygon(LEFT*0.2 + UP*0.6,LEFT*3 + UP*1.732,3.458*DOWN,fill_opacity = 0.2, color = YELLOW_B)
        triangle_int3 = Polygon(LEFT*0.2 + UP*0.6,3.468*DOWN,RIGHT*3 + 1.732*UP,fill_opacity = 0.2, color = GOLD_E)

    
        area.move_to(UP*2.5)
        side1.set_color(YELLOW)
        side2.set_color(YELLOW)
        hexagon_pale.set_color(GREEN_A)

        a1.next_to(height11, LEFT*0.1)
        a2.move_to(RIGHT*0.8 + DOWN*0.2)
        a3.move_to(LEFT*0.9 + DOWN*0.16)
        summ.move_to(UP*2.5)
        summ1.move_to(UP*2.5)

        a1.scale(0.8)
        a2.scale(0.8)
        a3.scale(0.8)

        height1.set_color(TEAL_C)
        height2.set_color(GREEN_B)
        height3.set_color(GOLD_D)
        height4.set_color(MAROON_C)
        height5.set_color(PURPLE_A)
        height6.set_color(BLUE_E)

        height11.set_color(YELLOW)
        height22.set_color(YELLOW)
        height33.set_color(YELLOW)
        height44.set_color(YELLOW)
        height55.set_color(YELLOW)
        height66.set_color(YELLOW)

        height222.set_color(YELLOW_E)
        height444.set_color(YELLOW_E)
        height666.set_color(YELLOW_E)

        paral1.set_color(RED)
        paral2.set_color(RED)

        self.play(ShowCreation(hexagon))
        self.wait()
        self.play(ShowCreation(point))
        self.wait()
        self.play(ShowCreation(line1),ShowCreation(line2),ShowCreation(line3),ShowCreation(line4),ShowCreation(line5),ShowCreation(line6))
        self.wait()
        self.play(Write(area))
        self.wait()
        self.play(ShowCreation(side1),ShowCreation(side2))
        self.wait()
        self.play(Uncreate(side1),Uncreate(side2))
        self.wait()
        self.play(FadeOut(area))
        self.wait()
        self.play(ShowCreation(height1),ShowCreation(height2),ShowCreation(height3),ShowCreation(height4),ShowCreation(height5),ShowCreation(height6))
        self.wait()
        self.play(Uncreate(line1),Uncreate(line2),Uncreate(line3),Uncreate(line4),Uncreate(line5),Uncreate(line6))
        self.wait()
        self.play(ShowCreation(paral1),ShowCreation(paral2))
        self.wait()
        self.play(Uncreate(paral1),Uncreate(paral2))
        self.wait()

        #self.play(ShowCreation(triangle1),ShowCreation(triangle2),ShowCreation(triangle3),ShowCreation(triangle4),ShowCreation(triangle5),ShowCreation(triangle6))
        self.play(ReplacementTransform(height1,height11),ReplacementTransform(height2,height22),ReplacementTransform(height3,height33),
            ReplacementTransform(height4,height44),ReplacementTransform(height5,height55),ReplacementTransform(height6,height66))
        self.wait()
        self.play(ShowCreation(triangle1),ShowCreation(triangle2),ShowCreation(triangle3),ShowCreation(triangle4),ShowCreation(triangle5),ShowCreation(triangle6))
        self.wait()
        self.play(Write(a1),Write(a2),Write(a3))
        self.wait()
        self.play(Uncreate(triangle1),Uncreate(triangle2),Uncreate(triangle3),Uncreate(triangle4),Uncreate(triangle5),Uncreate(triangle6))
        self.wait()
        self.play(ReplacementTransform(height22,height222),ReplacementTransform(height44,height444),ReplacementTransform(height66,height666))
        self.wait()
        self.play(ShowCreation(triangle_line1))
        self.wait()
        self.play(ShowCreation(triangle_line2))
        self.wait()
        self.play(ShowCreation(triangle_line3))
        self.wait()
        self.play(ReplacementTransform(hexagon,hexagon_pale))
        self.wait()
        self.play(ShowCreation(diag1),ShowCreation(diag2),ShowCreation(diag3))
        self.wait()
        self.play(ShowCreation(triangle_int1),ShowCreation(triangle_int2),ShowCreation(triangle_int3))
        self.wait()
        self.play(Write(summ))
        self.wait()
        self.play(ReplacementTransform(summ,summ1))
        self.wait()
        self.play(Uncreate(summ1))
        self.wait()


       


class Hex_area(Scene):
    def construct(self):
        hexagon = Polygon(LEFT + 1.732*UP, RIGHT + 1.732*UP, 2*RIGHT, RIGHT+1.732*DOWN, LEFT+1.732*DOWN, LEFT*2)
        
        point_middle = Dot(LEFT*0.001 + UP*0.001)
        point_other = Dot(RIGHT*0.65 + UP*0.78)

        

        line1 = Line(DOWN*2.2, 2.2*UP, )
        line2 = Line(LEFT*2.4, RIGHT*2.4)

        vector = Vector([0.65,0.78,0])
        
        self.play(ShowCreation(hexagon))
        self.play(ShowCreation(point_middle))
        self.wait()
        self.play(ReplacementTransform(point_middle, point_other))
        self.wait()
        self.play(ShowCreation(line1),ShowCreation(line2))
        self.play(ShowCreation(vector))

class Hex_par(Scene):
    def construct(self):
        hexagon = Polygon(LEFT + 1.732*UP, RIGHT + 1.732*UP, 2*RIGHT, RIGHT+1.732*DOWN, LEFT+1.732*DOWN, LEFT*2)
        
        point = Dot(LEFT*0.2 + UP*0.6)

        triangle1 = Polygon(LEFT*0.988 + 1.732*UP, RIGHT*0.99 + 1.732*UP,LEFT*0.2 + UP*0.6, fill_opacity=0.5, color = RED)
        triangle2 = Polygon(RIGHT + 1.73*UP, 1.985*RIGHT, LEFT*0.2 + UP*0.6, fill_opacity=0.5,color = BLUE)
        triangle3 = Polygon(1.99*RIGHT, RIGHT+1.73*DOWN, LEFT*0.2 + UP*0.6,fill_opacity=0.5, color = RED)
        triangle4 = Polygon(0.99*RIGHT+1.732*DOWN, LEFT+1.732*DOWN,LEFT*0.2 + UP*0.6,fill_opacity=0.5, color = BLUE)
        triangle5 = Polygon(LEFT+1.732*DOWN, LEFT*2,LEFT*0.2 + UP*0.6, fill_opacity=0.5, color = RED)
        triangle6 = Polygon(LEFT*1.99,LEFT + 1.73*UP,LEFT*0.2 + UP*0.6, fill_opacity=0.5, color = BLUE)

        line1 = Polygon(2*LEFT + 1.732*UP, 2*RIGHT + 1.732*UP)
        
        self.play(ShowCreation(hexagon))
        self.play(ShowCreation(point))
        self.play(ShowCreation(triangle1))
        self.play(ShowCreation(triangle2))
        self.play(ShowCreation(triangle3))
        self.play(ShowCreation(triangle4))
        self.play(ShowCreation(triangle5))
        self.play(ShowCreation(triangle6))
        self.play(Write(tex))
        self.wait(2)
