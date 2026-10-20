# class, method

class Car:
    def __init__ (self,brand_name,brand_color,price):
        self.brand=brand_name
        self.color=brand_color
        self.price=price
        
    def start(self):
        print(f"Brand name: {self.brand}")

        
car_one=Car("Tyota","White",3200000)

print(car_one.price)
car_one.start()