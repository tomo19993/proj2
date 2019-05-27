from Triangle import Triangle

class IsoscelesTriangle(Triangle):
    def __init__(self,left_bottom,base_length,height,fill_color,outline_color):
        points= [left_bottom]
        points.append((left_bottom[0]+base_length,left_bottom[1]))
        points.append((left_bottom[0]+(base_length/2),left_bottom[1]-height))
        print(points)
        super(IsoscelesTriangle,self).__init__(points,fill_color,outline_color)
