from big_ol_pile_of_manim_imports import *
from manimlib.imports import *
from manimlib.animation import *
 # Code used in this video: https://youtu.be/yf0G4QOTeYc

class Zeeman(Scene):
    def construct(self):
    	tex = TextMobject("Christopher Zeeman")
    	texx = TextMobject("1925-2016")
    	tex.move_to(UP*3)
    	texx.next_to(tex, DOWN)
    	self.play(Write(tex))
    	self.play(Write(texx))


class Fermat(Scene):
    def construct(self):
        title = TextMobject("Calculus")
        int2 = TexMobject(" x^{n}\\, + y^{n}\\, =\\, z^{n} \\, ? ")
        int1 = TexMobject("\\int_{0}^{1} x^e \\, (1-x)^{n} \\, dx  \\, =\\, n!/(e\\, +\\, 1)(e\\, +\\, 2)...(e\\, +\\, n\\, +\\, 1)")
        int2.next_to(int1, DOWN)
        title.move_to(UP*3.2)
        #self.play(Write(title))
        self.play(Write(int2))
        self.wait(2)
        #self.play(Write(int2))
class Morley(Scene):
    def construct(self):
    	tex = TextMobject("Morley's Miracle")
    	texx = TextMobject("1899")
    	tex.move_to(UP*3 + LEFT*3)
    	tex.set_color(BLACK)
    	texx.next_to(tex, DOWN)
    	self.play(Write(tex))
    	self.wait(2)
    	self.play(Write(texx))
    	self.wait(2)

class Proof(Scene):
    def construct(self):
    	tex = TextMobject("Possible proofs")
    	texx = TextMobject("1899")
    	tex.move_to(UP*3 + LEFT*3)
    	tex.set_color(BLACK)
    	texx.next_to(tex, DOWN)
    	self.play(Write(tex))
    	self.wait(2)
    	#self.play(Write(texx))
    	#self.wait(2)
