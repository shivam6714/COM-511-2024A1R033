"""write a pyhton program to take a 2-digit number as input and the sum of digits"""

num=int(input())
a=num%10
num//=10
b=num%10
sum=a+b
print(f"Sum of its digits are {sum}")