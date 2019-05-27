import math

from Quadrilateral import Quadrilateral


class Parallelogram(Quadrilateral):
    def __init__(self,left_bottom,left_angle,base_len,height,fill_color,outline_color):
        angle = math.radians(left_angle)
        points = [left_bottom]
        points.append((left_bottom[0]+base_len,left_bottom[1]))
        x = left_bottom[0]+base_len+height/math.tan(angle)
        y = left_bottom[1]-height
        point = (left_bottom[0]+height/math.tan(angle),left_bottom[1]-height)
        points.append((x,y))
        points.append(point)


        super(Parallelogram,self).__init__(points,fill_color,outline_color)
