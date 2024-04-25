class Vehicle:
    def __init__(self, plate_n, color, wheels_n, capacity, ):
        self.__plate_n = plate_n
        self.__color = color
        self.__wheels_n = wheels_n
        self.__capacity = capacity
        
    @property
    def plate_n(self):
        return self.__plate_n

    @plate_n.setter
    def plate_n(self, value):
        # if len(value) < 1:
        #     raise Exception('The name is too long!')
        self.__plate_n = value
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__plate_n}', {self.__color}, {self.__wheels_n}, {self.__capacity})"