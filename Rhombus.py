from Quadrilateral import Quadrilateral
import math

class Rhombus(Quadrilateral):
    def __init__(self,left_bottom,angle ,diagonal, fill_color,outline_color):

        b= math.cos(angle)*0.5*diagonal
        points = [left_bottom]
        points.append((left_bottom[0]+0.5*diagonal,left_bottom[1]+0.5*diagonal))
        points.append((left_bottom[0]+diagonal,left_bottom[1]))
        points.append((left_bottom[0]+0.5*diagonal,left_bottom[1]-0.5*diagonal))


        super(Rhombus,self).__init__(points,fill_color,outline_color)
