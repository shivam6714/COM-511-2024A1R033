"""Create a student class and object: Student details
    Problem: Create a student class to store a students name and roll number. 
    Create an object and display the details using an instance method
"""

class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number

    def display_details(self):
        print("Name:",self.name)
        print("Roll Number:",self.roll_number)

student1= Student("Sher Khan", 25)
student1.display_details()