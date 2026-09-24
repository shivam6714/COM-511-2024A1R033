"""WAP to store one studnet data as a tuple: name, roll no , and amrks display  the grades based on marks"""

student = input("Enter Name of student: ")
roll = int(input("Enter Roll no: "))
marks = int(input("Enter marks: "))

lst=[]
lst.append(student)
lst.append(roll)
lst.append(marks)

grade =""

if marks>=90:
    grade+="A"
elif marks>=75:
    grade+="B"
elif marks>=60:
    grade+="C"
elif marks>=33:
    grade+="D"
else:
    grade+="Fail"


lst.append(grade)
tup=tuple(lst)

print("Student data: ",tup)
