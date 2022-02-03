from manim import *
import time

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class Opening(Scene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )
        t0 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],
             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )
        t2 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )
        '''
        for j in range(4):
            for i in range(4):
                highlight = t0.get_highlighted_cell((2+i,2+j), color=GREEN)
                t0.add_to_back(highlight)
        t0.remove(*t0.get_vertical_lines())
        t0.remove(*t0.get_horizontal_lines())
        '''

        t0.scale(0.5)
        t1.scale(0.5)
        t2.scale(0.5)

        t0.remove(*t0.get_rows()[8])
        t1.remove(*t1.get_rows()[8])
        #t1.remove(*t1.get_vertical_lines())

        #self.play(t1.create())
        #self.wait()
        #self.add(t0)
        self.play(t0.create(), run_time = 4)

        self.add(t1)
        self.wait(0.2)

        for j in range(3):
            self.wait(0.1)
            t1.add_highlighted_cell((j+1,4), color=GREEN)
            self.wait(0.1)
            t1.add_highlighted_cell((4,j+1), color=GREEN)
            self.wait(0.1)

        t1.add_highlighted_cell((4,4), color=YELLOW)
        self.wait(0.1)

        for i in range(7):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,7), color=GREEN)
            self.wait(0.1)
            if i < 6:
                t1.add_highlighted_cell((8,i+1), color=GREEN)
                self.wait(0.1)
        
        t1.add_highlighted_cell((8,7), color=YELLOW)

        for i in range(5):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,2), color=GREEN)
            self.wait(0.1)
            if i < 1:
                t1.add_highlighted_cell((6,i+1), color=GREEN)
                self.wait(0.1)
        t1.add_highlighted_cell((6,2), color=YELLOW)

        self.wait()





class Ex1(MovingCameraScene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )
        t0 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],
             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )
        t2 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )
        prod = MathTex("4\\cdot 25","=","10 \\cdot 10")
        prod1 = MathTex("54\\cdot 56","=","42 \\cdot 72")

        prod[0].set_color(RED)
        prod[2].set_color(PURPLE_B)

        prod1[0].set_color(YELLOW)
        prod1[2].set_color(PURE_GREEN)
        
        prod.move_to(RIGHT*6 + UP*2)
        prod1.move_to(RIGHT*6 + DOWN*2)
        '''
        for j in range(4):
            for i in range(4):
                highlight = t0.get_highlighted_cell((2+i,2+j), color=GREEN)
                t0.add_to_back(highlight)
        t0.remove(*t0.get_vertical_lines())
        t0.remove(*t0.get_horizontal_lines())
        '''

        t0.scale(0.5)
        t1.scale(0.5)
        t2.scale(0.5)

        t0.remove(*t0.get_rows()[8])
        t1.remove(*t1.get_rows()[8])
        #t1.remove(*t1.get_vertical_lines())

        #self.play(t1.create())
        #self.wait()
        #self.add(t0)
        self.play(t0.create())
        self.add(t1)
        self.wait(0.2)

        for j in range(4):
            for i in range(4):
                self.wait(0.1)
            #highlight = 
                t1.add_highlighted_cell((2+i,2+j), color=GREEN)
        self.wait(0.1)

        d1 = VGroup(t1.get_cell((2,2)), t1.get_cell((5,5)))
        d2 = VGroup(t1.get_cell((5,2)), t1.get_cell((2,5)))


        d11 = VGroup(t1.get_cell((9,6)), t1.get_cell((7,8)))
        d22 = VGroup(t1.get_cell((7,6)), t1.get_cell((9,8)))

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(RIGHT*2))

        #t1.add_highlighted_cell((2,2), color = RED)
        #t1.add_highlighted_cell((5,5), color = RED)
        self.wait(0.1)
        t1.add(t2.get_cell((2,2), color=RED))
        self.wait(0.5)
        t1.add(t2.get_cell((5,5), color=RED))
        self.wait(0.1)
        self.play(TransformFromCopy(d1, prod[0]), run_time = 2)
        self.wait()
        t1.add(t2.get_cell((2,5), color=PURPLE_B))
        self.wait(0.1)
        t1.add(t2.get_cell((5,2), color=PURPLE_B))
        self.wait()
        self.play(TransformFromCopy(d2, prod[2]), run_time = 2)
        self.wait()
        self.play(Write(prod[1]))


        self.wait(1)
        t1.add(t2.get_cell((9,6), color=YELLOW))
        t1.add(t2.get_cell((7,8), color=YELLOW))
        self.wait()
        self.play(TransformFromCopy(d11, prod1[0]), run_time = 2)
        self.wait()

        t1.add(t2.get_cell((7,6), color=PURE_GREEN))
        t1.add(t2.get_cell((9,8), color=PURE_GREEN))
        self.wait()
        self.play(TransformFromCopy(d22, prod1[2]), run_time = 2)
        self.wait(0.5)
        self.play(Write(prod1[1]))
        self.wait(1)

       




class Ex2(MovingCameraScene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )

        t1.scale(0.5)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(RIGHT*2))

        self.add(t1)
        self.wait(0.2)
        summ1 = MathTex("16","+20","+24","+28","+32")
        summ2 = MathTex("20","+25","+30","+35","+40")
        summ3 = MathTex("24","+30","+36","+42","+48")
        summ4 = MathTex("28","+35","+42","+49","+56")
        summ5 = MathTex("32","+40","+48","+56","+64")

        summ_tot = MathTex("= 900")
        summ_tot1 = MathTex("= 30^{2}")

        summ1.move_to(RIGHT*6 + UP*2)
        summ2.move_to(RIGHT*6 + UP*1)
        summ3.move_to(RIGHT*6 )
        summ4.move_to(RIGHT*6 + DOWN*1)
        summ5.move_to(RIGHT*6 + DOWN*2)
        summ_tot.move_to(RIGHT*6 + DOWN*3)
        summ_tot1.move_to(RIGHT*6 + DOWN*3)

        summ_tot.set_color(YELLOW)
        summ_tot1.set_color(YELLOW)


        summ1.scale(0.8)
        summ2.scale(0.8)
        summ3.scale(0.8)
        summ4.scale(0.8)
        summ5.scale(0.8)


        for j in range(5):
            for i in range(5):
                self.wait(0.1)
                t1.add_highlighted_cell((4+i,4+j), color=GOLD_C)
        self.wait(0.2)

        for m in range(5):
            self.wait(0.1)
            self.play(TransformFromCopy(t1.get_cell((4,4+m)), summ1[m] ), run_time = 0.1 )

        for m in range(5):
            self.wait(0.1)
            self.play(TransformFromCopy(t1.get_cell((5,4+m)), summ2[m] ), run_time = 0.1 )

        for m in range(5):
            self.wait(0.1)
            self.play(TransformFromCopy(t1.get_cell((6,4+m)), summ3[m] ), run_time = 0.1 )

        for m in range(5):
            self.wait(0.1)
            self.play(TransformFromCopy(t1.get_cell((7,4+m)), summ4[m] ), run_time = 0.1 )

        for m in range(5):
            self.wait(0.1)
            self.play(TransformFromCopy(t1.get_cell((8,4+m)), summ5[m] ), run_time = 0.1 )

        self.wait(0.2)
        self.play(Write(summ_tot))
        self.wait(0.5)
        self.play(ReplacementTransform(summ_tot,summ_tot1))
        self.wait()
        

class Ex3(MovingCameraScene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )

        t1.scale(0.5)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(RIGHT*2 + DOWN*0.4))

        self.add(t1)
        self.wait(0.2)

        sum_v = MathTex("24")
        sum_h = MathTex("24")
        sum_v.move_to(DOWN*3.5 + LEFT*0.9)
        sum_h.move_to(RIGHT*6 + UP*1.4)

        sum_v.set_color(BLUE)
        sum_h.set_color(BLUE)

        t1.add_highlighted_cell((1,4), color=BLUE)
        self.wait(0.1)
        t1.add_highlighted_cell((3,2), color=BLUE)
        self.wait(0.1)
        t1.add_highlighted_cell((5,4), color=BLUE)
        self.wait(0.1)
        t1.add_highlighted_cell((3,6), color=BLUE)
        self.wait(0.1)

        g1 = VGroup(t1.get_cell((1,4)), t1.get_cell((5,4)) )
        g2 = VGroup(t1.get_cell((3,2)), t1.get_cell((3,6)) )

        self.play(TransformFromCopy(g1, sum_v), run_time = 2)
        self.wait(0.2)
        self.play(TransformFromCopy(g2, sum_h), run_time = 2)
        self.wait(2)


class Ex4(MovingCameraScene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )

        t1.scale(0.5)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(RIGHT*2 + DOWN*0.4))

        self.add(t1)
        self.wait(0.2)

        avg = MathTex("10","+54","+18","+30")
        avg1 = MathTex("\\frac{10 +54 +18 +30}{4}","= 28")

        avg.move_to(RIGHT*6 + UP)
        avg1.move_to(RIGHT*6.2 + UP)

        t1.add_highlighted_cell((5,2), color=RED)
        t1.add_highlighted_cell((5,6), color=RED)
        t1.add_highlighted_cell((9,2), color=RED)
        t1.add_highlighted_cell((9,6), color=RED)

        self.wait(0.2)
        t1.add_highlighted_cell((7,4), color=YELLOW)
        self.wait(0.2)

        self.play(TransformFromCopy(t1.get_cell((5,2)), avg[0]), run_time = 0.5)
        self.wait(0.2)
        self.play(TransformFromCopy(t1.get_cell((9,6)), avg[1]), run_time = 0.5)
        self.wait(0.2)
        self.play(TransformFromCopy(t1.get_cell((9,2)), avg[2]), run_time = 0.5)
        self.wait(0.2)
        self.play(TransformFromCopy(t1.get_cell((5,6)), avg[3]), run_time = 0.5)
        self.wait(0.2)

        self.play(Transform(avg, avg1[0]))
        self.wait(0.2)
        self.play(TransformFromCopy(t1.get_cell((7,4)), avg1[1]), run_time = 1)
        self.wait()

class prove(Scene):
    def construct(self):
        pr = Text("Prove it !")

        pr.scale(1.5)
        self.play(Write(pr))
        self.wait()
#260 tot 13 elements
class Ex5(MovingCameraScene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )

        t1.scale(0.5)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(RIGHT*2 + DOWN*0.4))

        self.add(t1)
        self.wait(0.2)

        avg = MathTex("9","+24","+12","+35")
        avg1 = MathTex("\\frac{9 +24 +12 +35}{4}","= 20")

        tot = MathTex("Total","= ","20\\cdot","13")

        tot[0].set_color(RED)
        tot[1].set_color(YELLOW)

        avg.move_to(RIGHT*6 + UP)
        avg1.move_to(RIGHT*6.2 + UP)

        tot.move_to(RIGHT*6.2 + UP)

        t1.add_highlighted_cell((3,3), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((4,6), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((6,2), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((7,5), color=RED)
        self.wait(2)

        t1.add_highlighted_cell((5,4), color=YELLOW)

        self.play(TransformFromCopy(t1.get_cell((3,3)), avg[0]), run_time = 0.5)
        self.wait(0.2)
        self.play(TransformFromCopy(t1.get_cell((4,6)), avg[1]), run_time = 0.5)
        self.wait(0.2)
        self.play(TransformFromCopy(t1.get_cell((6,2)), avg[2]), run_time = 0.5)
        self.wait(0.2)
        self.play(TransformFromCopy(t1.get_cell((7,5)), avg[3]), run_time = 0.5)
        self.wait(0.2)

        self.play(Transform(avg, avg1[0]))
        self.wait(0.2)
        self.play(TransformFromCopy(t1.get_cell((5,4)), avg1[1]), run_time = 1)
        self.wait()

        self.play(Uncreate(avg), Uncreate(avg1))
        self.wait()
        t1.add_highlighted_cell((4,3), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((4,4), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((4,5), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((5,3), color=RED)
        self.wait(0.1)

        t1.add_highlighted_cell((5,4), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((5,5), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((6,3), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((6,4), color=RED)
        self.wait(0.1)
        t1.add_highlighted_cell((6,5), color=RED)
        self.wait(0.1)

        g3 = VGroup(t1.get_cell((3,3)), t1.get_cell((4,6)), t1.get_cell((6,2)),
                    t1.get_cell((7,5)), t1.get_cell((5,4)), t1.get_cell((4,3)),
                    t1.get_cell((4,4)), t1.get_cell((4,5)), t1.get_cell((5,3)),
                    t1.get_cell((5,5)),t1.get_cell((6,3)),
                    t1.get_cell((6,4)),t1.get_cell((6,5)))

        self.wait(2)
        self.play(Write(tot[0]))
        self.wait()
        self.play(TransformFromCopy(t1.get_cell((5,4)), tot[1:3]), run_time = 1)
        self.wait()
        self.play(TransformFromCopy(g3, tot[3]))
        self.wait()

class Whole(MovingCameraScene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )
        t1.scale(0.5)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(RIGHT*2 + DOWN*0.4))

        self.add(t1)
        self.wait(0.2)

        summ = MathTex("\\sum_{i=1}^{9} \\sum_{j=1}^{9} ij "," = ","25 \\cdot","81")
        equals = MathTex("= 2025")
        summ.move_to(RIGHT*6)
        equals.move_to(RIGHT*6 + DOWN)

        self.play(Write(summ[0:2]))
        self.wait(0.5)
        t1.add_highlighted_cell((5,5), color=YELLOW)
        self.wait(0.5)
        self.play(TransformFromCopy(t1.get_cell((5,5)), summ[2]))
        self.play(TransformFromCopy(t1, summ[3]))
        self.play(Write(equals))
        self.wait()

class Corners(MovingCameraScene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )

        t1.scale(0.5)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(RIGHT*2 + DOWN*0.4))

        self.add(t1)
        self.wait(0.2)

        equa = MathTex("(1+2+3+...+n)^{2} = 1^{3} + 2^{3} + 3^{3}+... +n^{3}")
        equa.scale(0.8)
        equa.move_to(DOWN*3.7 + RIGHT*2)

        for i in range(2):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,2), color=RED)
            if i < 1:
                t1.add_highlighted_cell((2,i+1), color=RED)
                self.wait(0.1)

        g1 = VGroup(t1.get_cell((1,2)), t1.get_cell((2,2)), t1.get_cell((2,1)) )

        sum1 = MathTex("2 + 4 + 2")
        sum11 = MathTex("8")

        sum1.scale(0.8)
        sum11.scale(0.8)

        sum1.move_to(RIGHT*6 + UP*2)
        sum11.move_to(RIGHT*6 + UP*2)

        for i in range(3):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,3), color=GREEN)
            if i < 2:
                t1.add_highlighted_cell((3,i+1), color=GREEN)
                self.wait(0.1)

        g2 = VGroup(t1.get_cell((1,3)), t1.get_cell((2,3)), t1.get_cell((3,3)),
        t1.get_cell((3,1)),t1.get_cell((3,2)) )

        sum2 = MathTex("3 + 6 + 9 + 6 + 3")
        sum22 = MathTex("27")

        sum2.scale(0.8)
        sum22.scale(0.8)

        sum2.move_to(RIGHT*6 + UP)
        sum22.move_to(RIGHT*6 + UP)

        for i in range(4):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,4), color=RED)
            if i < 3:
                t1.add_highlighted_cell((4,i+1), color=RED)
                self.wait(0.1)
        g3 = VGroup(t1.get_cell((1,4)), t1.get_cell((2,4)), t1.get_cell((3,4)),
        t1.get_cell((4,4)),t1.get_cell((4,1)), t1.get_cell((4,2)),t1.get_cell((4,3)) )

        sum3 = MathTex("4 + 8 + 12 + 16 + 12 + 8 + 4")
        sum33 = MathTex("64")

        sum3.scale(0.8)
        sum33.scale(0.8)

        sum3.move_to(RIGHT*6 )
        sum33.move_to(RIGHT*6 )

        for i in range(5):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,5), color=BLUE)
            if i < 4:
                t1.add_highlighted_cell((5,i+1), color=BLUE)
                self.wait(0.1)

        for i in range(6):
            self.wait(0.09)
            t1.add_highlighted_cell((i+1,6), color=GREEN)
            if i < 5:
                t1.add_highlighted_cell((6,i+1), color=GREEN)
                self.wait(0.09)

        for i in range(7):
            self.wait(0.09)
            t1.add_highlighted_cell((i+1,7), color=RED)
            if i < 6:
                t1.add_highlighted_cell((7,i+1), color=RED)
                self.wait(0.09)

        for i in range(8):
            self.wait(0.09)
            t1.add_highlighted_cell((i+1,8), color=BLUE)
            if i < 7:
                t1.add_highlighted_cell((8,i+1), color=BLUE)
                self.wait(0.09)

        for i in range(9):
            self.wait(0.09)
            t1.add_highlighted_cell((i+1,9), color=GREEN)
            if i < 8:
                t1.add_highlighted_cell((9,i+1), color=GREEN)
                self.wait(0.09)
        self.wait(1)

        self.play(TransformFromCopy(g1, sum1))
        self.wait(0.2)
        self.play(Transform(sum1, sum11))
        self.wait(1)

        self.play(TransformFromCopy(g2, sum2))
        self.wait(0.2)
        self.play(Transform(sum2, sum22))
        self.wait(1)

        self.play(TransformFromCopy(g3, sum3))
        self.wait(0.2)
        self.play(Transform(sum3, sum33))
        self.wait()
        self.play(Write(equa))
        self.wait(1)



class Ques(MovingCameraScene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )

        t1.scale(0.5)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(RIGHT*2 + DOWN*0.4))

        self.add(t1)
        self.wait(0.2)

        seq1 = MathTex("{2,6,12,20,30,42,56,72}")
        seq2 = MathTex("{3,8,15,24,35,48,63}")
        seq3 = MathTex("{4,10,18,28,40,54}")
        seq4 = MathTex("{5,12,21,32,45}")

        seq1.move_to(RIGHT*6 + UP)
        seq2.move_to(RIGHT*6 )
        seq3.move_to(RIGHT*6 + DOWN)
        seq4.move_to(RIGHT*6 + DOWN*2)

        for i in range(8):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,2 + i), color=BLUE)

        for i in range(7):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,3 + i), color=GREEN)

        for i in range(6):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,4 + i), color=RED)

        for i in range(5):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,5 + i), color=BLUE)

        for i in range(4):
            self.wait(0.1)
            t1.add_highlighted_cell((i+1,6 + i), color=GREEN)
        self.wait()

        self.play(Write(seq1))
        self.play(Write(seq2))
        self.play(Write(seq3))
        self.play(Write(seq4))



class TableExamples(Scene):
    def construct(self):
        t1 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],

             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )
        t0 = Table(
            [[" 1", " 2"," 3"," 4", " 5"," 6"," 7", " 8"," 9"],
             ["2", "4","6","8", "10","12","14", "16","18"],
             ["3", "6","9","12", "15","18","21", "24","27"],
             ["4", "8","12","16", "20","24","28", "32","36"],
             ["5", "10","15","20", "25","30","35", "40","45"],
             ["6", "12","18","24", "30","36","42", "48","54"],
             ["7", "14","21","28", "35","42","49", "56","63"],
             ["8", "16","24","32", "40","48","56", "64","72"],
             ["9 ", "18","27","36", "45","54","63", "72","81"]],
             include_outer_lines = True,
             h_buff=0.8,
             v_buff=0.9,
            #row_labels=[Text("R1"), Text("R2")],
            #col_labels=[Text("C1"), Text("C2")],
            #top_left_entry=Text("TOP")
            )
        '''
        for j in range(4):
            for i in range(4):
                highlight = t0.get_highlighted_cell((2+i,2+j), color=GREEN)
                t0.add_to_back(highlight)
        t0.remove(*t0.get_vertical_lines())
        t0.remove(*t0.get_horizontal_lines())
        '''

        t0.scale(0.5)
        t1.scale(0.5)

        t0.remove(*t0.get_rows()[8])
        t1.remove(*t1.get_rows()[8])
        #t1.remove(*t1.get_vertical_lines())

        #self.play(t1.create())
        #self.wait()
        #self.add(t0)
        self.add(t1)
        #self.play(TransformFromCopy(t1,t0))
        
        #self.play(t0.create(), run_time = 2)
        #self.play(t0.add_highlighted_cell((2,2), color=GREEN),run_time = 1 )
        self.wait()

        for j in range(4):
            for i in range(4):
            #highlight = 
                t0.add_highlighted_cell((2+i,2+j), color=GREEN)
            #t0.add_to_back(highlight)
                #self.wait(0.1)

        #t0.remove(*t0.get_vertical_lines())
        self.wait()

      
        
      



