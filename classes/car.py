class Car:
    def __init__(self,make,model,speed,color,reg_number):
        self.make=make
        self.speed=speed
        self.model=model
        self.color=color
        self.reg_number=reg_number

    def acceleration(self):
        self.accelerate=23
        return self.accelerate+self.speed

    def decceleration(self):
        self.deccelerate=45
        self.decceleration=self.speed-self.deccelerate
        return self.decceleration

    def car_description(self):
        return f"The {self.color} {self.make} model {self.model} of registration number {self.reg_number} is from Kenya"
