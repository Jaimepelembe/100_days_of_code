class RGBColor:

    def __init__(self):
        """Initialize an empty RGB color."""
        self.color=()

    def generateRandomColor(self):
        """Generate a random RGB color."""
        from random import randint
        red=randint(0,255)
        green=randint(0,255)
        blue=randint(0,255)

        self.color=(red,green,blue)


