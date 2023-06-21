import colorgram

class ColorExtraction:
    def __init__(self,image , color_number ):
        self.image=image
        self.color_number=color_number
    def __str__(self):
        return (f"image file :{self.image} , number of color {self.number_color}")

    def print_image(self):
        '''
        print the image file
        :return:
        '''
        print(f"{self.image}")
    def print_color_number(self):
        '''
        print the color numbers
        :return:
        '''
        print(f"{self.print_color_number()}")

    def extract_colors(self):
        '''
        function to extract number of color from image
        :return:colors extracted
        '''
        return colorgram.extract(self.image ,self.color_number)
    def colors_to_rgb(self):
        colors=self.extract_colors()
        rgb_color=[]
        for color in colors:
            r=color.rgb.r
            g=color.rgb.g
            b=color.rgb.b
            new_color=(r,g,b)
            rgb_color.append(new_color)

        return rgb_color

