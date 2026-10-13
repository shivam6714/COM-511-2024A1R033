"""Create a product class with the product name, price, and quantity. Add an 
   instance method to calculate the total cost. Take these values from the user and display
   the product name and total cost.
"""

class Product:
    def __init__(self,name,price,quant):
        self.name=name
        self.price=price
        self.quant=quant
    def cost(self):
        return self.price*self.quant

    def display(self):
        print(f"Name of product is {self.name} and total cost is {self.cost()}")
p1=Product("Potato",10,100)
p1.display()