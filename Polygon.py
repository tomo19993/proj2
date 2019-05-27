from abc import ABCMeta, abstractmethod
import math
import tkinter

class Polygon:
    __metaclass__ = ABCMeta

    def __init__(self,points,color,outline_color):
        self.color = color
        self.outline_color = outline_color
        self.points = points


    def draw(self):
        top = tkinter.Tk()
        canvas = tkinter.Canvas(top, bg="white", height=800, width=800)
        canvas.create_polygon(self.points,fill = self.color,outline = self.outline_color)
        canvas.pack()
        top.mainloop()

    @abstractmethod
    def area(self):
        pass


    def set_fill_color(self,color):
        self.color = color

    def size_line(self, x):
        if(x==len(self.points)):
            return math.sqrt((self.points[0][1]-self.points[x-1][1])**2+(self.points[0][0]-self.points[x-1][0])**2)
        return math.sqrt((self.points[x][1]-self.points[x-1][1])**2+(self.points[x][0]-self.points[x-1][0])**2)
