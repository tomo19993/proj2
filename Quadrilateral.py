import math
from decimal import Decimal

from Polygon import Polygon


class Quadrilateral(Polygon):

    def __init__(self,points,fill_color,outline_color):
        super(Quadrilateral, self).__init__(points, fill_color, outline_color)



    def area(self):
        a = self.size_line(1)
        b = self.size_line(2)
        diagonal_length = math.sqrt(((self.points[2][1]-self.points[0][1])**2)+ ((self.points[2][0]-self.points[0][0])**2))
        angle = math.acos(((a** 2) + (b ** 2) - (diagonal_length ** 2)) / (2 * a * b))
        x = Decimal(a * b * math.sin(angle))
        return round(x, 3)



