import math
from decimal import Decimal

from Polygon import Polygon

class Triangle(Polygon):

    def __init__(self,points,fill_color,outline_color):
        super(Triangle,self).__init__(points,fill_color,outline_color)


    def area(self):
        a = self.size_line(1)
        b = self.size_line(2)
        c = self.size_line(3)
        angle = math.acos(((a ** 2) + (b ** 2) - (c ** 2))/(2 * a * b))
        x = Decimal(a * b * math.sin(angle) * 0.5)
        return round(x, 3)


