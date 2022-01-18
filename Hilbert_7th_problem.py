from big_ol_pile_of_manim_imports import *
from manimlib.mobject.coordinate_systems import ThreeDAxes

class problem(Scene):
	def construct(self):
		title = TextMobject("If a, b are" , "irrational" , "Can $a^{b}$ be" , "rational ?")
		
		title.scale(1.4)
		title[0:2].move_to(UP)
		title[2:4].move_to(DOWN*0.1 )

		title[1].set_color(BLUE)
		title[3].set_color(BLUE)
	

		title.scale(1.4)
	

		box2 = SurroundingRectangle(title,color=BLUE )
		

		self.play(Write(title[0:2]))
		self.wait()
		self.play(Write(title[2:4]))
		self.wait()
		self.play(Write(box2))

class hilbert(Scene):
	def construct(self):
		tit = TextMobject("Hilbert's 7th problem")
		prob1 = TextMobject("If a, b are algebraic and irrational", "is $a^{b}$ always transcendental ?")
		

		tit.to_edge(UP)
		prob1[0].move_to(UP*2.2)
		prob1[1].move_to(UP*1.5)

		box = SurroundingRectangle(prob1,color=BLUE )
		box2 = SurroundingRectangle(prob1,color=GREEN)

		prob1.scale(0.8)

		self.play(Write(tit))
		self.wait()
		self.play(Write(prob1))
		self.wait()
		self.play(Write(box))
		self.wait()
		self.play(Write(box2))

class root2(Scene):
	def construct(self):
		q = TextMobject("Is $2^{\\sqrt{2}}$ rational ?", "(1919)")
		a = TextMobject("Hell No !", "(1930)")

		hilb = TextMobject("David Hilbert")
		kuz = TextMobject("Rodion Kuzmin")

		q[0].move_to(UP*3)
		q[1].move_to(UP*2)

		hilb.move_to(DOWN)
		kuz.move_to(DOWN*2)
		"""

		q.set_color(BLACK)
		a.set_color(BLACK)
		hilb.set_color(BLACK)
		kuz.set_color(BLACK)
		"""


		self.play(Write(q) , Write(a), Write(hilb), Write(kuz))


class theodGel(Scene):
	def construct(self):
		t = TextMobject("1934")
		t2 = TextMobject("1934: Gelfond- Schneider theorem")

		gel = TextMobject("Aleksandr Gelfond")
		sch = TextMobject("Theodor Schneider")

		t.move_to(UP*3)
		t2.move_to(UP*3)

		gel.move_to(UP*2)


		self.play(Write(t),Write(gel),Write(sch))
		self.wait()
		self.play(ReplacementTransform(t, t2))


class algeb(Scene):
	def construct(self):
		t = TextMobject("x", " is algebraic if")

		t2 = TextMobject("x is a root of a non- zero polynomial ","in one variable with integer coefficients")

		root = TextMobject("$\\sqrt{2}$ :", "root of $x^{2}\\, -\\, 2$")
		pie = TextMobject("$\\pi $" , ", ", "$e$: ", "not algebraic", "(Lindemann–Weierstrass theorem )")


		t.to_edge(UP)
		t2[0].move_to(UP*2)
		t2[1].move_to(UP*1.2)
		pie[0:4].move_to(DOWN)
		pie[4].move_to(DOWN*1.5)

		pie[4].scale(0.8)

		root[0].set_color(YELLOW)
		pie[0].set_color(YELLOW)
		pie[2].set_color(YELLOW)

		box = SurroundingRectangle(t2, color = WHITE )

		self.play(Write(t))
		self.play(Write(t2))
		self.play(Write(box))
		self.play(Write(root))
		self.play(Write(pie[0:4]))
		self.play(Write(pie[4]))

class proof1(Scene):
	def construct(self):
		t = TextMobject("Gelfond- Schneider theorem" , "$\\Rightarrow$", " $\\sqrt{2}^{\\sqrt{2}}$ is irrational")
		ab = TextMobject("$(a\\, =\\, \\sqrt{2}^{\\sqrt{2}} $ , $b \\, = \\, \\sqrt{2}$) $\\Rightarrow$" , "$a^{b}\\, = \\, 2$ ")

		t.move_to(UP)

		t.scale(0.9)
		ab.scale(0.9)

		self.play(Write(t[0]))
		self.play(Write(t[1:3]))
		self.wait()
		self.play(Write(ab[0]))
		self.wait()
		self.play(Write(ab[1]))


class video(Scene):
	def construct(self):
		#n = TextMobject("Gregory Galperin")
		video = TextMobject("Video by 3Blue1Brown: https://www.youtube.com/watch?v=jsYwFizhncE")

		#self.play(Write(n))
		self.play(Write(video))

class nonc(Scene):
	def construct(self):
		nonc = TextMobject("Non- constructive proof")
		video = TextMobject("Video by 3Blue1Brown: https://www.youtube.com/watch?v=jsYwFizhncE")

		nonc.move_to(UP)
		video.scale(0.8)
		self.play(Write(nonc))
		self.play(Write(video))


class proof2(Scene):
	def construct(self):
		ab = TextMobject("$(a\\, =\\, \\sqrt{2} $ , $b \\, = \\, \\sqrt{2}$)")
		power = TextMobject("$a^{b}\\, =\\, \\sqrt{2}^{\\sqrt{2}}$")

		rat = TextMobject("solved")
		irrat = TextMobject("$a \\, =\\, \\sqrt{2}^{\\sqrt{2}}$,$b \\, = \\, \\sqrt{2}$ ")
		power2 = TextMobject("$a^{b}\\, =\\, \\sqrt{2}^{2}\\, =\\, 2$", "- solved")

		ratio = TextMobject("rational")
		irratio = TextMobject("irrational")

		ab.move_to(UP*2)
		power.move_to(UP*1.2)
		rat.move_to(LEFT*3 + DOWN)
		irrat.move_to(RIGHT*2.5 + DOWN*0.9)
		power2.move_to(RIGHT*2.5 + DOWN*1.9)


		arr1 = Arrow(UP*0.97, LEFT*3 + DOWN*0.9 )
		arr2 = Arrow(UP*0.97, RIGHT*2.5 + DOWN*0.8)

		ratio.move_to(LEFT*2.7 )
		irratio.next_to(RIGHT*1.3 )

		ratio.set_color(RED)
		irratio.set_color(RED)

		ratio.scale(0.8)
		irratio.scale(0.8)

		arr1.set_color(BLUE)
		arr2.set_color(BLUE)

		self.play(Write(ab))
		self.play(Write(power))
		self.play(Write(arr1))
		self.play(Write(ratio))
		self.play(Write(rat))
		self.play(Write(arr2))
		self.play(Write(irratio))
		self.play(Write(irrat))
		self.play(Write(power2[0]))
		self.play(Write(power2[1]))
	
class proof3(Scene):
	def construct(self):
		t = TextMobject("Third solution")
		log = TextMobject("logarithms !")
		ab = TextMobject("$(a\\, =\\, \\sqrt{3} $ ", ", $b \\, = \\, 2\\log_{3}2$)")
		apb = TextMobject("$a^{b}\\, =\\, 2$")


		t.to_edge(UP)
		log.move_to(UP*2)
		ab.move_to(UP)

		self.play(Write(t))
		self.play(Write(log))
		self.play(Uncreate(log))
		self.play(Write(ab))
		self.play(Write(apb))
		self.wait()
