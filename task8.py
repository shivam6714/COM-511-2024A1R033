"""Python program to calculate Simple Interest and total amounnt using Principal,rate, and time entered by user"""

p=int(input())
r=int(input())
t=int(input())
si=(p*r*t)/100
total=p+si
print("Simple Interest:",si)
print("Total:",total)