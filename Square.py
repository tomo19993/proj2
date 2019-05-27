from Quadrilateral import Quadrilateral
import math
class Square(Quadrilateral):
    def __init__(self,left_bottom,base_length,fill_color,outline_color):
        points=[left_bottom]
        points.append((left_bottom[0]+base_length,left_bottom[1]))
        points.append((left_bottom[0]+base_length,left_bottom[1]+base_length))
        points.append((left_bottom[0],left_bottom[1]+base_length))

        super(Square,self).__init__(points, fill_color,outline_color)
