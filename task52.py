"""WAP to input two numbers and find GCD using a loop"""

num1 = int(input("Enter first number: "))   
num2 = int(input("Enter second number: "))

while num2!=0:
    num1,num2 = num2,num1%num2

gcd = num1

print("GCD: ",gcd)