"""Instance methods: Rectangle area and perimeter
   Problem: Create a rectangle class with length and breadth. Use instance methods to calculate 
   its area and perimeter.
"""

class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of rectangle is :",(self.l)*(self.b))
    def perimeter(self):
        print("Perimeter of rectangle is :",2*(self.l+self.b))


rect=Rectangle(10,10)
rect.area()
rect.perimeter()