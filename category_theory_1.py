from big_ol_pile_of_manim_imports import *
from manimlib.mobject.coordinate_systems import ThreeDAxes
from numpy import *
from pathlib import Path

class opening(Scene):
	def construct(self):
		elems = TextMobject("Elements")
		opers = TextMobject("Operations")

		nums = TextMobject("2\\," , ",\\, 3\\," , ",\\, 4\\, ,\\,","\\,5")
		add = TextMobject("2 + 3 ")
		subtr = TextMobject("4\\, -\\, 2")
		mult = TexMobject("3\\, \\cdot \\, 5")

		tr = Polygon(2*LEFT, 3.464*UP, 2*RIGHT, color = BLUE)
		tr.move_to(LEFT*3)

		tr1 = Polygon(2*LEFT, 3.464*UP, 2*RIGHT, color = RED)
		tr1.scale(0.5)
		tr1.move_to(RIGHT*3 + UP*1.5)

		tr2 = Polygon(2*LEFT, 3.464*UP, 2*RIGHT, color = RED)
		tr2.scale(0.5)
		tr2.move_to(RIGHT*3.5 + DOWN*1.5)

		elems.move_to(LEFT*3)
		opers.move_to(RIGHT*3)
		nums.move_to(LEFT*3)

		add.move_to(RIGHT*3 + UP*2)
		subtr.move_to(RIGHT*3)
		mult.move_to(RIGHT*3 + DOWN*2)

		add.set_color(YELLOW)
		subtr.set_color(YELLOW)
		mult.set_color(YELLOW)

		self.play(FadeIn(elems))
		self.wait()
		self.play(FadeIn(opers))
		self.wait()

		self.play(Transform(elems, nums[0]))
		self.wait()
		self.play(Write(nums[1]))
		self.play(Write(nums[2]))
		self.play(Write(nums[3]))
		self.wait()
		self.play(TransformFromCopy(nums[0:2] , add))
		subgr1 = VGroup(nums[0] , nums[2])
		subgr2 = VGroup(nums[1] , nums[3])
		self.play(TransformFromCopy(subgr1 , subtr), FadeOut(opers))
		self.wait()
		self.play(TransformFromCopy(subgr2 , mult))

		self.play(Transform(nums , tr), FadeOut(elems))
		self.wait()
		self.play(FadeOut(add),FadeOut(subtr), FadeOut(mult))
		self.wait()

		self.play(Rotate(tr1, angle = math.radians(120)), run_time = 2)
		self.wait()
		self.play(ShowCreation(tr2))
		self.wait()


class heart(Scene):
	def construct(self):
		arr1 = Arrow(2*DOWN , 1.8*LEFT)
		arr2 = Arrow(1.8*LEFT , LEFT + 1.5*UP)
		arr3 = Arrow(LEFT + 1.5*UP, UP)
		arr4 = Arrow(UP , RIGHT + 1.5*UP)
		arr5 = Arrow(RIGHT + 1.5*UP , 1.8*RIGHT)
		arr6 = Arrow(1.8*RIGHT , 2*DOWN)

		arr1.set_color(RED)
		arr2.set_color(RED)
		arr3.set_color(RED)
		arr4.set_color(RED)
		arr5.set_color(RED)
		arr6.set_color(RED)

		self.play(ShowCreation(arr1))
		self.play(ShowCreation(arr2))
		self.play(ShowCreation(arr3))
		self.play(ShowCreation(arr4))
		self.play(ShowCreation(arr5))
		self.play(ShowCreation(arr6))
		self.wait()




class opening2(Scene):
	def construct(self):
		elems = TextMobject("Elements")
		opers = TextMobject("Operations")
		cat = TextMobject("Category Theory")
		cat.to_edge(UP)


		elems2 = TextMobject("Elements")
		opers2 = TextMobject("Operations")

		elems3 = TextMobject("Elements")
		opers3 = TextMobject("Operations")

		elems2.scale(2)
		elems2.move_to(UP)
		box = SurroundingRectangle(elems2, color = RED)
		opers2.move_to(DOWN)
		ar = Arrow(elems2, opers2)

		opers3.scale(2)
		opers3.move_to(UP)
		elems3.move_to(DOWN)
		box1 = SurroundingRectangle(opers3, color = RED)



		rotate = TextMobject("Rotate" , " a triangle")
		add = TextMobject("Add " , " two and three")
		


		elems.move_to(LEFT*3 + UP*3)
		opers.move_to(RIGHT*3 + UP*3)

		self.play(FadeIn(elems))
		self.play(FadeIn(opers))
		self.play(FadeIn(rotate[0]))
		self.play(FadeIn(rotate[1]))
		subgr1 = VGroup(rotate[0] , rotate[1])
		self.play(FadeOut(rotate))
		self.play(FadeIn(add[0]))
		self.play(Write(add[1]))

		self.play(FadeOut(add))
		self.play(FadeOut(elems), FadeOut(opers) )

		self.play(Write(elems2))
		self.play(ShowCreation(box))
		self.play(Write(ar))
		self.wait()
		self.play(Write(opers2))

		self.play(FadeIn(cat))
		self.play(Transform(elems2,opers3), FadeOut(opers2), FadeOut(box),FadeIn(box1))
		self.play(Write(elems3))
		self.wait()

class diagram(Scene):
	def construct(self):
		x = TextMobject("X")
		y = TextMobject("Y")
		z = TextMobject("Z")

		x.move_to(LEFT + UP*2)
		y.move_to(RIGHT + UP*2)
		z.move_to(RIGHT)

		arr1 = Arrow(x,y)
		arr2 = Arrow(y,z)
		arr3 = Arrow(x,z)

		self.play(FadeIn(x), FadeIn(y),FadeIn(z))
		self.play(FadeIn(arr1))
		self.play(FadeIn(arr2))
		self.play(FadeIn(arr3))
		self.wait()

class opening3(Scene):
	def construct(self):
		set1 = TexMobject("{ " , "\\, 2\\, ,\\, 3\\, , \\, \\pi \\, ,\\, \\frac{-1}{12}", "\\, }")
		set2 = TexMobject("{ " , "\\, a\\, , \\, b\\, ,\\, c\\, , \\, ...  \\, ,\\, d ", "\\, }")
		sets = TextMobject("Sets")
		sets.move_to(RIGHT*2)
		set1.move_to(LEFT*3 + UP*1.5)
		set2.move_to(LEFT*3 + DOWN*1.5)

		br1 = Brace(set1, LEFT)
		br2 = Brace(set2, LEFT)
		br3 = Brace(set1, RIGHT)
		br4 = Brace(set2, RIGHT)

		arr1 = Arrow(br3, RIGHT*1.2)
		arr2 = Arrow(br4, RIGHT*1.2)
		arr1.set_color(BLUE)
		arr2.set_color(BLUE)

		arr3 = Arrow(set1[1], set2[1])
		arr3.set_color(RED)
		func = TextMobject("function")
		func.scale(0.8)
		func.next_to(arr3, LEFT)


		self.play(Write(set1[1]))
		self.play(Write(set2[1]))
		self.wait()

		self.play(Write(br1) , Write(br2))
		self.play(Write(br3) , Write(br4))
		self.wait()

		self.play(ShowCreation(arr1),ShowCreation(arr2))
		self.play(Write(sets))
		self.wait()

		self.play(ShowCreation(arr3))
		self.play(Write(func))
		self.wait()

class subset(Scene):
	def construct(self):
		subs = TexMobject("f \\, \\subseteq \\, A\\times B ")
		self.play(Write(subs))
		self.wait()


class function(Scene):
	def construct(self):
		title = TextMobject("Function")
		inj = TextMobject("Injective")
		surj = TextMobject("Surjective")

		defin = TextMobject("Defined through elements !")

		inj.move_to(UP*2 + LEFT*3.5)
		surj.move_to(UP*2 + RIGHT*3.5)
		title.to_edge(UP)
		defin.to_edge(UP)

		definition = TexMobject("For\\, sets\\, A\\, ,\\, B\\,"," \\, a\\, function\\, ","\\, f\\,:\\, A\\, \\rightarrow \\, B \\,"," \\, is ")
		definition2 = TexMobject("a\\, subset\\, of \\, \\,  A\\times B\\,","\\,=\\, \\,", "\\, \\, \\, {(a,b)\\, |\\, a\\, \\in \\, A\\, ,\\, b\\, \\in \\, B }")
		definition3 = TexMobject("a\\, subset\\, of \\, \\,  A\\times B\\,","\\,=\\, \\,", "\\, \\, \\, {(a,b)\\, |\\, a\\, \\in \\, A\\, ,\\, b\\, \\in \\, B }")

		definition.move_to(UP)
		definition[2].set_color(BLUE)
		definition2[2].set_color(BLUE)
		definition3[2].set_color(YELLOW)

		a = TextMobject("a")
		b = TextMobject("b")
		c = TexMobject("c")
		
		a.move_to(DOWN*2 + LEFT)
		b.move_to(DOWN + RIGHT)
		c.move_to(DOWN*3 + RIGHT)

		br1 = Brace(definition2[2], LEFT)
		br2 = Brace(definition2[2], RIGHT)

		arr1 = Arrow(a,b)
		arr2 = Arrow(a,c)


		self.play(FadeIn(title))
		self.wait()
		self.play(Write(definition[0]))
		self.play(Write(definition[1:4]))
		self.play(Write(definition2[0]))
		self.wait()
		self.play(FadeIn(definition2[1]))
		self.play(FadeIn(definition2[2]), FadeIn(br1), FadeIn(br2))
		self.wait()

		self.play(FadeIn(a))
		self.play(FadeIn(b),FadeIn(c))
		self.play(FadeIn(arr1) , FadeIn(arr2))
		self.play(Transform(definition2[2],definition3[2]))
		self.wait()

		self.play(Uncreate(a) , Uncreate(b) , Uncreate(c) , Uncreate(arr1) , Uncreate(arr2))
		self.play(Uncreate(definition) , Uncreate(definition2) , Uncreate(br1) , Uncreate(br2))
		self.wait()

		self.play(FadeIn(inj))
		self.play(FadeIn(surj))
		self.wait()

		self.play(Transform(title, defin))
		self.wait()

class inj(Scene):
	def construct(self):
		d1 = Dot(UP*1.5 + LEFT*2)
		d2 = Dot(UP*0.5 + LEFT*2)
		d3 = Dot(DOWN*0.5 + LEFT*2)
		d4 = Dot(DOWN*1.5 + LEFT*2)

		d11 = Dot(UP*2 + RIGHT*2)
		d22 = Dot(UP + RIGHT*2)
		d33 = Dot( RIGHT*2)
		d44 = Dot(DOWN*1 + RIGHT*2)
		d55 = Dot(DOWN*2 + RIGHT*2)

		arr1 = Arrow(d1, d11)
		arr2 = Arrow(d2, d22)
		arr3 = Arrow(d3, d44)
		arr4 = Arrow(d4, d44)

		arr5 = Arrow(d4, d55)

		self.play(ShowCreation(d1) , ShowCreation(d2), ShowCreation(d3), ShowCreation(d4))
		self.play(ShowCreation(d11),ShowCreation(d22),ShowCreation(d33),ShowCreation(d44),ShowCreation(d55))
		self.play(ShowCreation(arr1),ShowCreation(arr2),ShowCreation(arr3),ShowCreation(arr4))
		self.wait()
		self.play(Transform(arr4, arr5))
		self.wait()

class surj(Scene):
	def construct(self):
		d1 = Dot(UP*1.5 + LEFT*2)
		d2 = Dot(UP*0.5 + LEFT*2)
		d3 = Dot(DOWN*0.5 + LEFT*2)
		d4 = Dot(DOWN*1.5 + LEFT*2)

		
		d22 = Dot(UP + RIGHT*2)
		d33 = Dot( RIGHT*2)
		d44 = Dot(DOWN*1 + RIGHT*2)
		
		arr1 = Arrow(d1, d22)
		arr2 = Arrow(d2, d22)
		arr3 = Arrow(d3, d33)
		arr4 = Arrow(d4, d33)

		arr5 = Arrow(d4, d44)


		self.play(ShowCreation(d1) , ShowCreation(d2), ShowCreation(d3), ShowCreation(d4))
		self.play(ShowCreation(d22),ShowCreation(d33),ShowCreation(d44))
		self.play(ShowCreation(arr1),ShowCreation(arr2),ShowCreation(arr3),ShowCreation(arr4))
		self.wait()
		self.play(Transform(arr4, arr5))
		self.wait()

class bij(Scene):
	def construct(self):
		tit = TextMobject("Bijection")
		tit.move_to(DOWN*2.5)
		d1 = Dot(UP*1.5 + LEFT*2)
		d2 = Dot(UP*0.5 + LEFT*2)
		d3 = Dot(DOWN*0.5 + LEFT*2)
		d4 = Dot(DOWN*1.5 + LEFT*2)

		d11 = Dot(UP*1.5 + RIGHT*2)
		d22 = Dot(UP*0.5 + RIGHT*2)
		d33 = Dot(DOWN*0.5 + RIGHT*2)
		d44 = Dot(DOWN*1.5 + RIGHT*2)

		arr1 = Arrow(d1, d22)
		arr2 = Arrow(d2, d11)
		arr3 = Arrow(d3, d33)
		arr4 = Arrow(d4, d44)

		self.play(ShowCreation(d1) , ShowCreation(d2), ShowCreation(d3), ShowCreation(d4))
		self.play(ShowCreation(d11) , ShowCreation(d22), ShowCreation(d33), ShowCreation(d44))
		self.play(ShowCreation(arr1) , ShowCreation(arr2) , ShowCreation(arr3), ShowCreation(arr4))
		self.wait()
		self.play(Write(tit))
		self.wait()


class bij2(Scene):
	def construct(self):
		tit = TextMobject("Bijection")
		tit.move_to(DOWN*2.5)
		d1 = Dot(UP*1.5 + LEFT*2)
		d2 = Dot(UP*0.5 + LEFT*2)
		d3 = Dot(DOWN*0.5 + LEFT*2)
		d4 = Dot(DOWN*1.5 + LEFT*2)

		d11 = Dot(UP*1.5 + RIGHT*2)
		d22 = Dot(UP*0.5 + RIGHT*2)
		d33 = Dot(DOWN*0.5 + RIGHT*2)
		d44 = Dot(DOWN*1.5 + RIGHT*2)

		f = TexMobject("f")
		f.move_to(DOWN*2.2)
		f.set_color(YELLOW)

		A = TextMobject("A")
		A.move_to(LEFT*2 + DOWN*2)
		B = TextMobject("B")
		B.move_to(RIGHT*2 + DOWN*2)
		A.set_color(BLUE)
		B.set_color(BLUE)

		arr1 = Arrow(d1, d22)
		arr2 = Arrow(d2, d11)
		arr3 = Arrow(d3, d33)
		arr4 = Arrow(d4, d44)

		d10 = Dot(UP*1.5 + LEFT*2)
		d20 = Dot(UP*0.5 + LEFT*2)
		d30 = Dot(DOWN*0.5 + LEFT*2)
		d40 = Dot(DOWN*1.5 + LEFT*2)

		d110 = Dot(UP*1.5 + RIGHT*2)
		d220 = Dot(UP*0.5 + RIGHT*2)
		d330 = Dot(DOWN*0.5 + RIGHT*2)
		d440 = Dot(DOWN*1.5 + RIGHT*2)

		Aa = TextMobject("A")
		Aa.move_to(LEFT*2 + DOWN*2)
		Bb = TextMobject("B")
		Bb.move_to(RIGHT*2 + DOWN*2)
		Aa.set_color(BLUE)
		Bb.set_color(BLUE)

		fin = TexMobject("f^{-1}")
		fin.move_to(DOWN*2.2)
		fin.set_color(YELLOW)

		arr11 = Arrow(d22, d1)
		arr22 = Arrow(d11, d2)
		arr33 = Arrow(d33, d3)
		arr44 = Arrow(d44, d4)

		bij1 = VGroup(d1,d2,d3,d4,d11,d22,d33,d44,arr1,arr2,arr3,arr4 , f, A, B)
		bij1.move_to(LEFT*3 + UP*2)
		bij1.scale(0.8)

		bij2 = VGroup(d10,d20,d30,d40,d110,d220,d330,d440,arr11,arr22,arr33,arr44, fin, Aa,Bb)
		bij2.move_to(RIGHT*3 + UP*2)
		bij2.scale(0.8)

		a = TexMobject("A\\,","\\, \\overset{f}{\\longrightarrow} \\,","\\,B\\,","\\overset{f^{-1}}{\\longrightarrow}\\,", "\\,A")
		a.move_to(DOWN)
		idA = TexMobject("id_{A}")
		idA.move_to(DOWN*3)

		b = TexMobject("B\\,","\\, \\overset{f^{-1}}{\\longrightarrow} \\,","\\,A\\,","\\overset{f}{\\longrightarrow}\\,", "\\,B")
		b.move_to(DOWN)
		idB = TexMobject("id_{B}")
		idB.move_to(DOWN*3)


		self.play(ShowCreation(bij1))
		self.play(ShowCreation(bij2))
		self.wait()
		self.play(Write(a[0]))
		self.play(FadeIn(a[1]))
		self.play(FadeIn(a[2]))
		self.play(FadeIn(a[3]))
		self.play(FadeIn(a[4]))
		self.wait()

		self.play(Write(idA))
		self.wait()

		self.play(FadeOut(a),FadeIn(b[0]), Uncreate(idA))
		self.wait()
		self.play(FadeIn(b[1]))
		self.play(FadeIn(b[2]))
		self.play(FadeIn(b[3]))
		self.play(FadeIn(b[4]))
		self.wait()
		self.play(Write(idB))
		self.wait()

class new_def(Scene):
	def construct(self):
		title = TextMobject("Alternative definition")
		title.to_edge(UP)
		equiv = TextMobject(" 'the same as' ")

		definition = TextMobject("A function ","f","is injective"," if and only if"," it has a left inverse")
		definition2 = TextMobject("A function ","f","is surjective"," if and only if"," it has a right inverse")

		definition1 = TextMobject("A function ","f","is injective"," if and only if"," it has a left inverse")
		definition21 = TextMobject("A function ","f","is surjective"," if and only if"," it has a right inverse")

		definition.move_to(UP*0.5)
		definition2.move_to(DOWN*0.5)
		definition.scale(0.8)
		definition2.scale(0.8)
		box = SurroundingRectangle(definition[3], color = RED)

		
		equiv.move_to(UP*1.5 + RIGHT)
		equiv.scale(0.7)
		arr = Arrow(box, equiv)


		definition1.move_to(UP*0.5)
		definition21.move_to(DOWN*0.5)
		definition1.scale(0.8)
		definition21.scale(0.8)

		definition1.set_color(YELLOW)
		definition21.set_color(YELLOW)

		
		self.play(FadeIn(title))
		self.wait()
		self.play(FadeIn(definition[0:4]))
		self.play(FadeIn(definition[4]))
		self.play(FadeIn(definition2[0:4]))
		self.play(FadeIn(definition2[4]))
		self.wait()
		
		self.play(ShowCreation(box),ShowCreation(arr))
		self.play(Write(equiv))
		self.wait()
		self.play(Uncreate(arr), Uncreate(equiv), Uncreate(box))

		self.play(Transform(definition[4] , definition1[4]))
		self.wait()
		self.play(Transform(definition2[4] , definition21[4]))
		self.wait()

class left_inv(Scene):
	def construct(self):
		definition = TextMobject("$ f\\,:\\, A\\, \\rightarrow \\, B $ ", " is injective " ,"$ \\Leftrightarrow $ ","  f has a left inverse")
		definition.to_edge(UP)
		box1 = SurroundingRectangle(definition, color = BLUE)

		proof1 = TexMobject("(\\Leftarrow)\\," , "\\, \\,\\exists \\, g\\, :\\, B\\, \\rightarrow \\, A\\,", "\\," , "\\,s.t.", "\\,", " \\, g\\circ f\\, =\\, id_{A}")
		proof1[3].scale(0.8)
		proof1.move_to(UP*2)

		proof2 = TextMobject("Let " , "$\\alpha \\, ,\\, \\alpha^\\prime\\, \\in \\, A\\,$ "," , $\\, \\alpha \\, \\neq \\, \\alpha^\\prime $")
		proof2.move_to(UP)

		proof3 = TexMobject("g\\circ f(\\alpha)\\," , "\\, =\\, \\alpha \\,","\\, \\neq \\,", "\\alpha^\\prime\\,", "\\, =\\, g\\circ f(\\alpha^\\prime)")
		proof4 = TexMobject("f(\\alpha)\\, \\neq \\, f(\\alpha^\\prime)")
		proof4.move_to(DOWN)

		d1 = Dot(UP*1.5 + LEFT*2)
		d2 = Dot(UP*0.5 + LEFT*2)

		d11 = Dot(UP*2 + RIGHT*2)
		d22 = Dot(RIGHT*2)

		alp = TexMobject("f(\\alpha)")
		alp.scale(0.8)
		alp.next_to(d1, LEFT)

		alpp = TexMobject("f(\\alpha^\\prime)")
		alpp.scale(0.8)
		alpp.next_to(d2, LEFT)
		g = TextMobject("g")
		g.move_to(DOWN*0.5)
		g.set_color(YELLOW)
		g.scale(0.9)

		arr1 = Arrow(d1,d11)
		arr2 = Arrow(d2,d22)

		gr = VGroup(d1,d2,d11,d22, alp, alpp, arr1, arr2, g)

		gr.move_to(DOWN*2)
		gr.scale(0.8)



		self.play(Write(definition))
		self.wait()
		self.play(ShowCreation(box1))
		self.play(FadeIn(proof1[0]))
		self.play(FadeIn(proof1[1]))
		self.play(FadeIn(proof1[2:4]))
		self.play(FadeIn(proof1[4:6]))
		self.wait()

		self.play(FadeIn(proof2[0:2]))
		self.play(FadeIn(proof2[2]))
		self.wait()
		self.play(FadeIn(proof3[0]))
		self.play(FadeIn(proof3[1]))
		self.play(FadeIn(proof3[2]))
		self.play(FadeIn(proof3[3]))
		self.play(FadeIn(proof3[4]))
		self.wait()

		self.play(ShowCreation(gr))
		self.wait()
		self.play(Uncreate(gr))
		self.play(Write(proof4))
		self.wait()

class another(Scene):
	def construct(self):
		inj = TextMobject("Injective")
		depen = TextMobject("(element dependent)")

		inv = TextMobject("Has a left inverse")
		nots = TextMobject("(not so much)")
		
		q = TexMobject("?")
		qq = TextMobject("Monomorphism")
		nota = TextMobject("(not dependent)")

		inv.move_to(UP*2)
		nots.move_to(UP*2)
		inj.move_to(LEFT*2.15 + DOWN)
		depen.move_to(LEFT*2.15 + DOWN)
		q.move_to(RIGHT*2.15 + DOWN)
		qq.move_to(RIGHT*2.45 + DOWN)
		nota.move_to(RIGHT*2.45 + DOWN)

		self.play(FadeIn(inj))
		self.play(FadeIn(inv))
		self.play(FadeIn(q))
		self.wait()
		self.play(Transform(q,qq))
		self.wait()
		self.play(Transform(inj, depen))
		self.play(Transform(inv, nots))
		self.play(Transform(q, nota))
		self.wait()

class notbut(Scene):
	def construct(self):
		nott = TextMobject("Not what injection", " is")
		butt = TextMobject("But"," how ", "it interacts with other functions")

		nott[1].set_color(YELLOW)
		butt[1].set_color(YELLOW)
		nott.move_to(UP*0.5)
		butt.move_to(DOWN*0.5)

		self.play(Write(nott[0]))
		self.play(Write(nott[1]))
		self.play(Write(butt[0]))
		self.play(Write(butt[1]))
		self.play(Write(butt[2]))
		self.wait()


class monomorph(Scene):
	def construct(self):
		title = TextMobject("Yet another definition !")
		defin = TextMobject("$f\\,:\\, A \\rightarrow \\, B$","is a","monomorphism ","if")
		defin2 = TextMobject("for all sets Z and ","all functions" , "$\\alpha\\, ,\\, \\alpha^\\prime\\, :\\, Z\\, \\rightarrow \\, A $")
		defin3 = TexMobject("f\\circ \\alpha \\, =\\, f\\circ \\alpha^\\prime \\, \\," , "\\, implies\\," , "\\, \\, \\alpha\\, =\\, \\alpha^\\prime ")
		defin22 = TextMobject("for all sets Z and ","all functions" , "$\\alpha\\, ,\\, \\alpha^\\prime\\, :\\, Z\\, \\rightarrow \\, A $")
		defin222 = TextMobject("for all sets Z and ","all functions" , "$\\alpha\\, ,\\, \\alpha^\\prime\\, :\\, Z\\, \\rightarrow \\, A $")

		surprise = TextMobject("A function is injective if and only if it is a monomorphism")

		defin.move_to(UP*2)
		defin2.move_to(UP)
		defin22.move_to(UP)
		defin222.move_to(UP)
		surprise.move_to(DOWN*1.5)
		defin22[1].set_color(YELLOW)
		defin3[1].scale(0.8)
		title.to_edge(UP)

		gr = VGroup(defin,defin2,defin3)
		box = SurroundingRectangle(gr, color = BLUE)

		defin[2].set_color(YELLOW)
		self.play(Write(title))
		self.play(FadeIn(defin[0]))
		self.play(FadeIn(defin[1:3]))
		self.play(FadeIn(defin[3]))
		self.play(FadeIn(defin2[0]))
		self.play(FadeIn(defin2[1]))
		self.play(FadeIn(defin2[2]))
		self.play(FadeIn(defin3[0]))
		self.play(FadeIn(defin3[1]))
		self.play(FadeIn(defin3[2]))
		self.wait()
		self.play(Transform(defin2[1] , defin22[1]))
		self.play(Transform(defin2[1] , defin222[1]))
		self.play(ShowCreation(box))
		self.play(FadeIn(surprise))
		self.wait()



class Graphs(GraphScene):
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
    "axes_color" : WHITE
    }
    def construct(self):
        self.graph_origin=0*LEFT+0*DOWN
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,x_min = 0.001, x_max = 5, color=YELLOW)
        func_graph_2=self.get_graph(self.func_to_graph_2,x_min = 0.001, x_max = 5, color=YELLOW)

        graph1 = self.get_graph(self.func_to_graph,x_min = 1.0001, x_max = 2.5, color=YELLOW)
        graph2 = self.get_graph(self.func_to_graph_2,x_min = 1.0001, x_max = 2.5, color=YELLOW)
        line1 = self.get_graph(self.line1, x_min = -1, x_max = 1, color = GREEN)
        #func_graph_3=self.get_graph(self.func_to_graph,x_min=-0.6823,x_max=3, color=BLUE)
        #func_graph_4=self.get_graph(self.func_to_graph_2,x_min=-0.6823,x_max=3, color=BLUE)
        self.play(ShowCreation(func_graph),ShowCreation(func_graph_2))
        self.wait()
        self.play(Uncreate(func_graph_2))
        #self.play(Uncreate(func_graph),Uncreate(func_graph_2),Uncreate(graph1),Uncreate(graph2))
        self.wait(2)
        #self.play(ShowCreation(func_graph_3),ShowCreation(func_graph_4))

    def func_to_graph(self,x):
        return(np.sqrt(x))
    def func_to_graph_2(self,x):
        return(- np.sqrt(x))
    def line1(sefl,x):
        return(0.5*x + 1)

class thumb(Scene):
	def construct(self):
		d1 = Dot(UP*2 , radius = 0.2 )
		d2 = Dot(DOWN*0.5, radius = 0.2 )
		d3 = Dot(DOWN*1.5 + RIGHT*2, radius = 0.2 )
		d4 = Dot(DOWN*1.5 + LEFT*2, radius = 0.2 )

		arr1 = Arrow(d1 , d2)
		arr2 = Arrow(d2 , d3)
		arr3 = Arrow(d2 , d4)

		arr4 = CurvedArrow(UP*2 , DOWN*1.5 + LEFT*2 )
		arr5 = CurvedArrow(UP*2 , DOWN*1.5 + RIGHT*2 )

		d1.set_color(YELLOW)

		self.play(Write(d1) , Write(d2) , Write(d3), Write(d4) )
		self.play(Write(arr1) , Write(arr2), Write(arr3) )


