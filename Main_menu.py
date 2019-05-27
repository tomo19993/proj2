
import sys


from Rhombus import Rhombus
from RegularHexagon import RegularHexagon
from RegularOctagon import RegularOctagon   ###########################  uncomment once TODOclasses are done  #####
from RegularPentagon import RegularPentagon
from Kite import Kite
from EquilateralTriangle import EquilateralTriangle
from IsoscelesTriangle import IsoscelesTriangle
from Square import Square
from Parallelogram import Parallelogram



colors = ["blue","red","grey","orange","black","yellow"]




class MainMenu:
    def __init__(self):
        self.choices = {
                "1": self.isosceles_triangle,
                "2": self.equilateral_triangle,
                "3": self.square,
                "4": self.parallelogram,
                "5": self.rhombus,
                "6": self.regular_hexagon,
                "7": self.regular_octagon,
                "8": self.regular_pentagon,
                "9": self.kite,
                "0": self.quit
                }
    @staticmethod
    def display_menu():
        print("""
            Polygon Menu
            Display:
            1. Isosceles Triangle
            2. Equilateral Triangle
            3. Square
            4. Parallelogram
            5. Rhombus
            6. Regular_Hexagon
            7. Regular_Octagon
            8. Regular_Pentagon
            9. Kite
            0. Quit
        """)
    @staticmethod
    def display_colors():
        print("Chose color:\n"
              "1. blue\n"
              "2. red\n"
              "3. grey\n"
              "4. orange\n"
              "5. black\n"
              "6. yellow \n")
    def isosceles_triangle(self):
        self.display_colors()
        fill_color = colors[int(input('choose fill color'))-1]
        outline_color = colors[ int(input('choose outline color'))-1]
        print(fill_color, outline_color)
        base_length = input('Provide base length')
        height = input('Provide triangle height')


        print(IsoscelesTriangle([800-int(base_length),int(height)],int(base_length),int(height),fill_color,outline_color).area())
        IsoscelesTriangle([800-int(base_length),int(height)],int(base_length),int(height),fill_color,outline_color).draw()


    def equilateral_triangle(self):
        self.display_colors()
        fill_color = colors[int(input('choose fill color'))-1]
        outline_color = colors[ int(input('choose outline color'))-1]
        print(fill_color, outline_color)
        base_length = input('Provide base length')

        print(EquilateralTriangle([000,400],int(base_length), fill_color,outline_color).area())
        EquilateralTriangle([000,400],int(base_length), fill_color,outline_color).draw()

    def square(self):
        self.display_colors()
        fill_color = colors[int(input('choose fill color'))-1]
        outline_color = colors[ int(input('choose outline color'))-1]
        base_length = input('Provide base length')

        print(Square([000,400],int(base_length), fill_color,outline_color).area())
        Square([000,400],int(base_length), fill_color,outline_color).draw()




    def parallelogram(self):
        self.display_colors()
        fill_color = colors[int(input('choose fill color'))-1]
        outline_color = colors[ int(input('choose outline color'))-1]
        print(fill_color, outline_color)
        left_angle = input('Provide left angle')
        base_length = input('Provide base length')
        height = input('Provide height')

        print(Parallelogram([000,400],int(left_angle),int(base_length),int(height), fill_color,outline_color).area())
        Parallelogram([000,400],int(left_angle),int(base_length),int(height), fill_color,outline_color).draw()


    def rhombus(self):
        self.display_colors()
        fill_color = colors[int(input('choose fill color'))-1]
        outline_color = colors[ int(input('choose outline color'))-1]
        print(fill_color, outline_color)
        angle = int(input('Provide left angle'))
        diagonal = int(input('Provide diagonal'))

        print(Rhombus([000,400],angle,diagonal,fill_color,outline_color).area())
        Rhombus([000,400],angle,diagonal,fill_color,outline_color).draw()


    def regular_hexagon(self):
        self.display_colors()
        fill_color = colors[int(input('choose fill color'))-1]
        outline_color = colors[ int(input('choose outline color'))-1]
        print(fill_color, outline_color)
        base_length = int(input('Provide base length'))

        print(RegularHexagon([400,400],base_length,fill_color,outline_color).area())
        RegularHexagon([400,400],base_length,fill_color,outline_color).draw()



    def regular_octagon(self):
        self.display_colors()
        fill_color = colors[int(input('choose fill color'))-1]
        outline_color = colors[ int(input('choose outline color'))-1]
        print(fill_color, outline_color)
        radius = int(input('Provide base length'))

        print(RegularOctagon([400,400],radius,fill_color,outline_color).area())
        RegularOctagon([400,400],radius,fill_color,outline_color).draw()


    def regular_pentagon(self):
        self.display_colors()
        fill_color = colors[int(input('choose fill color'))-1]
        outline_color = colors[ int(input('choose outline color'))-1]
        print(fill_color, outline_color)
        radius = int(input('Provide base length'))

        print(RegularPentagon([400,400],radius,fill_color,outline_color).area())
        RegularPentagon([400,400],radius,fill_color,outline_color).draw()


    def kite(self):
        self.display_colors()
        fill_color = colors[int(input('choose fill color'))-1]
        outline_color = colors[ int(input('choose outline color'))-1]
        print(fill_color, outline_color)
        angle = int(input('Provide left angle'))
        diagonal_ac = int(input('Provide diagonal_ac'))
        diagonal_bd = int(input('Provide diagonal_bd'))

        print(Kite([000,400],angle,diagonal_ac,diagonal_bd,fill_color,outline_color).area())
        Kite([100,400],angle,diagonal_ac,diagonal_bd,fill_color,outline_color).draw()



    @staticmethod
    def quit():
        print("Closing application")
        sys.exit(0)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))








if __name__ == "__main__":
    MainMenu().run()



