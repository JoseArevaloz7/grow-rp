class Vehicle:
    def __init__(self, plate_n, color, wheels_n, capacity, ):
        self.__plate_n = plate_n
        self.__color = color
        self.__wheels_n = wheels_n
        self.__capacity = capacity
       
    # encapsulation
    # All of the variables are hidden to the users, it give more scurity and control to the code. 
    # Exmpl: self.__capacity = capacity
    # Not hidden: self.capacity = capacity
    @property
    def plate_n(self):
        return self.__plate_n
    @property
    def color(self):
        return self.__color
    @property
    def wheels_n(self):
        return self.__wheels_n
    @property
    def capacity(self):
        return self.__capacity
    
    # The setters allow you modify the specify variable.
    @plate_n.setter
    def plate_n(self, value):
        if len(value) < 8:
            raise Exception('The name is too short!')
        self.__plate_n = value
    ########################################
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__plate_n}', {self.__color}, {self.__wheels_n}, {self.__capacity})"