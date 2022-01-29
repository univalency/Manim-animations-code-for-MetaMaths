from manimlib import *
from big_ol_pile_of_manim_imports import *
from manimlib.mobject.coordinate_systems import ThreeDAxes


class intro(Scene):
	def construct(self):
		eq = TexMobject("y\\, = \\, x^{2}\\, - \\,2x\\, +\\, 3")

		self.play(FadeIn(eq))
		self.wait(2)


class Parabola(GraphScene):
    CONFIG = {
    "y_max" : 5,
    "y_min" : 0,
    "x_max" : 5,
    "x_min" : 0,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 600,
    "y_axis_label": " ",
    "x_axis_label": " ",
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "axes_color" : "#000000"
    }
    def construct(self):
        self.graph_origin=1.5*LEFT+3*DOWN
        self.setup_axes(animate=True)
        parabola = self.get_graph(self.parabola,x_min= -0.4, x_max = 2.4, color=BLUE)
        self.play(ShowCreation(parabola))
        

    def parabola(self,x):
        return(x**2 - 2*x + 3)
   


   
class ExampleApproximation(GraphScene, MovingCameraScene):
	CONFIG = {
	"function" : lambda x : np.cos(x),
	"function_color" : BLUE,
	"taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
	lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
	"center_point" : 0,
	"approximation_color" : GREEN,
	"x_min" : -8,
	"x_max" : 8,
	"y_min" : -3,
	"y_max" : 3,
	"graph_origin" : ORIGIN ,
	#"x_labeled_nums" :range(-8,8,2),
	 
	}
	def construct(self):
		self.setup_axes(animate=True)
		func_graph = self.get_graph(
		self.function,
		self.function_color,
		)
		approx_graphs = [
		self.get_graph(
		f,
		self.approximation_color
		)
		for f in self.taylor
		]
		 
		term_num = [
		TexMobject("n = " + str(n),aligned_edge=TOP)
		for n in range(0,8)]
		[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]
		 
		term = TexMobject("")
		term.to_edge(BOTTOM,buff=SMALL_BUFF)
		 
		approx_graph = VectorizedPoint(
		self.input_to_graph_point(self.center_point, func_graph)
		)
		 
		self.play(
		ShowCreation(func_graph),
		)
		for n,graph in enumerate(approx_graphs):
			self.play(
			Transform(approx_graph, graph, run_time = 2),
			Transform(term,term_num[n])
			)
	
			



class eq(MovingCameraScene):
	def construct(self):
		eq0 = TexMobject("x^{2}\\, +\\, xy\\, +\\, y^{2}\\, =\\,"," 9")
		eq1 = TexMobject("x^{2}\\, +\\, xy\\, +\\, y^{2}\\, =\\,"," 9")
		eq2 = TexMobject("y^{2}\\, +\\, yz\\, +\\, z^{2}\\, =\\, ","16")
		eq3 = TexMobject("x^{2}\\, +\\, xz\\, +\\, z^{2}\\, =\\, ","25")
		find = TexMobject("xy\\, +\\, yz\\, +\\, xz\\, ?")


		eq14 = TexMobject("x^{2}\\, +\\, xy\\, +\\, y^{2}\\, =\\,"," 9")
		eq24 = TexMobject("y^{2}\\, +\\, yz\\, +\\, z^{2}\\, =\\, ","16")
		eq34 = TexMobject("x^{2}\\, +\\, xz\\, +\\, z^{2}\\, =\\, ","25")

		eq35 = TexMobject("x^{2}\\, +\\, xz\\, +\\, z^{2}\\, =\\, ","25")

		eq11 = TexMobject("x^{2}\\, =\\, 9  -\\, xy\\, -\\, y^{2}")
		eq111 = TexMobject("x \\, =\\, \\sqrt {9-\\,xy\\,-\\,y^{2}} ")

		costh = TextMobject("Cosine theorem")
		costh2 = TextMobject(" 'Generalised Pythagoras Theorem' ")

		eq1.move_to(UP*2 + LEFT*0.1)
		eq0.move_to(UP*2 + LEFT*0.1)
		eq11.move_to(UP*2 + LEFT*0.1)
		eq111.move_to(UP*2 + LEFT*0.1)
		eq14.move_to(UP*2 + LEFT*0.1)

		costh.move_to(UP*1.5)
		costh2.move_to(UP*1.5)

		tr1 = Polygon(2.5*LEFT + DOWN, 0.768*LEFT , 2.5*RIGHT + DOWN)
		l1 = TextMobject("a")
		l2 = TextMobject("b")
		l3 = TextMobject("c")
		arc = Arc(radius=0.3, start_angle= 3.74, angle = 2.2 , 
			 arc_center= [-0.768, 0, 0.])
		alpha = TexMobject("\\alpha")

		l1.move_to(1.85*LEFT + DOWN*0.4)
		l2.move_to(1.1*RIGHT + DOWN*0.33)
		l3.move_to(1.25*DOWN)
		alpha.next_to(arc, DOWN*0.5)
		alpha.set_color(YELLOW)

		l1.scale(0.8)
		l2.scale(0.8)
		l3.scale(0.8)
		alpha.scale(0.7)


		l11 = TextMobject("x")
		l22 = TextMobject("z")
		l33 = TextMobject("5")
		angle = TexMobject("120^{\\circ}")

		l11.move_to(1.85*LEFT + DOWN*0.4)
		l22.move_to(1.1*RIGHT + DOWN*0.33)
		l33.move_to(1.25*DOWN)
		angle.next_to(arc, DOWN*0.5)
		angle.set_color(YELLOW)

		l11.scale(0.8)
		l22.scale(0.8)
		l33.scale(0.8)
		angle.scale(0.7)


		cosine = TexMobject("c^{2}\\, = \\, a^{2}\\, -\\, 2ab\\cdot cos(\\alpha)\\, +\\, b^{2}")
		cosine2 = TexMobject("5^{2}\\, = \\, x^{2}\\, -\\, 2xz\\cdot cos(120)\\, +\\, z^{2}")
		cosine3 = TexMobject("25\\, = \\, x^{2}\\, +\\, xz\\, +\\, z^{2}")

		cosine.move_to(2.5*DOWN)
		cosine.scale(0.9)
		cosine2.move_to(2.5*DOWN)
		cosine2.scale(0.9)
		cosine3.move_to(2.5*DOWN)
		cosine3.scale(0.9)



		eq2.move_to(UP)
		eq24.move_to(UP)
		find.move_to(DOWN)

		eq35.move_to(UP*2.8)
		box1 = SurroundingRectangle(eq35, color = BLUE)

		eq1.scale(0.9)
		eq0.scale(0.9)
		eq11.scale(0.9)
		eq111.scale(0.9)
		eq2.scale(0.9)
		eq3.scale(0.9)
		eq35.scale(0.9)

		eq14.scale(0.9)
		eq24.scale(0.9)
		eq34.scale(0.9)

		find.set_color(YELLOW)
		eq14[1].set_color(BLUE)
		eq24[1].set_color(BLUE)
		eq34[1].set_color(BLUE)

		gr = Group(eq1,eq2,eq3)
		br = Brace(gr, LEFT)

		self.play(FadeIn(eq1))
		self.play(FadeIn(eq2))
		self.play(FadeIn(eq3))
		self.play(Write(br))
		self.play(Write(find))
		self.wait()

		self.play(ReplacementTransform(eq1,eq11))
		self.wait()
		self.play(ReplacementTransform(eq11,eq111))
		self.wait()
		self.play(ReplacementTransform(eq111,eq0))
		self.wait()

		self.camera_frame.save_state()
		self.play(self.camera_frame.scale,.6, self.camera_frame.move_to, gr)
		self.wait()
		self.play(ReplacementTransform(eq0[1],eq14[1]) , 
				  ReplacementTransform(eq2[1],eq24[1]) ,
				  ReplacementTransform(eq3[1],eq34[1]) )
		self.wait()
		self.play(Restore(self.camera_frame))
		self.wait()
		self.play(ReplacementTransform(eq34,eq35), FadeOut(br), FadeOut(find),
			FadeOut(eq0), FadeOut(eq2), FadeOut(eq3),
			FadeOut(eq14[1]), FadeOut(eq24[1]), FadeOut(eq34[1]))

		self.wait()
		self.play(Write(box1))
		self.wait()

		self.play(ShowCreation(tr1), Write(costh))
		self.wait()
		self.play(Write(l1),Write(l2),Write(l3),Write(arc), Write(alpha))
		self.wait()
		self.play(ReplacementTransform(costh, costh2))
		self.wait()
		self.play(Write(cosine))
		self.wait()
		self.play(ReplacementTransform(l1, l11),
				  ReplacementTransform(l2, l22),
				  ReplacementTransform(l3,l33)
				  )
		self.wait()
		self.play(ReplacementTransform(alpha,angle),
			      ReplacementTransform(cosine,cosine2))
		self.play(ReplacementTransform(cosine2,cosine3))
		self.wait(2)



class part3(Scene):
	def construct(self):
		eq1 = TexMobject("x^{2}\\, +\\, xy\\, +\\, y^{2}\\, =\\,"," 9")
		eq2 = TexMobject("y^{2}\\, +\\, yz\\, +\\, z^{2}\\, =\\, ","16")
		eq3 = TexMobject("x^{2}\\, +\\, xz\\, +\\, z^{2}\\, =\\, ","25")
		find = TexMobject("xy\\, +\\, yz\\, +\\, xz\\, ?")

		repl = TexMobject("t\\, =\\, -\\, y")


		eq11 = TexMobject("x^{2}\\, -\\, xt\\, +\\, t^{2}\\, =\\,"," 9")
		eq22 = TexMobject("t^{2}\\, -\\, tz\\, +\\, z^{2}\\, =\\, ","16")
		eq33 = TexMobject("x^{2}\\, +\\, xz\\, +\\, z^{2}\\, =\\, ","25")

		tr1 = Polygon(1.5*LEFT, 0.634*LEFT + UP*0.5, 1.5*RIGHT)
		tr2 = Polygon(2*LEFT, 1.134*LEFT + UP*0.5, 2*RIGHT )
		tr3 = Polygon(2.5*LEFT + DOWN, 0.768*LEFT , 2.5*RIGHT + DOWN)

		arr = Arrow(LEFT + UP*0.5, RIGHT + UP*0.5)

		eq1.set_color(BLUE)
		eq2.set_color(RED)
		eq3.set_color(GREEN)

		eq11.set_color(BLUE)
		eq22.set_color(RED)
		eq33.set_color(GREEN)

		eq1.move_to(UP*2)
		eq2.move_to(UP)
		eq11.move_to(UP*2)
		eq22.move_to(UP)
		find.move_to(DOWN)
		repl.scale(0.8)
		repl.set_color(YELLOW)
		repl.next_to(arr, DOWN)

		group = VGroup(eq1,eq2,eq3)
		group2 = VGroup(eq11,eq22,eq33)
		group1 = VGroup(eq1,eq2,eq3, find)

		group.scale(0.9)
		group2.scale(0.9)

		group1.move_to(LEFT*3)
		group2.move_to(RIGHT*3.5 + UP*0.5)

		braces = Brace(group, LEFT)
		braces2 = Brace(group2, LEFT)

		tr1.move_to(RIGHT*3 + UP*2.1)
		tr2.move_to(RIGHT*3.5 + UP*0.7)
		tr3.move_to(RIGHT*4 + DOWN*0.8)

		tr1.set_color(BLUE)
		tr2.set_color(RED)



		self.play(FadeIn(group1),FadeIn(braces))
		self.wait()
		self.play(FadeIn(tr1),FadeIn(tr2),FadeIn(tr3))
		self.wait()

		self.play(Uncreate(tr1), Uncreate(tr2), Uncreate(tr3))
		self.wait()
		self.play(Write(arr))
		self.wait()
		self.play(Write(repl))
		self.wait()
		self.play(ShowCreation(group2), Write(braces2))
		self.wait()

class secondTriangle(Scene):
	def construct(self):

		form = TexMobject("\\frac{1}{2}\\, xt\\, sin(60)", "\\, +\\,", "\\frac{1}{2}\\, zt\\, sin(60)",
			"\\, -\\, ", "\\frac{1}{2}\\, xz\\, sin(120)", "\\, =\\, 6")
		form2 = TexMobject("\\sqrt 3 (xt\\, +\\, zt\\, -\\, xz)\\, =\\, 6")
		form3 = TexMobject("-\\,xt\\, -\\, tz\\, +\\, xz\\, =\\, -8\\sqrt 3")

		change = TexMobject("xy\\, +\\, yz\\, +\\, xz\\, ","\\longrightarrow","-\\,xt\\, -\\, tz\\, +\\, xz\\, ")
		change.move_to(DOWN*3)
		change.scale(0.8)

		form.move_to(DOWN*2)
		form.scale(0.9)

		form2.move_to(DOWN*2)
		form2.scale(0.9)

		form3.move_to(DOWN*2)
		form3.scale(0.9)

		tr1 = Polygon(2*LEFT, 2*LEFT + UP*3, 2*RIGHT + 3*UP)
		tr2 = Polygon(2*LEFT, 2*RIGHT + 3*UP, 0.17*RIGHT)
		tr11 = Polygon(2*LEFT, 2*LEFT + UP*3, 2*RIGHT + 3*UP, fill_opacity = 0.7, color = YELLOW)
		dot = Dot(0.17*RIGHT)
		l1 = Line(dot, 2*LEFT)
		l2 = Line(dot, 2*RIGHT + 3*UP)
		l3 = DashedLine(dot, 2*LEFT + 3*UP)

		arc = Arc(radius=0.2, start_angle= 2, angle = 1.2 , 
			 arc_center= [0.17, 0, 0])

		x = TexMobject("x")
		z = TexMobject("z")
		t = TexMobject("t")
		sixty = TexMobject("60^{\\circ}")

		x.scale(0.8)
		z.scale(0.8)
		t.scale(0.8)

		x.move_to(0.985*LEFT + DOWN*0.2)
		z.move_to(1.5*UP + RIGHT*1.26)
		t.move_to(1.6*UP + LEFT*0.6)
		sixty.move_to(LEFT*0.2 + UP*0.2)
		sixty.scale(0.6)
		sixty.set_color(YELLOW)
		three = TexMobject("3")
		three.move_to(2.2*LEFT + UP*1.5)
		four = TexMobject("4")
		four.move_to(UP*3.2)
		five = TexMobject("5")
		five.move_to(1.25*UP)
		three.scale(0.8)
		four.scale(0.8)
		five.scale(0.8)

		self.play(ShowCreation(tr1))
		self.wait()
		self.play(ShowCreation(dot), Write(l1),Write(l2), Write(x),Write(z),Write(t) )
		self.play(ShowCreation(l3), Write(three), Write(four), Write(five), Write(arc), Write(sixty))
		self.wait()
		self.play(Transform(tr1, tr11))
		self.wait()
		self.play(Write(form[0:3]))
		self.wait()
		self.play(TransformFromCopy(tr2, form[3:5] ))
		self.wait()
		self.play(TransformFromCopy(tr1, form[5]))
		self.wait()
		self.play(Write(change))
		self.wait()
		self.play(Transform(form, form2))
		self.wait()
		self.play(Transform(form, form3))
		self.wait()



class variables(Scene):
	def construct(self):
		var = TexMobject("\\, x\\, \\,", "\\,z\\, \\,", "\\, y\\,")
		varp = TexMobject("\\, x\\, \\,", "\\, z\\, \\,", "\\, y\\,")
		varpp = TexMobject("\\, x\\, \\,", "\\, z\\, \\,", "\\, y\\,")
		varn = TexMobject("\\, x\\, \\,", "\\, z\\, \\,", "\\, y\\,")
		
		var.scale(1.4)
		varp.scale(1.4)
		varpp.scale(1.4)
		varn.scale(1.4)

		varp.set_color(GREEN)
		varpp.set_color(GREEN)
		varn.set_color(RED)

		box = SurroundingRectangle(var, color = BLUE, opacity = 0.5 )

		self.play(Write(var), FadeIn(box))
		self.wait()
		self.play(Transform(var, varp))
		self.wait()
		self.play(Transform(varp, varn))
		self.wait()

		self.play(Transform(varn[0:2], varpp[0:2]))
		self.wait()

class variables2(Scene):
	def construct(self):
		var = TexMobject("\\, x\\, \\,", "\\,z\\, \\,", "\\, y\\,")
		varp = TexMobject("\\, x\\, \\,", "\\, z\\, \\,", "\\, y\\,")
		varpp = TexMobject("\\, x\\, \\,", "\\, z\\, \\,", "\\, y\\,")
		varn = TexMobject("\\, x\\, \\,", "\\, z\\, \\,", "\\, y\\,")
		
		var.scale(1.4)
		varp.scale(1.4)
		varpp.scale(1.4)
		varn.scale(1.4)

		varp.set_color(GREEN)
		varpp.set_color(GREEN)
		varn.set_color(RED)

		box = SurroundingRectangle(varp, color = BLUE, opacity = 0.5 )

		self.play(Write(varp), FadeIn(box))
		self.wait()
		self.play(Transform(varp[0], varn[0]))
		self.wait()
		self.play(Transform(varp[1], varn[1]), Transform(varp[0], varpp[0]))
		self.wait()

class angle(Scene):
	def construct(self):
		arc = Arc(radius=0.2, start_angle= 3.74, angle = 2.2 , 
			 arc_center= [-0.768, 0, 0.])
		circ = Arc(radius=0.4, start_angle= 0, angle = 6.5 )
		self.play(Write(arc))
		self.play(ShowCreation(circ))
		self.wait()


class part2(MovingCameraScene):
	def construct(self):

		eq1 = TexMobject("x^{2}\\, +\\, xy\\, +\\, y^{2}\\, =\\,"," 9")
		eq2 = TexMobject("y^{2}\\, +\\, yz\\, +\\, z^{2}\\, =\\, ","16")
		eq3 = TexMobject("x^{2}\\, +\\, xz\\, +\\, z^{2}\\, =\\, ","25")
		find = TexMobject("xy\\, +\\, yz\\, +\\, xz\\, ?")
		sine_formula = TexMobject("\\frac{1}{2}sin(120^{\\circ})\\,","(xy\\,  +\\, yz\\, +\\, xz)","\\, =\\, 6")
		equals = TexMobject("xy\\,  +\\, yz\\, +\\, xz\\, =\\, 8\\sqrt 3")


		sine_formula.move_to(UP*2.5 + RIGHT*2.5)
		equals.move_to(RIGHT*2.8 + UP*1.5)
		sine_formula.scale(0.9)
		equals.scale(0.9)

		box_equals = SurroundingRectangle(equals, color = BLUE)

		tr1 = Polygon(1.5*LEFT, 0.634*LEFT + UP*0.5, 1.5*RIGHT)
		tr2 = Polygon(2*LEFT, 1.134*LEFT + UP*0.5, 2*RIGHT )
		tr3 = Polygon(2.5*LEFT + DOWN, 0.768*LEFT , 2.5*RIGHT + DOWN)

		bigtr = Polygon(1.5*LEFT + DOWN, 1.5*LEFT + 3*UP, 1.5*RIGHT + DOWN )
		start = (-0.4, 0,0)
		tr11 = Polygon(1.5*LEFT + DOWN, 1.5*LEFT + 3*UP, start, fill_opacity=0.8, color = RED )
		tr22 = Polygon(1.5*LEFT + 3*UP, 1.5*RIGHT + DOWN, start, fill_opacity=0.8, color = GREEN )
		tr33 = Polygon(1.5*RIGHT + DOWN, start, 1.5*LEFT + DOWN, fill_opacity=0.8, color = BLUE  )

		tr111 = Polygon(1.5*LEFT + DOWN, 1.5*LEFT + 3*UP, start, fill_opacity=0.4, color = RED )
		tr222 = Polygon(1.5*LEFT + 3*UP, 1.5*RIGHT + DOWN, start, fill_opacity=0.4, color = GREEN )
		tr333 = Polygon(1.5*RIGHT + DOWN, start, 1.5*LEFT + DOWN, fill_opacity=0.4, color = BLUE  )

		three = TextMobject("3")
		four = TextMobject("4")
		five = TextMobject("5")

		fermat = TextMobject("Fermat point")
		fermat.set_color(YELLOW)
		fermat.scale(0.5)
		
		
		three.move_to(DOWN*1.25)
		four.move_to(1.7*LEFT + UP)
		five.move_to(UP*1.3 + RIGHT*0.1)
		
		three.scale(0.8)
		four.scale(0.8)
		five.scale(0.8)
		
		end1 = (-1.5, 3, 0)
		end2 = (-1.5, -1, 0)
		end3 = (1.5, -1, 0)

		p1 = Dot(0.4*LEFT )
		p11 = Dot(0.4*LEFT )
		p11.set_color(YELLOW)
		fermat.next_to(p1, DOWN)
		line1 = Line(start,end1)
		line2 = Line(start,end2)
		line3 = Line(start,end3)

		perp1 = DashedLine(start, 1.5*LEFT)
		perp2 = DashedLine(start, DOWN + 0.4*LEFT)
		perp3 = DashedLine(start, RIGHT*0.35 + 0.5625*UP)

		start2 = (2.4, 0, 0)
		start3 = (4.4, 0.5, 0)
		start4 = (5, -0.2, 0)

		end11 = (3.5, 0, 0)
		end22 = (4.4, -0.5, 0)
		end33 = (5.75, 0.3625, 0)

		perp11 = DashedLine(start2, end11 )
		perp22 = DashedLine(start3, end22 )
		perp33 = DashedLine(start4, end33 )

		starttot = (2.4, 0, 0)
		endtot = (5.379 , 0 , 0)

		linetot = DashedLine(starttot, endtot)
		linetot.set_color(YELLOW)
		minimal = TextMobject("minimal !")

		minimal.next_to(linetot, DOWN)

		groupperp = VGroup(perp11, perp22, perp33)

		eq1.set_color(BLUE)
		eq2.set_color(RED)
		eq3.set_color(GREEN)
		find.set_color(YELLOW)
		tr1.set_color(BLUE)
		tr2.set_color(RED)

		eq1.move_to(UP*2)
		eq2.move_to(UP)
		find.move_to(DOWN)

		group = VGroup(eq1,eq2,eq3)
		group1 = VGroup(eq1,eq2,eq3, find)
		grouptr = VGroup(tr1, tr2, tr3)

		groupbig = VGroup(bigtr, tr111, tr222, tr333, p11, perp1, perp2, perp3, three, four, five,
			line1, line2, line3)


		group.scale(0.9)
		group1.move_to(LEFT*3)

		tr1.move_to(RIGHT*3 + UP*2.1)
		tr2.move_to(RIGHT*3.5 + UP*0.7)
		tr3.move_to(RIGHT*4 + DOWN*0.8)

		group_sides = VGroup(three, four)


		braces = Brace(group, LEFT)
		l1 = Line(groupbig.get_center(), LEFT*2 + UP*0.8)

		self.play(Write(group1), Write(braces))
		self.play(TransformFromCopy(eq1,tr1))
		self.play(TransformFromCopy(eq2,tr2))
		self.play(TransformFromCopy(eq3,tr3))
		#self.play(ShowCreation(tr1),ShowCreation(tr2),ShowCreation(tr3))
		self.wait()
		self.play(FadeOut(group1), FadeOut(braces))
		self.wait()
		self.play(Transform(grouptr, bigtr), ShowCreation(tr11), ShowCreation(tr22), ShowCreation(tr33) )
		self.wait()
		self.play(Write(p1))
		self.wait()
		self.play(Write(line1), Write(line2), Write(line3))
		self.wait()
		self.play(Write(three), Write(four), Write(five))
		self.wait()

		self.camera_frame.save_state()
		self.play(self.camera_frame.scale,.6, self.camera_frame.move_to, p1)
		self.wait()
		self.play(Write(fermat), ShowCreation(p11), Uncreate(p1))
		self.wait()
		self.play(Restore(self.camera_frame))
		self.wait()
		self.play(Uncreate(fermat),Transform(tr11, tr111), Transform(tr22, tr222), Transform(tr33, tr333))
		self.wait()
		self.play(ShowCreation(perp1))
		self.play(ShowCreation(perp2))
		self.play(ShowCreation(perp3))
		self.wait()
		self.play(TransformFromCopy(perp1,perp11),
				  TransformFromCopy(perp2,perp22),
				  TransformFromCopy(perp3,perp33))
		self.wait()
		self.play(Transform(groupperp, linetot), Write(minimal))
		self.wait()

		self.play(Uncreate(groupperp), Uncreate(minimal))
		self.play(MoveAlongPath(groupbig, l1), rate_func=linear) 
		self.play(Uncreate(tr11),
			Uncreate(tr22), Uncreate(tr33), Uncreate(grouptr))

		self.play(Write(sine_formula[0]))
		self.wait()
		self.play(TransformFromCopy(groupbig, sine_formula[1]))
		self.wait()
		self.play(TransformFromCopy(group_sides, sine_formula[2]))
		self.wait()
		self.play(Write(equals), ShowCreation(box_equals))
		self.wait()



