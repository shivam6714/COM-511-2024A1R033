"""Print true if student atlesat 40 in all 3 subjects and averge marks are atleast 50 else false"""
marks1=int(input())
marks2=int(input())
marks3=int(input())
print(marks1>=40 and marks2>=40 and marks3>=40 and ((marks1+marks2+marks3)/3)>=50)