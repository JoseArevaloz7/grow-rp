from vehicle import Vehicle

class Moto(Vehicle):
    def __init__(self, plate_n, color, wheels_n, capacity):
        super().__init__(plate_n, color, wheels_n, capacity)
        
        self.__model = 'Motocycle'
        
    @property
    def model(self):
        return self.__model 
    
    def pr(self):
        return self.plate_n

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.plate_n}', {self.color}, {self.wheels_n}, {self.capacity}, {self.model})"