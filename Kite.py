from Quadrilateral import Quadrilateral
import math
class Kite(Quadrilateral):
    def __init__(self,left_bottom,angle ,diagonal_ac,diagonal_bd, fill_color,outline_color):

        b = math.cos(angle)*0.5*diagonal_ac
        points = [left_bottom]
        points.append((left_bottom[0]+0.5*diagonal_ac,left_bottom[1]+0.5*diagonal_bd))
        points.append((left_bottom[0]+diagonal_ac,left_bottom[1]))
        points.append((left_bottom[0]+0.5*diagonal_ac,left_bottom[1]-0.5*diagonal_bd))


        super(Kite,self).__init__(points,fill_color,outline_color)
