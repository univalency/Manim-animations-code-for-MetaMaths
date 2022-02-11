#Code for this video: https://youtu.be/_CWSYu4mrY4
from big_ol_pile_of_manim_imports import *
from manimlib.mobject.coordinate_systems import ThreeDAxes

class tr(Scene):
    def construct(self):
        tr = Polygon(2*LEFT, 3.464*UP, 2*RIGHT, color = BLUE)
        h = Line(3.464*UP, DOWN*0.001, color= RED)
        two = TexMobject("2")
        height = TextMobject("a")
        h_equals = TexMobject("a^{2}\\, = (2sin(60^{\\circ}))^{2} \\, =","\\, 3")
        h_equals1 = TexMobject("a^{2}\\, =\\,"," 3")
        
        h_equals[1].set_color(RED)
        h_equals1[1].set_color(RED)

        two.move_to(1.7*UP + LEFT*1.35)
        height.move_to(1.4*UP + RIGHT*0.25)
        h_equals.move_to(DOWN)
        h_equals1.move_to(DOWN)

        self.play(ShowCreation(tr))
        self.play(Write(two))
        self.play(ShowCreation(h))
        self.play(Write(height))
        self.play(Write(h_equals[0]) )
        self.play(Write(h_equals[1]) )
        self.wait()
        self.play(Transform(h_equals, h_equals1))
        self.wait()


class rhombus(Scene):
    def construct(self):
    	sq = Polygon(1.5*LEFT, 1.5*LEFT+ 3*UP, 1.5*RIGHT + 3*UP, 1.5*RIGHT, color = BLUE)
    	diag = Line(LEFT*2.127 + 1.5*UP, RIGHT*2.127 + 1.5*UP )
    	h1 = Line(UP*3.6, UP*1.5)
    	h2 = Line(UP*1.5, DOWN*0.62)
    	
    	two = TexMobject("2")
    	a = TexMobject("a")
    	b = TexMobject("b")
    	equa = TexMobject("a^{2}\\, +", "\\, b^{2}\\, =","\\, 4" )


    	a.move_to(UP* 2.54 + RIGHT*0.3)
    	b.move_to(UP* 0.5  + RIGHT*0.3)
    	equa.move_to(DOWN*1.5)
    	
    	h1.set_color(RED)
    	h2.set_color(GREEN)
    

    	two.move_to(0.75*RIGHT + UP*0.5)

    	self.play(ShowCreation(sq))
    	self.play(Rotate(sq, angle = math.radians(45)))
    	self.play(ShowCreation(diag))
    	self.play(ShowCreation(h1))
    	self.play(ShowCreation(h2))
    	self.play(Write(a),Write(b))
    
    	self.play(FadeIn(equa[0]))
    	self.play(FadeIn(equa[1]))
    	self.play(Write(equa[2]))
    	self.wait()


class pentagon(Scene):
    def construct(self):
    	pentagon = Polygon(0.38199*LEFT + 1.17555*UP, 1.2361*LEFT, 0.38199*LEFT + 1.17555*DOWN, RIGHT + 0.7265*DOWN, RIGHT + 0.7265*UP, color = BLUE )
    	pentagon.scale(1.2)
    	diag = Line(1.425*LEFT + 0.578*UP, 1.35*RIGHT + 0.57*UP)
    	vert1 = Line(1.6*UP + LEFT*0.01, 0.578*UP)
    	vert2 = Line(0.578*UP, DOWN*1.1)
    	
    	vert1.set_color(RED)
    	vert2.set_color(GREEN)

    	a = TexMobject("a")
    	b = TexMobject("b")
    	equa = TexMobject("a^{2}\\, +", "\\, b^{2}\\, =","\\, 5" )

    	a.move_to(UP* 0.92 + RIGHT*0.23)
    	b.move_to(UP* 0.02  + RIGHT*0.23)
    	equa.move_to(DOWN*2)


    	self.play(ShowCreation(pentagon))
    	self.play(Rotate(pentagon, angle = math.radians(53.5)))
    	self.play(ShowCreation(diag))
    	self.play(ShowCreation(vert1), Write(a))
    	self.play(ShowCreation(vert2), Write(b))
    	

    	self.play(FadeIn(equa[0]))
    	self.play(FadeIn(equa[1]))
    	self.play(Write(equa[2]))
    	self.wait()

class hexagon(MovingCameraScene):
    def construct(self):
    	hexagon = Polygon(UP*3, 2.598*LEFT + 1.5*UP, 2.598*LEFT + 1.5*DOWN, 3*DOWN,
    	 2.598*RIGHT + 1.5*DOWN, 2.598*RIGHT + 1.5*UP, color = BLUE )

    	pentagon = Polygon(0.38199*LEFT + 1.17555*UP, 1.2361*LEFT, 0.38199*LEFT + 1.17555*DOWN, RIGHT + 0.7265*DOWN, RIGHT + 0.7265*UP, color = BLUE )
    	vertical = Line(3*UP, 3*DOWN)
    	h1 = DashedLine(2.598*LEFT + 1.5*UP, 2.598*RIGHT + 1.5*UP )
    	h2 = DashedLine(2.598*LEFT + 1.5*DOWN, 2.598*RIGHT + 1.5*DOWN )


    	a = TexMobject("v_{1}")
    	b = TexMobject("v_{2}")
    	c = TexMobject("v_{3}")
    	two = TexMobject("2")
    	summ = TexMobject("v_{1}^{2}\\, +\\, v_{2}^{2}\\, +\\, v_{3}^{2}\\, =\\, 6 ")
    	summ.move_to(DOWN*4.5)

    	a.move_to(2.25*UP + 0.3*LEFT)
    	b.move_to( 0.3*LEFT)
    	c.move_to(2.25*DOWN + 0.3*LEFT)
    	two.move_to(2.6*UP + 1.55*LEFT)


    	self.play(ShowCreation(hexagon))
    	self.play(Rotate(hexagon, angle = math.radians(360), run_time = 3))
    	self.play(ShowCreation(pentagon))
    	self.play(Rotate(pentagon, angle = math.radians(-360), run_time = 2))
    	self.play(Uncreate(pentagon), Write(two))
    	self.play(ShowCreation(vertical))
    	self.wait()
    	self.play(ShowCreation(h1), ShowCreation(h2))
    	self.play(Write(a), Write(b), Write(c))
    	self.camera_frame.save_state()
    	self.play(self.camera_frame.scale,1.2, self.camera_frame.move_to, DOWN)
    	self.play(Write(summ))

    	self.wait()

class threeShapes(Scene):
	def construct(self):
		tr = Polygon(2*LEFT, 3.464*UP, 2*RIGHT, color = BLUE)
		h = Line(3.464*UP, DOWN*0.001, color= RED)
		two = TexMobject("2")
		height = TexMobject("a")
		h_equals1 = TexMobject("a^{2}\\, =\\,"," 3")

		sq = Polygon(1.5*LEFT, 1.5*LEFT+ 3*UP, 1.5*RIGHT + 3*UP, 1.5*RIGHT, color = BLUE)
		diag = Line(LEFT*2.127 + 1.5*UP, RIGHT*2.127 + 1.5*UP )
		h1 = Line(UP*3.6, UP*1.5)
		h2 = Line(UP*1.5, DOWN*0.62)

		a = TexMobject("a")
		b = TexMobject("b")

		pentagon = Polygon(0.38199*LEFT + 1.17555*UP, 1.2361*LEFT, 0.38199*LEFT + 1.17555*DOWN, RIGHT + 0.7265*DOWN, RIGHT + 0.7265*UP, color = BLUE )
		pentagon.scale(1.2)
		diagg = Line(1.425*LEFT + 0.578*UP, 1.35*RIGHT + 0.57*UP)
		vert1 = Line(1.6*UP + LEFT*0.01, 0.578*UP)
		vert2 = Line(0.578*UP, DOWN*1.1)

		aa = TexMobject("a")
		bb = TexMobject("b")

		aa.scale(0.8)
		bb.scale(0.8)

		aa.move_to(UP* 0.92 + RIGHT*0.23)
		bb.move_to(UP* 0.02  + RIGHT*0.23)

		h_equals1[1].set_color(RED)
		two.move_to(1.7*UP + LEFT*1.35)
		height.move_to(1.4*UP + RIGHT*0.25)
		h_equals1.move_to(DOWN)


		a.move_to(UP* 2.54 + RIGHT*0.3)
		b.move_to(UP* 0.5  + RIGHT*0.3)

		vert1.set_color(RED)
		vert2.set_color(GREEN)

		h1.set_color(RED)
		h2.set_color(GREEN)

		gr = VGroup(tr, h, two, height)
		gr.move_to(LEFT*4 + UP)

		gr1 = VGroup(diag, h1, h2,a,b)

		gr2 = VGroup(pentagon, diagg,vert1, vert2,aa,bb)
		gr2.scale(1.3)
		gr2.move_to(RIGHT*4.8 + UP*0.8)

		tr_equals = TexMobject("a^{2}\\, =\\,"," 3")
		sq_equals = TexMobject("a^{2}\\, +", "\\, b^{2}\\, =","\\, 4" )
		pent_equals = TexMobject("a^{2}\\, +", "\\, b^{2}\\, =","\\, 5" )

		tr_equals[1].set_color(YELLOW)
		sq_equals[2].set_color(YELLOW)
		pent_equals[2].set_color(YELLOW)

		tr_equals.move_to(LEFT*4.2 + DOWN*2)
		sq_equals.move_to(DOWN*2)
		pent_equals.move_to(RIGHT*5 + DOWN*2)

		self.play(ShowCreation(gr))
		self.play(Rotate(sq, angle = math.radians(45)))
		self.play(ShowCreation(gr1))
		self.play(Rotate(pentagon, angle = math.radians(53.5)))
		self.play(ShowCreation(gr2))
		self.wait()
		self.play(Write(tr_equals))
		self.wait(0.5)
		self.play(Write(sq_equals))
		self.wait(0.5)
		self.play(Write(pent_equals))
		self.wait()
      
class tengon(MovingCameraScene):
	def construct(self):
		tengon = Polygon(UP, 0.617*LEFT + 0.8507*UP, LEFT + 0.325*UP, LEFT + 0.325*DOWN, 0.617*LEFT + 0.8507*DOWN, DOWN,
			0.617*RIGHT + 0.8507*DOWN, RIGHT + 0.325*DOWN, RIGHT + 0.325*UP, 0.617*RIGHT + 0.8507*UP )
		tengon.scale(3)

		tr1 = Polygon(UP*3, 1.82*RIGHT+UP*2.54, UP*2.52, color = YELLOW )
		tr2 = Polygon(1.851*RIGHT+UP*2.52, UP + RIGHT*3, 1.851*RIGHT+ UP, color = YELLOW)

		two1 = TexMobject("2")
		two2 = TexMobject("2")
		two3 = TexMobject("2")
		even = TextMobject("n - even")
		even.move_to(LEFT*5.5 + UP*3.2)
		box4 = SurroundingRectangle(even, color = RED, opacity = 0.2)
		even.scale(0.8)

		summ1 = TexMobject("v_{1}^{2}\\, +\\, v_{2}^{2}\\, =")
		summ2 = TexMobject("2^{2}sin(\\alpha_{1})^{2}\\, +\\, 2^{2}sin(\\alpha_{2})^{2}" )
		
		sin_identity = TexMobject("\\alpha_{4} \\, +\\, \\beta_{4}\\, =\\, \\pi")
		sin_identity1 = TexMobject("sin(\\alpha_{4})\\, = sin(\\beta_{4})")
		sin_identity2 = TexMobject("sin(\\alpha)\\, = sin(\\pi - \\alpha)")

		sin_identity.move_to(1.8*DOWN + RIGHT*4.5)
		sin_identity1.move_to(2.8*DOWN + RIGHT*4.5)
		sin_identity2.move_to(2.8*DOWN + RIGHT*4.5)

		sin_identity.scale(0.9)
		sin_identity1.scale(0.9)
		sin_identity2.scale(0.9)

		box2 = SurroundingRectangle(sin_identity2, color = RED, opacity = 0.8 )

		summ_tot = TexMobject("\\sum_{k=1}^{\\frac{n}{2}}v_{k}^{2}\\, =")
		summ_tot1 = TexMobject("\\sum_{k=1}^{\\frac{n}{2}}2^{2}sin(\\alpha_{k})^{2}")
		summ1.move_to(RIGHT*6 + UP*2.5)
		summ1.scale(0.9)
		summ_tot.move_to(RIGHT*6 + UP*2.5)
		summ_tot.scale(0.9)

		summ2.move_to(RIGHT*5.5 + UP*1.5)
		summ2.scale(0.8)
		summ_tot1.move_to(RIGHT*5.8 + UP*1.0)
		summ_tot1.scale(0.8)

		a = TexMobject("v_{1}")
		b = TexMobject("v_{2}")
		c = TexMobject("v_{3}")

		two1.move_to(1.0*RIGHT + 3.1*UP)
		two2.move_to(1.0*LEFT + 3.1*UP)
		two3.move_to(2.7*RIGHT + 1.9*UP)
		two1.scale(0.8)
		two2.scale(0.8)
		two3.scale(0.8)

		a.move_to(UP*2.7 + LEFT*0.22)
		b.move_to(UP*1.8 + RIGHT*1.63)
		c.move_to(LEFT*0.22)
		a.scale(0.7)
		b.scale(0.7)
		c.scale(0.7)

		h1 = Line(UP*2.52 + LEFT*1.85, UP*2.52 + RIGHT*1.85)
		h2 = Line(UP + LEFT*3,UP + RIGHT*3)
		h3 = Line(DOWN + LEFT*3,DOWN + RIGHT*3)
		h4 = Line(DOWN*2.52 + LEFT*1.85, DOWN*2.52 + RIGHT*1.85)

		h11 = DashedLine(UP*2.52 + LEFT*1.85, UP*2.52 + RIGHT*1.85, opacity = 0.3)
		h22 = DashedLine(UP + LEFT*3,UP + RIGHT*3, opacity = 0.3)
		h33 = DashedLine(DOWN + LEFT*3,DOWN + RIGHT*3, opacity = 0.3)
		h44 = DashedLine(DOWN*2.52 + LEFT*1.85, DOWN*2.52 + RIGHT*1.85, opacity = 0.3)
		
		v1 = Line(UP*3, UP*2.52)
		v2 = Line(UP*2.52, UP)
		v3 = Line(UP, DOWN)
		v4 = Line(DOWN, DOWN*2.52 )
		v5 = Line(DOWN*2.52, DOWN*3 )

		v11 = Line(3*UP, UP*2.52)
		v22 = Line(1.851*RIGHT+UP*2.52, 1.851*RIGHT+ UP)
		v33 = Line(UP, DOWN)
		v44 = Line(DOWN + 1.851*RIGHT, DOWN*2.52+1.851*RIGHT )
		v55 = Line(DOWN*2.52, DOWN*3 )

		arc1 = Arc(radius=0.8, start_angle= 2.9, angle = 0.28 , 
			 arc_center= [1.851, 2.5521, 0.])
		alpha1 = TexMobject("\\alpha_{1}")
		alpha1.next_to(arc1, LEFT*0.5)
		alpha1.scale(0.6)

		arc2 = Arc(radius=0.6, start_angle= 2.2, angle = 0.92 , 
			 arc_center= [3, 0.975, 0.])
		alpha2 = TexMobject("\\alpha_{2}")
		alpha2.next_to(arc2, LEFT*0.2)
		alpha2.scale(0.6)

		arc3 = Arc(radius=0.6, start_angle= 1.565, angle = 1.6 , 
			 arc_center= [3, -0.975, 0.])
		alpha3 = TexMobject("\\alpha_{3}")
		alpha3.next_to(arc3, LEFT*0.2)
		alpha3.scale(0.6)

		arc4 = Arc(radius=0.6, start_angle= 0.965, angle = 2.115 , 
			 arc_center= [1.851, -2.5521, 0.])
		alpha4 = TexMobject("\\alpha_{4}")
		alpha4.move_to(1.6*RIGHT + 1.75*DOWN)
		alpha4.scale(0.6)

		arc44 = Arc(radius=0.4, start_angle= 3.185, angle = 0.88 , 
			 arc_center= [3, -0.975, 0.], color = YELLOW)
		alpha44 = TexMobject("\\beta_{4}")
		alpha44.move_to(2.4*RIGHT + 1.25*DOWN)
		alpha44.scale(0.6)
		#18 degrees
		group1 = VGroup(a,b)


		angles = TexMobject("\\alpha_{1},\\alpha_{2},\\alpha_{3},..\\, ?")
		angles.move_to(RIGHT*6 + DOWN )

		box1 = SurroundingRectangle(angles, color = BLUE, opacity = 0.5 )

		internal = TexMobject("\\sum internal\\, angles\\, =\\, 180(n-2)")
		each_angle = TexMobject("\\gamma \\,= \\, \\frac{(n-2)}{n}180")
		alpha_1 = TexMobject("\\alpha_{1}\\, = \\frac{1}{2} \\left( \\pi\\, - \\frac{(n-2)}{n} \\right) \\pi")
		alpha_11 = TexMobject("\\alpha_{1}","\\, = \\frac{\\pi}{n} ")

		internal.move_to(RIGHT*5.5 + 2.5*UP)
		each_angle.move_to(RIGHT*6 + 1.5*UP)
		alpha_1.move_to(RIGHT*6 + 0.5*UP)
		alpha_11.move_to(RIGHT*6 + 0.5*UP)
		
		internal.scale(0.6)
		each_angle.scale(0.7)
		alpha_1.scale(0.7)
		alpha_11.scale(0.7)
		alpha_11[0].set_color(YELLOW)

		arc_gen = Arc(radius=0.4, start_angle= 5.285, angle = 2.58 , 
			 arc_center= [-3, -0.975, 0.], color = YELLOW)
		arc_genl = TexMobject("\\gamma")
		arc_genl.move_to(2.4*LEFT + 0.88*DOWN)
		arc_genl.scale(0.6)

		center = Dot(0.001*DOWN)
		l1 = Line(center, UP*3 )
		l2 = Line(center, UP*2.52 + RIGHT*1.85 )
		l3 = Line(center, UP*2.52 + LEFT*1.85 )
		l4 = Line(center, UP + LEFT*3 )
		l5 = Line(center, UP + RIGHT*3 )

		l6 = Line(center, DOWN + LEFT*3)
		l7 = Line(center, DOWN + RIGHT*3 )
		l8 = Line(center, DOWN*2.52 + RIGHT*1.85 )
		l9 = Line(center, DOWN*2.52 + LEFT*1.85)
		l10 = Line(center, DOWN*3)

		group2 = VGroup(tengon, l1,l2,l3,l4,l5,l6,l7,l8,l9,l10)


		

		v1.set_color(BLUE)
		v2.set_color(RED)
		v3.set_color(TEAL)
		v4.set_color(MAROON)
		v5.set_color(GOLD)

		v11.set_color(BLUE)
		v22.set_color(RED)
		v33.set_color(TEAL)
		v44.set_color(MAROON)
		v55.set_color(GOLD)

		self.play(ShowCreation(tengon))
		self.play(Write(even), ShowCreation(box4))
		self.play(Write(h1))
		self.play(Write(h2))
		self.play(Write(h3))
		self.play(Write(h4))
		self.play(Write(v1))
		self.play(Write(v2))
		self.play(Write(v3))
		self.play(Write(v4))
		self.play(Write(v5))
		self.play(Write(two1))
		self.play(Write(two2))

		self.play(Transform(v2,v22))
		self.play(Transform(v3,v33))

		self.camera_frame.save_state()
		self.play(self.camera_frame.scale,0.7, self.camera_frame.move_to, UP + RIGHT*2.5)

		self.play(Write(tr1))
		self.play(Write(tr2))
		self.play(Write(two3))
		self.play(Write(a),Write(b))


		self.play(Write(arc1), Write(alpha1))
		self.play(Write(arc2), Write(alpha2))
		self.play(Uncreate(tr1), Uncreate(tr2))
		self.play(Write(summ1))
		self.play(TransformFromCopy(group1, summ2))
		self.play(self.camera_frame.scale,1.2, self.camera_frame.move_to, UP*0.1 + RIGHT*2.4)
		self.play(Transform(summ1, summ_tot))
		self.play(Transform(summ2, summ_tot1))

		self.play(Write(arc3))
		self.play(self.camera_frame.scale,0.7, self.camera_frame.move_to, DOWN*1 + RIGHT*2.9)
		self.play(Transform(v4,v44))
		self.play(Write(arc4))

		self.play(Write(arc44))
		self.play(Write(alpha44),Write(alpha4))
		self.play(Write(sin_identity))
		self.play(Write(sin_identity2))
		self.play(Write(box2))
		self.play(ReplacementTransform(sin_identity2,sin_identity1))
		self.wait()
		self.play(self.camera_frame.scale,1.4, self.camera_frame.move_to, UP*0.1 + RIGHT*2.4)
		self.play(Uncreate(sin_identity),Uncreate(sin_identity1), Uncreate(box2))
		self.play(Write(alpha3))
		self.play(Write(angles))

		#the polygon is regualar so,,,

		self.play(Uncreate(summ1), Uncreate(summ2), Write(box1))
		self.play(Transform(h1,h11),Transform(h2,h22),Transform(h3,h33),Transform(h4,h44))
		self.play(ShowCreation(arc_gen), Write(arc_genl))
		self.play(Write(internal))
		self.play(Write(each_angle))
		self.play(Write(alpha_1))
		self.play(Transform(alpha_1, alpha_11))

		self.play(Uncreate(h1),Uncreate(h2),Uncreate(h3),Uncreate(h4),
			Uncreate(v1),Uncreate(v2),Uncreate(v3),Uncreate(v4),Uncreate(v5),
			Uncreate(two1),Uncreate(two2),Uncreate(two3), Uncreate(a), Uncreate(b),
			Uncreate(arc1),Uncreate(arc2),Uncreate(arc3),Uncreate(arc4),Uncreate(arc44),
			Uncreate(alpha1),Uncreate(alpha2),Uncreate(alpha3),Uncreate(alpha4),Uncreate(alpha44),
			Uncreate(arc_gen), Uncreate(arc_genl)  )

		self.play(Uncreate(internal),Uncreate(angles),Uncreate(box1),Uncreate(alpha_1),Uncreate(each_angle))

		self.play(Restore(self.camera_frame))



class transparent(MovingCameraScene):
	def construct(self):
		arc_gen = Arc(radius=0.4, start_angle= 5.285, angle = 2.58 , 
			 arc_center= [-3, -0.975, 0.], color = YELLOW)
		arc_genl = TexMobject("\\gamma")
		arc_genl.move_to(2.4*LEFT + 0.88*DOWN)
		arc_genl.scale(0.6)

		arc1 = Arc(radius=0.8, start_angle= 2.9, angle = 0.28 , 
			 arc_center= [1.851, 2.5521, 0.])
		alpha1 = TexMobject("\\alpha_{1}")
		alpha1.next_to(arc1, LEFT*0.5)
		alpha1.scale(0.6)

		arc2 = Arc(radius=0.6, start_angle= 2.2, angle = 0.92 , 
			 arc_center= [3, 0.975, 0.])
		alpha2 = TexMobject("\\alpha_{2}")
		alpha2.next_to(arc2, LEFT*0.2)
		alpha2.scale(0.6)

		hh1 = Line(UP*2.52 , UP*2.52 + RIGHT*1.85, color = YELLOW)
		hh2 = Line(1.851*RIGHT+ UP, UP + RIGHT*3, color = YELLOW)
		hh3 = Line(DOWN + 1.851*RIGHT, DOWN + RIGHT*3, color = YELLOW)

		self.play(ShowCreation(arc_gen), Write(arc_genl))
		self.play(ShowCreation(arc1), Write(alpha1))
		self.play(ShowCreation(arc2), Write(alpha2))
		self.play(Write(hh1))
		self.play(Write(hh2))
		self.play(Write(hh3))

class tengonRot(MovingCameraScene):
	def construct(self):
		tengon = Polygon(UP*3, 1.7634*LEFT + 2.427*UP, 2.8531*LEFT + 0.9269*UP,
			2.8529*LEFT + 0.9271*DOWN, 1.76304*LEFT + 2.4269*DOWN, 3*DOWN,
			1.76304*RIGHT + 2.4269*DOWN, 2.8529*RIGHT + 0.9271*DOWN, 2.8531*RIGHT + 0.9269*UP,
			 1.7634*RIGHT + 2.427*UP)

		alpha_11 = TexMobject("\\alpha_{1}","\\, = \\frac{\\pi}{n} ")

		alpha_11.move_to(RIGHT*6 + 3.5*UP)
		alpha_11.scale(1)

		alpha_22 = TexMobject("\\alpha_{2} \\, = \\frac{\\pi}{n} \\, +\\,"," \\frac{2\\pi}{n} ")

		alpha_22.move_to(RIGHT*6 + 2.2*UP)
		alpha_22.scale(1)

		general = TexMobject("\\alpha_{k} \\, = \\frac{\\pi}{n} +\\, \\frac{2\\pi}{n}k")
		general1 = TexMobject("\\alpha_{k} \\, = \\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right)")
		krange = TexMobject("k\\, =\\, 0,1,...,\\frac{n-2}{2}")

		general.move_to(RIGHT*6 )
		general1.move_to(RIGHT*6 )
		krange.move_to(RIGHT*6 + DOWN)
		krange.scale(0.8)

		gr = VGroup(general1, krange)
		box = SurroundingRectangle(gr, color = BLUE, opacity = 0.5)


		center = Dot(0.0001*DOWN)

		l1 = Line([0,0,0], UP*3)
		l2 = Line([0,0,0], 1.7634*LEFT + 2.427*UP)
		l3 = Line([0,0,0], 2.8531*LEFT + 0.9269*UP)
		l4 = Line([0,0,0], 2.8529*LEFT + 0.9271*DOWN)
		l5 = Line([0,0,0], 1.76304*LEFT + 2.4269*DOWN)
		l6 = Line([0,0,0], 3*DOWN)
		l7 = Line([0,0,0], 1.76304*RIGHT + 2.4269*DOWN)
		l8 = Line([0,0,0], 2.8529*RIGHT + 0.9271*DOWN)
		l9 = Line([0,0,0], 2.8531*RIGHT + 0.9269*UP)
		l10 = Line([0,0,0], 1.7634*RIGHT + 2.427*UP)

		arc3 = Arc(radius=0.8, start_angle= 1.6, angle = 0.57 , 
			 arc_center= [0, 0, 0.], color = YELLOW)
		alpha3 = TexMobject("\\frac{2\\pi}{n}")
		alpha3.move_to(UP*1.4 + LEFT*0.4)
		alpha3.set_color(RED)
		alpha3.scale(1)

		group2 = VGroup(tengon, l1,l2,l3,l4,l5,l6,l7,l8,l9,l10)

		h11 = DashedLine(1.7634*LEFT + 2.427*UP, 1.7634*RIGHT + 2.427*UP, opacity = 0.3)
		h22 = DashedLine(2.8531*LEFT + 0.9269*UP, 2.8531*RIGHT + 0.9269*UP, opacity = 0.3)


		self.play(ShowCreation(tengon))
		self.play(Write(center))
		self.play(ShowCreation(l1),ShowCreation(l2),ShowCreation(l3),
			ShowCreation(l4),ShowCreation(l5),ShowCreation(l6),
			ShowCreation(l7),ShowCreation(l8),ShowCreation(l9),ShowCreation(l10))
		self.play(Write(arc3))

		self.play(Rotate(group2, angle = math.radians(36)))
		self.play(Write(alpha3))
		self.wait()

		self.camera_frame.save_state()
		self.play(self.camera_frame.scale,0.9, self.camera_frame.move_to, UP + RIGHT*2.5)
		self.play(ShowCreation(h11))
		self.play(Write(alpha_11), Write(alpha_22[0]))
		self.play(TransformFromCopy(alpha3, alpha_22[1]))
		self.wait()
		self.play(ShowCreation(h22))
		self.wait()
		self.play(Write(general))
		self.play(Transform(general, general1))
		self.play(Write(krange))
		self.play(ShowCreation(box))
		self.wait()

class summ(MovingCameraScene):
	def construct(self):
		title = TextMobject("Sum of squares of vertical elements")
		title1 = TextMobject("Sum of squares of horizontal elements")
		title.to_edge(UP)
		title.scale(0.8)
		title1.scale(0.8)

		form1 = TexMobject("v_{1}^{2}\\, +\\, v_{2}^{2}\\, +\\, ...\\, + v_{k}^{2}\\, = ","\\, \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right)")
		form1.scale(0.8)

		form11 = TexMobject("v_{1}^{2}\\, +\\, v_{2}^{2}\\, +\\, ...\\, + v_{k}^{2}\\, = \\, \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right)")
		form11.scale(0.8)

		form111 = TexMobject(" \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right)")
		form111.scale(0.8)

		form11.move_to(UP*2)
		form111.move_to(UP*2)

		form2 = TexMobject("h_{1}^{2}\\, +\\, h_{2}^{2}\\, +\\, ...\\, + h_{k}^{2}\\, = ","\\, \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}cos^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right)")
		form2.scale(0.8)

		form22 = TexMobject("\\sum_{k=0}^{\\frac{n-2}{2}}2^{2}cos^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right)")
		form22.scale(0.8)
		form2.move_to(DOWN*1.3)
		form22.move_to(DOWN*1.3)

		summ = TexMobject("\\sum_{k=0}^{\\frac{n-2}{2}}2^{2}sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\, +\\, \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}cos^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) ")
		summ.move_to(UP*2.5)

		summ1 = TexMobject("\\sum_{k=0}^{\\frac{n-2}{2}}2^{2}\\left[ sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\, +\\, cos^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\right]")
		summ2 = TexMobject("\\sum_{k=0}^{\\frac{n-2}{2}}2^{2}","\\, =\\, 4 \\frac{n}{2}","\\, =\\,"," 2n")
		summ2[3].set_color(YELLOW)
		summ2.move_to(DOWN*2)
		
		box1 = SurroundingRectangle(title, color = GOLD)
		box2 = SurroundingRectangle(title1, color = GOLD)


		self.play(Write(title))
		self.play(ShowCreation(box1))
		self.play(Write(form1))
		self.play(ReplacementTransform(form1,form11))
		self.play(Write(title1))
		self.play(Write(form2))
		self.play(ShowCreation(box2))
		self.play(ReplacementTransform(form11,form111), ReplacementTransform(form2,form22))
		gr = VGroup(form22,form111)
		self.wait()
		self.play(Uncreate(box1),Uncreate(box2),Uncreate(title),Uncreate(title1))
		self.play(ReplacementTransform(gr, summ))
		self.play(Write(summ1))
		self.play(Write(summ2[0]))
		self.play(Write(summ2[1]))
		self.play(Write(summ2[2:4]))
		self.wait()


class claim(MovingCameraScene):
	def construct(self):
		claim = TexMobject("Claim:\\, \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}cos^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\, =\\,"," \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) ")
		claim.move_to(UP*2.5)
		claim.scale(0.8)

		claim1 = TexMobject("\\Leftrightarrow \\, \\, \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}\\left[ cos^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right)\\, -\\, sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\right]\\, =\\, 0 ")
		claim1.scale(0.8)

		double_angle = TexMobject("cos(2\\theta)\\, =\\, cos^{2}(\\theta)\\, -\\, sin^{2}(\\theta)")
		double_angle.scale(1)
		double_angle.move_to(DOWN*1.8)
		double_angle.set_color(YELLOW)

		claim2 = TexMobject("\\Leftrightarrow \\, \\, \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}\\left[ cos \\left(\\frac{2\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\right]\\, =\\, 0")
		claim2.move_to(DOWN*1.8)
		double_angle.scale(0.8)

		self.play(Write(claim[0]))
		self.play(Write(claim[1]))
		self.wait()
		self.play(Write(claim1))
		self.play(Write(double_angle))
		self.play(Transform(double_angle, claim2))
		self.wait()

class tengon1(MovingCameraScene):
	def construct(self):
		tengon = Polygon(UP, 0.617*LEFT + 0.8507*UP, LEFT + 0.325*UP, LEFT + 0.325*DOWN, 0.617*LEFT + 0.8507*DOWN, DOWN,
			0.617*RIGHT + 0.8507*DOWN, RIGHT + 0.325*DOWN, RIGHT + 0.325*UP, 0.617*RIGHT + 0.8507*UP )
		tengon.scale(3)


		two1 = TexMobject("2")
		two2 = TexMobject("2")
		two3 = TexMobject("2")
		summ1 = TexMobject("v_{1}^{2}\\, +\\, v_{2}^{2}\\, =")
		summ2 = TexMobject("2^{2}sin(\\alpha_{1})^{2}\\, +\\, 2^{2}sin(\\alpha_{2})^{2}" )
		
	

		

		summ_tot = TexMobject("\\sum_{k=1}^{\\frac{n}{2}}v_{k}^{2}\\, =")
		summ_tot1 = TexMobject("\\sum_{k=1}^{\\frac{n}{2}}2^{2}sin(\\alpha_{k})^{2}")
		summ1.move_to(RIGHT*6 + UP*2.5)
		summ1.scale(0.9)
		summ_tot.move_to(RIGHT*6 + UP*2.5)
		summ_tot.scale(0.9)

		summ2.move_to(RIGHT*5.5 + UP*1.5)
		summ2.scale(0.8)
		summ_tot1.move_to(RIGHT*5.8 + UP*1.0)
		summ_tot1.scale(0.8)

		a = TexMobject("v_{1}")
		b = TexMobject("v_{2}")
		c = TexMobject("v_{3}")

		aa = TexMobject("h_{1}")
		bb = TexMobject("h_{2}")
		cc = TexMobject("h_{3}")

		horsumm1 = TexMobject("h_{k}\\, =\\, 2 \\,cos(\\alpha_{k}) ")
		horsum2 = TexMobject("h_{k}\\, =\\, 2 cos(\\alpha_{k}) ")

		horsumm1.move_to(RIGHT*6 + UP*2.5)
		horsumm1.scale(0.9)


		two1.move_to(1.0*RIGHT + 3.1*UP)
		two2.move_to(1.0*LEFT + 3.1*UP)
		two3.move_to(2.7*RIGHT + 1.9*UP)
		two1.scale(0.8)
		two2.scale(0.8)
		two3.scale(0.8)

		a.move_to(UP*2.7 + LEFT*0.22)
		b.move_to(UP*1.8 + RIGHT*1.63)
		c.move_to(LEFT*0.22)
		a.scale(0.7)
		b.scale(0.7)
		c.scale(0.7)

		h1 = Line(UP*2.52 + LEFT*1.85, UP*2.52 + RIGHT*1.85)
		h2 = Line(UP + LEFT*3,UP + RIGHT*3)
		h3 = Line(DOWN + LEFT*3,DOWN + RIGHT*3)
		h4 = Line(DOWN*2.52 + LEFT*1.85, DOWN*2.52 + RIGHT*1.85)

		hh1 = Line(UP*2.52 , UP*2.52 + RIGHT*1.85, color = YELLOW)
		hh2 = Line(1.851*RIGHT+ UP, UP + RIGHT*3, color = YELLOW)
		hh3 = Line(DOWN + 1.851*RIGHT, DOWN + RIGHT*3, color = YELLOW)

		aa.next_to(hh1, DOWN*0.2)
		aa.scale(0.7)
		aa.set_color(GOLD)

		bb.next_to(hh2, DOWN*0.2)
		bb.scale(0.7)
		bb.set_color(GOLD)

		cc.next_to(hh3, DOWN*0.2)
		cc.scale(0.7)
		cc.set_color(GOLD)

		h11 = DashedLine(UP*2.52 + LEFT*1.85, UP*2.52 + RIGHT*1.85, opacity = 0.3)
		h22 = DashedLine(UP + LEFT*3,UP + RIGHT*3, opacity = 0.3)
		h33 = DashedLine(DOWN + LEFT*3,DOWN + RIGHT*3, opacity = 0.3)
		h44 = DashedLine(DOWN*2.52 + LEFT*1.85, DOWN*2.52 + RIGHT*1.85, opacity = 0.3)
		
		v1 = Line(UP*3, UP*2.52)
		v2 = Line(UP*2.52, UP)
		v3 = Line(UP, DOWN)
		v4 = Line(DOWN, DOWN*2.52 )
		v5 = Line(DOWN*2.52, DOWN*3 )

		v11 = Line(3*UP, UP*2.52)
		v22 = Line(1.851*RIGHT+UP*2.52, 1.851*RIGHT+ UP)
		v33 = Line(UP, DOWN)
		v44 = Line(DOWN + 1.851*RIGHT, DOWN*2.52+1.851*RIGHT )
		v55 = Line(DOWN*2.52, DOWN*3 )

		arc1 = Arc(radius=0.8, start_angle= 2.9, angle = 0.28 , 
			 arc_center= [1.851, 2.5521, 0.])
		alpha1 = TexMobject("\\alpha_{1}")
		alpha1.next_to(arc1, LEFT*0.5)
		alpha1.scale(0.6)

		arc2 = Arc(radius=0.6, start_angle= 2.2, angle = 0.92 , 
			 arc_center= [3, 0.975, 0.])
		alpha2 = TexMobject("\\alpha_{2}")
		alpha2.next_to(arc2, LEFT*0.2)
		alpha2.scale(0.6)

		arc3 = Arc(radius=0.6, start_angle= 1.565, angle = 1.6 , 
			 arc_center= [3, -0.975, 0.])
		alpha3 = TexMobject("\\alpha_{3}")
		alpha3.next_to(arc3, LEFT*0.2)
		alpha3.scale(0.6)

		arc4 = Arc(radius=0.6, start_angle= 0.965, angle = 2.115 , 
			 arc_center= [1.851, -2.5521, 0.])
		alpha4 = TexMobject("\\alpha_{4}")
		alpha4.move_to(1.6*RIGHT + 1.75*DOWN)
		alpha4.scale(0.6)

		arc44 = Arc(radius=0.4, start_angle= 3.185, angle = 0.88 , 
			 arc_center= [3, -0.975, 0.], color = YELLOW)
		alpha44 = TexMobject("\\beta_{4}")
		alpha44.move_to(2.4*RIGHT + 1.25*DOWN)
		alpha44.scale(0.6)
		#18 degrees
		group1 = VGroup(a,b)


		angles = TexMobject("\\alpha_{1},\\alpha_{2},\\alpha_{3},..\\, ?")
		angles.move_to(RIGHT*6 + DOWN )

		box1 = SurroundingRectangle(angles, color = BLUE, opacity = 0.5 )

		internal = TexMobject("\\sum internal\\, angles\\, =\\, 180(n-2)")
		each_angle = TexMobject("\\gamma \\,= \\, \\frac{(n-2)}{n}180")
		alpha_1 = TexMobject("\\alpha_{1}\\, = \\frac{1}{2} \\left( \\pi\\, - \\frac{(n-2)}{n} \\right) \\pi")
		alpha_11 = TexMobject("\\alpha_{1}","\\, = \\frac{\\pi}{n} ")

		internal.move_to(RIGHT*5.5 + 2.5*UP)
		each_angle.move_to(RIGHT*6 + 1.5*UP)
		alpha_1.move_to(RIGHT*6 + 0.5*UP)
		alpha_11.move_to(RIGHT*6 + 0.5*UP)
		
		internal.scale(0.6)
		each_angle.scale(0.7)
		alpha_1.scale(0.7)
		alpha_11.scale(0.7)
		alpha_11[0].set_color(YELLOW)

		arc_gen = Arc(radius=0.4, start_angle= 5.285, angle = 2.58 , 
			 arc_center= [-3, -0.975, 0.], color = YELLOW)
		arc_genl = TexMobject("\\gamma")
		arc_genl.move_to(2.4*LEFT + 0.88*DOWN)
		arc_genl.scale(0.6)

		center = Dot(0.001*DOWN)
		l1 = Line(center, UP*3 )
		l2 = Line(center, UP*2.52 + RIGHT*1.85 )
		l3 = Line(center, UP*2.52 + LEFT*1.85 )
		l4 = Line(center, UP + LEFT*3 )
		l5 = Line(center, UP + RIGHT*3 )

		l6 = Line(center, DOWN + LEFT*3)
		l7 = Line(center, DOWN + RIGHT*3 )
		l8 = Line(center, DOWN*2.52 + RIGHT*1.85 )
		l9 = Line(center, DOWN*2.52 + LEFT*1.85)
		l10 = Line(center, DOWN*3)

		group2 = VGroup(tengon, l1,l2,l3,l4,l5,l6,l7,l8,l9,l10)


		

		v1.set_color(BLUE)
		v2.set_color(RED)
		v3.set_color(TEAL)
		v4.set_color(MAROON)
		v5.set_color(GOLD)

		v11.set_color(BLUE)
		v22.set_color(RED)
		v33.set_color(TEAL)
		v44.set_color(MAROON)
		v55.set_color(GOLD)

		self.play(ShowCreation(tengon))
		self.play(Write(h1))
		self.play(Write(h2))
		self.play(Write(h3))
		self.play(Write(h4))
		self.play(Write(v1))
		self.play(Write(v2))
		self.play(Write(v3))
		self.play(Write(v4))
		self.play(Write(v5))
		self.play(Write(two1))
		self.play(Write(two2))

		self.play(Transform(v2,v22))
		self.play(Transform(v3,v33))

		self.camera_frame.save_state()
		self.play(self.camera_frame.scale,0.7, self.camera_frame.move_to, UP + RIGHT*2.6)


		self.play(Write(two3))
		self.play(Write(a),Write(b), Write(c))


		self.play(Write(arc1), Write(alpha1))
		self.play(Write(arc2), Write(alpha2))
	
		self.play(self.camera_frame.scale,1.2, self.camera_frame.move_to, UP*0.1 + RIGHT*2.4)
		

		self.play(Write(arc3))
		
		self.play(Transform(v4,v44))
		self.play(Write(arc4))
		self.play(Write(hh1))
		self.play(Write(hh2))
		self.play(Write(hh3))
		self.play(Write(aa),Write(bb),Write(cc))
		self.play(Write(horsumm1))
		self.wait()


class rootsOfUnity(GraphScene,MovingCameraScene):
    CONFIG = {
    "y_max" : 2,
    "y_min" : -2,
    "x_max" : 2, #2
    "x_min" : -2, #-2
    "y_tick_frequency" : 2,
    "x_tick_frequency" : 2,
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

        func_graph=self.get_graph(self.func_to_graph,x_min=1, x_max=1, color=BLUE)

        point1 = Dot(self.coords_to_point(-1,self.func_to_graph(-1)), radius = 0.08)
        point11 = Dot(self.coords_to_point(-1,self.func_to_graph(-1)), radius = 0.08, color= YELLOW)

        point2 = Dot(self.coords_to_point(1,self.func_to_graph(1)), radius = 0.08)
        point22 = Dot(self.coords_to_point(1,self.func_to_graph(1)), radius = 0.08, color = YELLOW)

        point3 = Dot(self.coords_to_point(0.5,self.func_to_graph(0.5)), radius = 0.08)
        point33 = Dot(self.coords_to_point(0.5,self.func_to_graph(0.5)), radius = 0.08, color = YELLOW)

        point4 = Dot(self.coords_to_point(-0.5,self.func_to_graph(-0.5)), radius = 0.08)
        point44 = Dot(self.coords_to_point(-0.5,self.func_to_graph(-0.5)), radius = 0.08, color =YELLOW)

        point5 = Dot(self.coords_to_point(-0.5,self.func_to_graph2(-0.5)), radius = 0.08)
        point55 = Dot(self.coords_to_point(-0.5,self.func_to_graph2(-0.5)), radius = 0.08, color = YELLOW)

        point6 = Dot(self.coords_to_point(0.5,self.func_to_graph2(0.5)), radius = 0.08)
        point66 = Dot(self.coords_to_point(0.5,self.func_to_graph2(0.5)), radius = 0.08, color = YELLOW)

        func_graph=self.get_graph(self.func_to_graph,x_min= -1, x_max= 1, color=BLUE)
        func_graph_2=self.get_graph(self.func_to_graph2,x_min= -1, x_max= 1, color=BLUE)

        

        claim2 = TexMobject("\\sum_{k=0}^{\\frac{n-2}{2}}2^{2}\\left[ cos \\left(\\frac{2\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\right]\\, =\\, 0")
        claim2.scale(0.5)

       

        claim4 = TexMobject("\\sum_{k=0}^{\\frac{n-2}{2}}2^{2}\\left[ cos \\left(\\frac{2\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\right]\\, +\\, i \\, \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}\\left[ sin \\left(\\frac{2\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\right]\\, =\\, 0")
        claim4.scale(0.5)

  
        claim4.move_to(LEFT*3.9 + DOWN*2)
        
        claim2.move_to(LEFT*4 + UP*2.5)
        box1 = SurroundingRectangle(claim2, color = RED)
        box2 = SurroundingRectangle(claim2, color = GREEN)

        complex_number = TexMobject("\\left[ ","cos \\left(\\frac{2\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right)\\, +\\, i\\, sin \\left(\\frac{2\\pi}{n}\\left( 1\\, +\\, 2k \\right)  \\right)","\\right]^{n}", "\\, =\\, 1" )
        complex_number.scale(0.7)
        complex_number.move_to(DOWN*2.5 + RIGHT*4.5)
       

        p1label=TexMobject("\\left(\\, cos \\left(\\frac{2\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right)\\, ,\\, sin \\left(\\frac{2\\pi}{n}\\left( 1\\, +\\, 2k \\right)  \\, \\right)")
        p1label.scale(0.6)
        p1label.set_color(YELLOW)
        p1label.next_to(point3,RIGHT)

        self.play(Write(claim2), Write(box1))
        self.play(ShowCreation(point2))
        self.play(ShowCreation(point3))
        self.play(ShowCreation(point4))
        self.play(ShowCreation(point1))
        self.play(ShowCreation(point5))
        self.play(ShowCreation(point6))
        self.play(ShowCreation(func_graph),ShowCreation(func_graph_2))
        self.play(FadeIn(p1label), ShowCreation(point33))

        self.camera_frame.save_state()
        self.play(self.camera_frame.scale,1.15, self.camera_frame.move_to, RIGHT*0.8)
        
        self.play(TransformFromCopy(p1label, complex_number[1]))
        self.play(Write(complex_number[2]) , Write(complex_number[0]))
        self.play(Write(complex_number[3]))

        self.play(ShowCreation(point44))
        self.play(ShowCreation(point11))
        self.play(ShowCreation(point55))
        self.play(ShowCreation(point66))
        self.play(ShowCreation(point22))
        self.play(Restore(self.camera_frame), Uncreate(complex_number))
        self.play(self.camera_frame.scale,0.8, self.camera_frame.move_to, claim4)
        self.play(Write(claim4))
        self.play(self.camera_frame.scale,1.2, self.camera_frame.move_to, box2)
        self.play(Write(box2))
        self.wait()
  
  




    def func_to_graph(self,x):
        return(np.sqrt(1 - x**2))

    def func_to_graph2(self,x):
        return(- np.sqrt(1 - x**2))
    	
class facts(MovingCameraScene):
	def construct(self):
		fact1 = TexMobject("\\sum_{k=0}^{\\frac{n-2}{2}}2^{2}sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\, +\\, \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}cos^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\, =\\, 2n")
		fact2 = TexMobject("\\sum_{k=0}^{\\frac{n-2}{2}}2^{2}cos^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) \\, =\\,"," \\sum_{k=0}^{\\frac{n-2}{2}}2^{2}sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right) ")
		result = TexMobject("\\sum_{k=0}^{\\frac{n-2}{2}}2^{2}sin^{2}\\left(\\frac{\\pi}{n}\\left( 1\\, +\\, 2k \\right) \\right)\\, =\\, n")
		
		fact1.scale(0.9)
		fact2.scale(0.9)
		result.scale(0.9)

		fact1.move_to(UP*2)
		result.move_to(DOWN*2)
		box = SurroundingRectangle(result, color = YELLOW)

		self.play(Write(fact1))
		self.wait(0.5)
		self.play(Write(fact2))
		self.wait(0.5)
		self.play(Write(result))
		self.wait(0.5)

		self.play(Write(box))
		self.wait()

class heptagon(MovingCameraScene):
	def construct(self):
		tengon = Polygon(3*UP, 2.3454*LEFT + 1.8705*UP, 2.9247*LEFT + 0.6673*DOWN, 1.3018*LEFT + 2.7026*DOWN,
		1.3012*RIGHT + 2.7028*DOWN, 2.92435*RIGHT + 0.6679*DOWN, 2.3454*RIGHT + 1.8697*UP )

		odd = TextMobject("n - odd ?")
		
		self.play(ShowCreation(tengon))
		self.wait()
		self.play(Write(odd))
		self.wait()
