"""WAP to store multiple students data in tuple, each one conatins name, roll no, marks. Display who scored above 75"""

students = (
    ("Mohammad", 101, 85),
    ("Rahul", 102, 72),
    ("Aman", 103, 91),
    ("Rohit", 104, 68),
    ("Karan", 105, 78)
)

print("Students who scored above 75:")

for student in students:
    name, roll_no, marks = student

    if marks > 75:
        print(name, roll_no, marks)