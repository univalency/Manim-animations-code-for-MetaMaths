from big_ol_pile_of_manim_imports import *
from numpy import sin, cos
import numpy as np
import scipy.integrate as integrate
from manimlib.imports import *

class Set1(GraphScene):
    CONFIG = {
    "y_max" : 13,
    "y_min" : 0,
    "x_max" : 20,
    "x_min" : 0,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 600,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "graph_origin": 3*DOWN,
    "axes_color" : GREY
    }
    def construct(self):
        self.graph_origin= 3*DOWN + 2*LEFT
        self.setup_axes(animate=True)


        point1=Dot(self.coords_to_point(10,8.04))
        point2=Dot(self.coords_to_point(8.0 , 6.95))
        point3=Dot(self.coords_to_point(13 , 7.58))
        point4=Dot(self.coords_to_point(9.0 , 8.81))
        point5=Dot(self.coords_to_point(11 , 8.33))
        point6=Dot(self.coords_to_point(14 , 9.96))
        point7=Dot(self.coords_to_point(6.0 , 7.24))
        point8=Dot(self.coords_to_point(4.0 , 4.26))
        point9=Dot(self.coords_to_point(12.0 , 10.84))
        point10=Dot(self.coords_to_point(7.0 , 4.82))
        point11=Dot(self.coords_to_point(5.0 , 5.68))

        line = self.get_graph(self.line,x_min= 0, x_max = 19, color=BLUE)

    
        self.play(ShowCreation(point1))
        self.play(ShowCreation(point2))
        self.play(ShowCreation(point3))
        self.play(ShowCreation(point4))
        self.play(ShowCreation(point5))
        self.play(ShowCreation(point6))
        self.play(ShowCreation(point7))
        self.play(ShowCreation(point8))
        self.play(ShowCreation(point9))
        self.play(ShowCreation(point10))
        self.play(ShowCreation(point11))
        self.wait(2)
        self.play(ShowCreation(line))
        self.wait()

    def line(self,x):
        return(0.5*x + 3)

class Set2(GraphScene):
    CONFIG = {
    "y_max" : 13,
    "y_min" : 0,
    "x_max" : 20,
    "x_min" : 0,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 600,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "graph_origin": 3*DOWN,
    "axes_color" : GREY
    }
    def construct(self):
        self.graph_origin= 3*DOWN + 2*LEFT
        self.setup_axes(animate=True)


        point1=Dot(self.coords_to_point(10,9.14))
        point2=Dot(self.coords_to_point(8.0 , 8.14))
        point3=Dot(self.coords_to_point(13 , 8.74))
        point4=Dot(self.coords_to_point(9.0 , 8.77))
        point5=Dot(self.coords_to_point(11 , 9.26))
        point6=Dot(self.coords_to_point(14 , 8.10))
        point7=Dot(self.coords_to_point(6.0 , 6.13))
        point8=Dot(self.coords_to_point(4.0 , 3.10))
        point9=Dot(self.coords_to_point(12.0 , 9.13))
        point10=Dot(self.coords_to_point(7.0 , 7.26))
        point11=Dot(self.coords_to_point(5.0 , 4.74))

        line = self.get_graph(self.line,x_min= 0, x_max = 19, color=BLUE)

    
        self.play(ShowCreation(point1))
        self.play(ShowCreation(point2))
        self.play(ShowCreation(point3))
        self.play(ShowCreation(point4))
        self.play(ShowCreation(point5))
        self.play(ShowCreation(point6))
        self.play(ShowCreation(point7))
        self.play(ShowCreation(point8))
        self.play(ShowCreation(point9))
        self.play(ShowCreation(point10))
        self.play(ShowCreation(point11))
        self.wait(2)
        self.play(ShowCreation(line))
        self.wait()

    def line(self,x):
        return(0.5*x + 3)

class Set3(GraphScene):
    CONFIG = {
    "y_max" : 13,
    "y_min" : 0,
    "x_max" : 20,
    "x_min" : 0,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 600,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "graph_origin": 3*DOWN,
    "axes_color" : GREY
    }
    def construct(self):
        self.graph_origin= 3*DOWN + 2*LEFT
        self.setup_axes(animate=True)


        point1=Dot(self.coords_to_point(10,7.46))
        point2=Dot(self.coords_to_point(8.0 , 6.77))
        point3=Dot(self.coords_to_point(13 , 12.74))
        point4=Dot(self.coords_to_point(9.0 , 7.11))
        point5=Dot(self.coords_to_point(11 , 7.81))
        point6=Dot(self.coords_to_point(14 , 8.84))
        point7=Dot(self.coords_to_point(6.0 , 6.08))
        point8=Dot(self.coords_to_point(4.0 , 5.39))
        point9=Dot(self.coords_to_point(12.0 , 8.15))
        point10=Dot(self.coords_to_point(7.0 , 6.42))
        point11=Dot(self.coords_to_point(5.0 , 5.73))

        line = self.get_graph(self.line,x_min= 0, x_max = 19, color=BLUE)

    
        self.play(ShowCreation(point1))
        self.play(ShowCreation(point2))
        self.play(ShowCreation(point3))
        self.play(ShowCreation(point4))
        self.play(ShowCreation(point5))
        self.play(ShowCreation(point6))
        self.play(ShowCreation(point7))
        self.play(ShowCreation(point8))
        self.play(ShowCreation(point9))
        self.play(ShowCreation(point10))
        self.play(ShowCreation(point11))
        self.wait(2)
        self.play(ShowCreation(line))
        self.wait()

    def line(self,x):
        return(0.5*x + 3)

class Set4(GraphScene):
    CONFIG = {
    "y_max" : 13,
    "y_min" : 0,
    "x_max" : 20,
    "x_min" : 0,
    "y_tick_frequency" : 1,
    "x_tick_frequency" : 1,
    "x_axis_width" : 6,
    "y_axis_height" : 6,
    "num_graph_anchor_points": 600,
    #"x_labeled_nums" : range(-15,16,1),
    #"y_labeled_nums" : range(-50,51,1),
    "graph_origin": 3*DOWN,
    "axes_color" : GREY
    }
    def construct(self):
        self.graph_origin= 3*DOWN + 2*LEFT
        self.setup_axes(animate=True)


        point1=Dot(self.coords_to_point(8.0 , 6.58))
        point2=Dot(self.coords_to_point(8.0 , 5.76))
        point3=Dot(self.coords_to_point(8.0 , 7.71))
        point4=Dot(self.coords_to_point(8.0 , 8.84))
        point5=Dot(self.coords_to_point(8.0 , 8.47))
        point6=Dot(self.coords_to_point(8.0 , 7.04))
        point7=Dot(self.coords_to_point(8.0 , 5.25))
        point8=Dot(self.coords_to_point(19.0 , 12.50))
        point9=Dot(self.coords_to_point(8.0 , 5.56))
        point10=Dot(self.coords_to_point(8.0 , 7.91))
        point11=Dot(self.coords_to_point(8.0 , 6.89))

        line = self.get_graph(self.line,x_min= 0, x_max = 19, color=BLUE)


    
        self.play(ShowCreation(point1))
        self.play(ShowCreation(point2))
        self.play(ShowCreation(point3))
        self.play(ShowCreation(point4))
        self.play(ShowCreation(point5))
        self.play(ShowCreation(point6))
        self.play(ShowCreation(point7))
        self.play(ShowCreation(point8))
        self.play(ShowCreation(point9))
        self.play(ShowCreation(point10))
        self.play(ShowCreation(point11))
        self.wait(2)
        self.play(ShowCreation(line))
        self.wait()

    def line(self,x):
        return(0.5*x + 3)
