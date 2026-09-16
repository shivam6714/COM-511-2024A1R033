"""WAP to repeatdely calculate the sum of digits of number until the result becomes a asingle digit"""

n = int(input("Enter a number: "))

while n >= 10:
    sum = 0

    while n > 0:
        sum += n % 10
        n //= 10

    n = sum

print("Single digit result:", n)