from Polygon import Polygon
import math
class RegularPentagon(Polygon):
    def __init__(self,central_point,radius,fill_color,outline_color):
        points=[central_point]
        for i in range (0,6):
            points.append((central_point[0]+radius*math.cos(2*math.pi*i/5),central_point[1]+ radius*math.sin(2*math.pi*i/5)))

        super(RegularPentagon,self).__init__(points, fill_color,outline_color)


    def area(self):
        return (math.sqrt(3)*self.base_lenght ** 2 )/4
