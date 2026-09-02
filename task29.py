"""Write a python program to take a student name and roll number, then generate a username using the first three letter of the name and last two digits of the roll number"""
name=input()
roll=input()

print(name[:3]+roll[-2:])