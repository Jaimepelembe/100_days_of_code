class Car:

    def __init__(self,brand,model):
        self.seats=5
        self.brand=brand
        self.model=model
    def enterRaceMode(self):
        """Turns the car into a race car, removing the seats."""
        self.seats=2 