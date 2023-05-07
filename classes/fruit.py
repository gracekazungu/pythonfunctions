class Fruit:

    def __init__(self,fruit_name,fruit_color,fruit_size,price,taste):
        self.fruit_name=fruit_name
        self.fruit_color=fruit_color
        self.fruit_size=fruit_size
        self.price=price
        self.taste=taste

    def fruit_description(self):
        return f"The {self.fruit_name} of {self.fruit_size} size is {self.fruit_color} in color"
    
    def make_juice(self):
        return f"We make {self.taste} from {self.fruit}"

    def discount(self):
        self.no_fruits_bought=34
        self.total=self.price*self.no_fruits_bought
        if self.total>700:
            self.selling_price=self.total*30/100
        return self.selling_price





    