#source code for animations in this video: https://youtu.be/KSC27j70z7o

from big_ol_pile_of_manim_imports import *
from manimlib.mobject.coordinate_systems import ThreeDAxes

class intro(MovingCameraScene):
    def construct(self):
    	ones = TexMobject("1\\, \\, \\,", "\\, \\, \\, -","1")
    	lesser = TextMobject("lesser")
    	greater = TextMobject("greater")

    	ratio1 = TexMobject("\\left( \\frac{lesser}{greater} \\right)" , "\\frac{-1}{1}\\,", "\\, =\\, ", "\\frac{1}{-1}", "\\left( \\frac{greater}{lesser} \\right)" )
    	ratio2 = TexMobject("\\left( \\frac{lesser}{greater} \\right)","\\,=\\,","\\left( \\frac{greater}{lesser} \\right)" )
    	ones.to_edge(UP)
    	ratio1.scale(2)
    	ratio1[0].scale(0.7)
    	ratio1[4].scale(0.7)

    	lesser.scale(0.6)
    	greater.scale(0.6)
    	greater.next_to(ones[0], DOWN)
    	lesser.next_to(ones[2], DOWN )
    	lesser.set_color(BLUE)
    	greater.set_color(GREEN)

    	self.camera_frame.save_state()
    	self.play(self.camera_frame.scale,0.4, self.camera_frame.move_to, ones, run_time = 3)

    	self.play(Write(ones[0]))
    	self.play(Write(ones[1:3]))
    	self.wait()

    	self.play(Restore(self.camera_frame))
    	self.play(FadeIn(lesser))
    	self.play(FadeIn(greater))

    	self.play(Write(ratio1[1]))
    	self.play(Write(ratio1[3]))
    	self.wait()
    	self.play(Write(ratio1[2]))
    	self.wait()
    	self.play(FadeIn(ratio1[0]))
    	self.play(FadeIn(ratio1[4]))
    	self.play(Transform(ratio1, ratio2))
    	self.wait()

class Leibniz(MovingCameraScene):
    def construct(self):
    	quote1 = TextMobject("The margin is too narrow")
    	quote2 = TextMobject("to solve this paradox")

    	quote2.next_to(quote1, DOWN)
    	quote1.set_color(YELLOW)
    	quote2.set_color(YELLOW)

    	self.play(Write(quote1))
    	self.play(Write(quote2))
    	self.wait()


class Arnault(MovingCameraScene):
    def construct(self):
        quote1 = TextMobject("I am not convinced")
        quote2 = TextMobject("to solve this paradox")

        
        quote1.set_color(YELLOW)
       

        self.play(Write(quote1))

        self.wait()

class Pascal(MovingCameraScene):
    def construct(self):
    	ratio2 = TexMobject("\\left( \\frac{lesser}{greater} \\right)","\\,=\\,","\\left( \\frac{greater}{lesser} \\right)" )
    	antoine = TextMobject("Antoine Arnauld")
    	pascal = TextMobject("Blaise Pascal")
    	
    	ratio2.scale(0.7)
    	ratio2.to_edge(UP)
    	antoine.move_to(DOWN*2.8 + LEFT*4)
    	pascal.move_to(DOWN*2.8 + RIGHT*4)
    	antoine.scale(0.9)
    	pascal.scale(0.9)

    	box1 = SurroundingRectangle(ratio2, color = BLUE, opacity = 0.1)

    	self.play(FadeIn(ratio2), ShowCreation(box1))
    	self.wait()
    	self.play(Write(antoine))
    	self.wait()
    	self.play(Write(pascal))
    	self.wait()

class euler(MovingCameraScene):
    def construct(self):
    	tit = TextMobject("Euler's argument")
    	rule = TextMobject("smaller denominator $\\longrightarrow $ bigger fraction")
    	more = TexMobject("(a \\, >\\, 0)")
    	more.set_color(BLUE)

    	frac = TexMobject("\\frac{a}{-2}", "\\,>\\,", " \\frac{a}{0}" ,"=\\,","\\infty")
    	frac[1].set_color(YELLOW)
    	frac.scale(2)
    



    	frac1 = TexMobject("\\frac{a}{2}")

    	frac2 = TexMobject("\\frac{a}{10}")
    	frac3 = TexMobject("\\frac{a}{50}")
    	frac4 = TexMobject("\\frac{a}{100}")
    	frac5 = TexMobject("\\frac{a}{150}")
    	frac6 = TexMobject("\\frac{a}{200}")

    	inf = TexMobject("\\frac{a}{0}\\,","=\\,","\\infty")
    	inf2 = TexMobject("\\frac{a}{0}\\,","=\\,","\\infty")
    	inf2.move_to(UP*2.5 + RIGHT*4.5)
    	inf2.scale(0.9)
    	box1 = SurroundingRectangle(inf2, color = GREEN)

    	frac1.scale(2)
    	frac2.scale(1.8)
    	frac3.scale(1.5)
    	frac4.scale(1.2)
    	frac5.scale(1)
    	frac6.scale(0.8)
    	inf.scale(2)
    	inf[2].set_color(RED)

    	tit.to_edge(UP)
    	more.next_to(tit, DOWN)
    	frac1.move_to(LEFT*1.2)
    	frac2.move_to(RIGHT*1.2)
    	frac3.move_to(RIGHT*1.2)
    	frac4.move_to(RIGHT*1.2)
    	frac5.move_to(RIGHT*1.2)
    	frac6.move_to(RIGHT*1.2)

    	more.scale(0.8)
    	rule.scale(0.5)
    	rule.move_to(LEFT*4.5 + UP*2.6)
    	box2 = SurroundingRectangle(rule, color = GREEN)



    	self.play(Write(tit))
    	self.play(Write(frac1), Write(frac2))
    	self.play(Transform(frac2, frac3), FadeIn(more))
    	self.play(Transform(frac2, frac4))
    	self.play(Transform(frac2, frac5))
    	self.play(Transform(frac2, frac6))
    	self.wait()
    	self.play(FadeOut(frac2), FadeOut(frac1))
    	self.play(Write(inf[0]))
    	self.play(Write(inf[1:3]))
    	self.wait()
    	self.play(Transform(inf, inf2), ShowCreation(box1))
    	self.play(Write(rule), ShowCreation(box2))
    	self.play(Write(frac[0]))
    	self.play(Write(frac[2:5]))
    	self.play(TransformFromCopy(rule, frac[1]))
    	self.wait()

class quest(Scene):
    def construct(self):
        ques = TexMobject("- \\,","\\times", "\\, -", "\\, =\\, \\,", "+")
        ques.scale(2)

        self.play(FadeIn(ques[0]))
        self.play(FadeIn(ques[1]))
        self.play(FadeIn(ques[2]))
        self.play(FadeIn(ques[3]))
        self.play(FadeIn(ques[4]))

        self.play(Rotate(ques[1], angle = math.radians(180)), run_time = 3 )

        self.wait()


class numberLine(GraphScene):
    def construct(self):
        axes = Axes((-3, 10))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))
     


class evolution(Scene):
    def construct(self):

        tex1 = TextMobject("Abstractify !")
        tit1 = TextMobject("Evolution of numbers")
        nat = TexMobject("\\mathbb{N}")
        integ = TexMobject("\\mathbb{Z}")
        rat = TexMobject("\\mathbb{Q}")
        irrat = TexMobject("\\mathbb{R}")
        compl = TexMobject("\\mathbb{C}")
        count = TextMobject("Counting")
        negquan = TextMobject("Negative","quantities")
        fracquan = TextMobject("Fractional","quantities")
        solv = TextMobject("Irrationals")
        solvc = TextMobject("Solving"," any equation")

        nat.move_to(LEFT*5 + UP)
        integ.move_to(LEFT*2.5 + UP)
        irrat.move_to(RIGHT*2.5 + UP)
        rat.move_to(UP)
        compl.move_to(RIGHT*5 + UP)
        count.next_to(nat, DOWN)
        negquan[0].next_to(integ, DOWN)
        negquan[1].next_to(negquan[0], DOWN)
        fracquan[0].next_to(rat, DOWN)
        fracquan[1].next_to(fracquan[0], DOWN)
        solv.next_to(irrat, DOWN*1.1)
        solvc[0].next_to(compl, DOWN)
        solvc[1].next_to(solvc[0], DOWN)
        nat.set_color(BLUE)
        integ.set_color(BLUE)
        rat.set_color(BLUE)
        irrat.set_color(BLUE)
        compl.set_color(BLUE)

        count.scale(0.7)
        negquan.scale(0.7)
        fracquan.scale(0.7)
        solv.scale(0.7)
        solvc.scale(0.7)
        tex1.scale(3)
        tit1.to_edge(UP)
        self.play(Write(tex1))
        self.wait()
        self.play(FadeOut(tex1), FadeIn(tit1))
        self.wait()
        self.play(FadeIn(nat))
        self.play(FadeIn(integ))
        self.play(FadeIn(rat))
        self.play(FadeIn(irrat))
        self.play(FadeIn(compl))
        self.play(FadeIn(count), FadeIn(negquan), FadeIn(fracquan), FadeIn(solv), FadeIn(solvc))
        self.wait()
        self.play(TransformFromCopy(count, negquan))
        self.wait()
        self.play(TransformFromCopy(negquan, fracquan))
        self.play(TransformFromCopy(fracquan, solv))
        self.play(TransformFromCopy(solv, solvc))
        self.wait()

class distrib(MovingCameraScene):
    def construct(self):
    	tit = TextMobject("Distributive property")
    	form = TexMobject("a(b\\, +\\, c)\\, = \\, ab \\, +\\, ac")
    	exp = TexMobject("2\\cdot (3\\, +\\, 5)\\, = \\, 2\\cdot 3 \\, +\\, 2\\cdot 5")
    	exp2 = TexMobject("-2\\cdot ","(-3\\, +\\, 5)\\, ", "= \\, -2\\cdot -3 \\,"," +\\, -2\\cdot 5")
    	exp22 = TexMobject("-2\\cdot"," (-3\\, +\\, 5)\\, ", "= \\, -6  \\,"," -\\, 10")
    	exp222 = TexMobject("-2\\cdot"," (2)\\,  ", "=\\, \\, -6  \\,"," -\\, 10")
    	exp2222 = TexMobject("-4\\, = ", " \\, -16")

    	exp3 = TexMobject("-2\\cdot ","(-3\\, +\\, 5)\\, ", "= \\, -2\\cdot -3 \\,"," +\\, -2\\cdot 5")
    	exp33 = TexMobject("-2\\cdot ","(2)\\, ", "= \\, 6 \\,"," -\\, 10")
    	exp333 = TexMobject("-4 ", "\\,=\\, -4")
    	exp33.move_to(DOWN)
    	exp333.move_to(DOWN*2)

    	minusm = TexMobject("-\\, \\times \\, -\\, =\\, ","\\, \\, -")
    	minusmq = TexMobject("-\\, \\times \\, -\\, =\\, "," ?")
    	minusmp = TexMobject("-\\, \\times \\, -\\, =\\, ","\\, \\, +")
    	two = TexMobject("2")

    	minusm.to_edge(DOWN)
    	minusm[1].set_color(RED)

    	minusmp.to_edge(DOWN)
    	minusmp[1].set_color(GREEN)

    	minusmq.to_edge(DOWN)
    	minusmq[1].set_color(RED)

    	tit.to_edge(UP)
    	form.move_to(UP*2.5)
    	form.scale(0.85)

    	box1 = SurroundingRectangle(form, color = BLUE, opacity = 0.5)
    

    	exp.scale(0.9)
    	exp2.scale(0.9)
    	exp22.scale(0.9)
    	exp222.scale(0.9)
    	exp2222.scale(0.9)

    	exp3.scale(0.9)
    	exp33.scale(0.9)
    	exp333.scale(0.9)

    	br1 = Brace(exp2[1], UP)
    	two.next_to(br1, UP)



    	self.play(Write(tit))
    	self.play(FadeIn(form), ShowCreation(box1))
    	self.play(Write(exp))
    	self.play(Write(minusmq))
    	self.play(FadeOut(exp), FadeIn(exp2[0:2]))
    	self.play(Transform(minusmq[1], minusm[1]))
    	self.play(Write(exp2[2:4]))
    	self.play(Transform(exp2[2] , exp22[2]))
    	self.play(Transform(exp2[3] , exp22[3]))
    	self.play(Write(br1), Write(two))
    	self.play(Transform(exp2, exp2222[0:2]), Uncreate(br1), Uncreate(two))
    	self.play(Transform(minusmq[1], minusmp[1]))
    	self.play(Transform(exp2, exp3))
    	self.play(Write(exp33))
    	self.play(Write(exp333))

    	self.play(Uncreate(exp33), Uncreate(exp333), Uncreate(exp2), Uncreate(tit),
    		Uncreate(box1), Uncreate(form))

    	self.camera_frame.save_state()
    	self.play(self.camera_frame.scale,1.2, self.camera_frame.move_to, minusmq, run_time = 3)
    	self.play(self.camera_frame.scale,0.7, self.camera_frame.move_to, minusmq, run_time = 3)
    


class barrier(MovingCameraScene):
    def construct(self):
        nat = TexMobject("\\mathbb{N}")
        integ = TexMobject("\\mathbb{Z}")
        rat = TexMobject("\\mathbb{Q}")
        irrat = TexMobject("\\mathbb{R}")
        compl = TexMobject("\\mathbb{C}")

        nat.move_to(LEFT*1.5 + UP)
        integ.move_to(UP*2)
        rat.move_to(RIGHT*1.5 + UP)
        irrat.move_to(RIGHT + DOWN)
        compl.move_to(LEFT + DOWN)

        gr  = VGroup(nat, integ, rat, irrat, compl)

        self.play(FadeIn(nat))
        self.play(FadeIn(integ))
        self.play(FadeIn(rat))
        self.play(FadeIn(irrat))
        self.play(FadeIn(compl))
        self.wait()
        self.play(Rotate(gr, angle = math.radians(270)), run_time = 4)

class barrier2(MovingCameraScene):
    def construct(self):
        plus = TexMobject("+")
        minus = TexMobject("-")
        mult = TexMobject("\\times")
        divide = TexMobject("/ ")

        binar = TextMobject("Binary operation")

        plus.scale(1.5)
        minus.scale(1.5)
        mult.scale(1.5)
        divide.scale(1.5)

        plus.move_to(UP*2.25 + LEFT)
        minus.next_to(plus, DOWN* 3)
        mult.next_to(minus, DOWN* 3)
        divide.next_to(mult, DOWN* 3)

        gr = VGroup(plus, minus, mult, divide)
        br = Brace(gr, RIGHT)

        binar.next_to(br, RIGHT)

        self.play(FadeIn(plus))
        self.play(FadeIn(minus))
        self.play(FadeIn(mult))
        self.play(FadeIn(divide))

        self.play(Write(br))

        self.play(FadeIn(binar))


class triangle(MovingCameraScene):
    def construct(self):
        tr = Polygon(2*LEFT, 3.464*UP, 2*RIGHT, color = BLUE)
        tr1 = Polygon(2*RIGHT, 2*LEFT, 3.464*UP, color = BLUE)
        tr2 = Polygon(2*RIGHT, 2*LEFT, 3.464*UP, color = BLUE)
        symm = TextMobject("Symmetries of a triangle")
        new = TextMobject("New transformation")
        new.scale(0.8)
        symm.to_edge(UP)

        two = TexMobject("2")
        three = TexMobject("3")
        plus = TexMobject("2\\, +\\, 3")


        tr.move_to(DOWN)
        tr1.scale(0.5)
        tr1.move_to(LEFT*4 + UP*1.5)

        tr2.scale(0.5)
        tr2.move_to(LEFT*4 + DOWN*1.5)


        arr1 = Arrow(tr1, RIGHT)
        arr2 = Arrow(LEFT*3 + DOWN*2, RIGHT)
        rotation = TextMobject("rotation")
        rotation.next_to(arr1, UP)
        rotation.scale(0.7)
        rotation.set_color(RED)

        refl = TextMobject("reflection")
        refl.scale(0.7)
        refl.next_to(arr2, DOWN)
        refl.set_color(RED)

        new.move_to(RIGHT*3)
        plus.move_to(RIGHT*3)
        box1 = SurroundingRectangle(symm, color = BLUE)

        two.move_to(LEFT*4 + UP*1.5)
        three.move_to(LEFT*4 + DOWN*1.5)

        self.play(ShowCreation(tr))
        self.play(Rotate(tr, angle = math.radians(120)), run_time = 2)
        self.wait()
        self.play(Uncreate(tr))
        self.wait()
        self.play(ShowCreation(tr1))
        self.play(Write(symm), ShowCreation(box1))
        self.play(ShowCreation(tr2))
        self.play(ShowCreation(arr1), ShowCreation(arr2))
        self.play(Write(refl), Write(rotation))
        self.play(Write(new))
        self.play(Write(two))
        self.play(Write(three))
        self.play(Transform(new, plus))
        self.wait()

class group(MovingCameraScene):
    def construct(self):
        group = TextMobject("Group")
        one = TexMobject("(\\, +\\,)")

        ring = TextMobject("Ring")
        two = TexMobject("(\\, +\\, , \\, \\times)")

        group.scale(2)
        group.move_to(UP)

        ring.scale(2)
        ring.move_to(UP)

        field = TextMobject("Field")
        three= TexMobject("(\\, +\\, , \\, \\times \\, ,\\, /)")

        field.scale(2)
        field.move_to(UP)

        one.set_color(GREEN)
        two.set_color(GREEN)
        three.set_color(GREEN)

        self.play(Write(group))
        self.play(Write(one))
        self.play(Transform(one, two))
        self.play(Transform(group, ring))

        self.wait()

        self.play(Transform(one, three))
        self.play(Transform(group, field))
        self.wait()

class triangle2(MovingCameraScene):
    def construct(self):
        tr = Polygon(2*LEFT, 3.464*UP, 2*RIGHT, color = BLUE)
        


        tr.move_to(DOWN)
       

       
        self.play(ShowCreation(tr))
        self.play(Rotate(tr, angle = math.radians(-120)), run_time = 2)
        self.wait()
