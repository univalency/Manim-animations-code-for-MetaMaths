#source code for the following video: https://youtu.be/LQvTJpgkGgE
from big_ol_pile_of_manim_imports import *
from manimlib.mobject.coordinate_systems import ThreeDAxes

class intro(MovingCameraScene):
    def construct(self):
        ferm1 = TextMobject("Solve ", "  $\\, \\,x^{n}\\, +\\, y^{n}\\, =\\, z^{n} $ ")
        ferm11 = TextMobject("Solve ", "  $\\, \\,x^{x}\\, +\\, y^{y}\\, =\\, z^{z} $ ")
        
        ferm2 = TextMobject("for ","$\\, n \\geq 3 \\,$, $\\, x,y,z \\, \\in \\mathbb{Z}$")
        ferm22 = TextMobject("$x,y,z \\, \\in \\mathbb{N}$")

        ferm3 = TexMobject("\\,x^{x}\\, +\\, y^{y}\\, =\\, z^{z} ")

        nosol = TextMobject("No solutions !")
        contr = TextMobject("proof by contradiction:")

        proof1 = TexMobject("Let \\,","\\, x,y,z\\,"," \\in \\, \\mathbb{N}\\, \\,","\\, and \\,","\\, \\, x", "^x", "+", "y", "^y", "=", "z", "^z" )

        ineq1 = TexMobject("z^{z}\\, >\\,  x^{x}")
        ineq2 = TexMobject("z^{z}\\, >\\,  y^{y}")

        ferm1.move_to(UP)
        ferm11.move_to(UP)

        nosol.move_to(UP)
        contr.move_to(UP)
        nosol.set_color(YELLOW)
        ferm2[1].set_color(BLUE)

        ferm3.to_edge(UP)
        ferm3.scale(1.2)

        ferm22.set_color(BLUE)

        proof1.move_to(UP*3)
        
        ineq1.move_to(UP*1.5)
        ineq2.move_to(UP*0.5)

        gr = VGroup(ineq1, ineq2)
        br = Brace(gr, LEFT)
    
        proof1.set_color_by_tex("x", YELLOW)
        proof1.set_color_by_tex("y", YELLOW)
        proof1.set_color_by_tex("z", YELLOW)
        proof1[1].set_color(BLUE)
        proof1[2:4].set_color(WHITE)
        proof1[4].set_color(WHITE)
        proof1[7].set_color(WHITE)
        proof1[10].set_color(WHITE)

        self.play(Write(ferm1))
        self.wait()
        self.play(Write(ferm2))
        self.wait()
        self.play(Transform(ferm1[1],ferm11[1]))
        self.wait()
        self.play(Transform(ferm2,ferm22))
        self.wait()
        self.play(Transform(ferm1, ferm3), Uncreate(ferm2))
        self.wait()
        self.play(FadeIn(nosol))
        self.wait()
        self.play(Uncreate(nosol), FadeIn(contr))
        self.wait()
        self.play(FadeOut(contr))
        self.play(Transform(ferm1, proof1))
        self.wait()
        self.play(Write(ineq1))
        self.play(Write(ineq2))
        self.wait()
        self.play(Write(br))
        gr2 = VGroup(br, gr)
        self.play(gr2.shift, 2*LEFT)
        self.wait()

        implies = TexMobject("\\Rightarrow")
        implies.next_to(gr2, RIGHT*2)
        implies.set_color(YELLOW)
        self.play(Write(implies))
        self.wait()
        
        ineq11 = TexMobject("z \\, > \\, x")
        ineq22 = TexMobject("z \\, > \\, y")

        ineq11.move_to(UP*1.5)
        ineq22.move_to(UP*0.5)

        ineq111 = TexMobject("z \\, \\geq \\, x\\, +\\, 1")
        ineq222 = TexMobject("z \\, \\geq \\, y\\, +\\, 1")

        ineq111.move_to(UP*1.5)
        ineq222.move_to(UP*0.5)

        gr11 = VGroup(ineq11, ineq22)
        br2 = Brace(gr11, LEFT) 
        gr3 = VGroup(gr11, br2)
        gr3.next_to(implies, RIGHT*2)

        gr111 = VGroup(ineq111, ineq222)
        br22 = Brace(gr111, LEFT) 
        gr33 = VGroup(gr111, br22)
        gr33.next_to(implies, RIGHT*2)


        self.play(Write(gr3))
        self.wait()

        suppose = TexMobject("Suppose\\, \\,"," z \\, < \\, x")
        suppose1 = TexMobject("Suppose\\, \\,"," z \\, < \\, x")
        suppose1[1].set_color(YELLOW)
        then1 = TexMobject("z^{z}\\, <\\,",  "x", "^z","<", "x", "^x")

        then1.set_color_by_tex("x", YELLOW)
        then1.set_color_by_tex("z", YELLOW)
        then1[0].set_color(WHITE)
        then1[1].set_color(WHITE)
        then1[4].set_color(WHITE)
      

        contra = TexMobject("z^{z}\\, < \\, x^{x}\\, ","\\Rightarrow \\, \\Leftarrow")

        suppose.move_to(DOWN)
        suppose1.move_to(DOWN)
        then1.move_to(DOWN*2)
        contra.move_to(DOWN*3)
        contra[1].set_color(RED)
        self.play(FadeIn(suppose))
        self.play(FadeIn(then1[0:3]))
        self.wait()
        self.play(Transform(suppose[1],suppose1[1]))
        self.play(FadeIn(then1[3:6]))
        self.wait()
        self.play(FadeIn(contra[0]))
        self.wait()
        self.play(FadeIn(contra[1]))
        self.wait()
        self.play(Uncreate(contra), Uncreate(then1), Uncreate(suppose))

        self.wait()
        self.play(Transform(gr3, gr33))
        self.wait()

        ineq_final = TexMobject("z","^z", "\\, \\geq \\," , " (x\\, +\\, 1)", "^{x\\, +\\, 1}", "\\, =\\, (x\\, +\\, 1)", "(x\\, +\\, 1)^{x}")
        ineq_final.move_to(DOWN)
        ineq_final[1].set_color(YELLOW)
        ineq_final[4].set_color(YELLOW)

        ineq_final1 = TexMobject("z","^z", "\\, \\geq \\," , " (x\\, +\\, 1)", "^{x\\, +\\, 1}", "\\, \\geq \\, 2", "(x\\, +\\, 1)^{x}")
        ineq_final11 = TexMobject("z","^z", "\\, \\geq \\," , " (x\\, +\\, 1)", "^{x\\, +\\, 1}", "\\, > \\, 2\\,", "x^{x}")
        
        ineq_final1.move_to(DOWN*2 + LEFT)
        
        ineq_final11.move_to(DOWN*3 + LEFT)

        final1 = TexMobject("z","^z", "\\, > \\, 2\\,", "x^{x}")
        final2 = TexMobject("z","^z", "\\, > \\, 2\\,", "y^{y}")

        final1.move_to(DOWN)
        final2.move_to(DOWN*2)

        self.play(Write(ineq_final[0]), Write(ineq_final[2]), Write(ineq_final[3]))
        self.wait()
        self.play(Write(ineq_final[1]), Write(ineq_final[4]))
        self.wait()
        self.play(Write(ineq_final[5]), Write(ineq_final[6]))
        self.play(Write(ineq_final1[5]), Write(ineq_final1[6]))
        self.play(Write(ineq_final11[5]), Write(ineq_final11[6]))

        self.play(Uncreate(ineq_final1[5:7]), Uncreate(ineq_final11[5:7]), Transform(ineq_final, final1))
        self.play(FadeIn(final2))
        self.wait()

        add1 = TexMobject("2z^{z}\\, > \\, 2(x^{x}\\, +\\, y^{y})")
        add2 = TexMobject("z^{z}\\, > \\, x^{x}\\, +\\, y^{y}")

        add1.move_to(DOWN*3)
        add1.set_color(BLUE)

        add2.move_to(DOWN*3)
        add2.set_color(BLUE)

        self.play(Write(add1))
        self.wait()
        self.play(Transform(add1,add2))
        self.wait()
