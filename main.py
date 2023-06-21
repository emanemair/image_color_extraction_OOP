from colorextraction import ColorExtraction
from displaycolor import Display
number_of_color=int(input("enter number of color : 1-15"))
color_extraction = ColorExtraction("color.jpg" , number_of_color)
colors =color_extraction.colors_to_rgb()
color_file = open("color.txt" , "w")
color_file.write(str(colors))
color_file.close()
screen=Display(colors)
screen.draw()
