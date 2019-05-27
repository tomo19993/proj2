from Polygon import Polygon
import math
class RegularHexagon(Polygon):
    def __init__(self,left_bottom,base_length,fill_color,outline_color):
        points=[left_bottom]
        points.append((left_bottom[0],left_bottom[1]))
        points.append((left_bottom[0]+0.5*base_length,left_bottom[1]+math.sqrt(2)/2*base_length))
        points.append((left_bottom[0]+1.5*base_length,left_bottom[1]+math.sqrt(2)/2*base_length))
        points.append((left_bottom[0]+2*base_length,left_bottom[1]))
        points.append((left_bottom[0]+1.5*base_length,left_bottom[1]-math.sqrt(2)/2*base_length))
        points.append((left_bottom[0]+0.5*base_length,left_bottom[1]-math.sqrt(2)/2*base_length))

        super(RegularHexagon,self).__init__(points, fill_color,outline_color)


    def area(self):
        return (math.sqrt(3)*self.base_lenght ** 2 )/4
