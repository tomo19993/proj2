from Polygon import Polygon
import math
class RegularOctagon(Polygon):
    def __init__(self,central_point,radius,fill_color,outline_color):
        points=[central_point] ###stuff from hexagon
        for i in range (0,9):
            points.append((central_point[0]+int(radius*math.cos(2*math.pi*i/8)),central_point[1]+ int(radius*math.sin(2*math.pi*i/8))))

        super(RegularOctagon,self).__init__(points, fill_color,outline_color)


    def area(self):
        return (math.sqrt(3)*self.base_lenght ** 2 )/4
