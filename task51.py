"""input a number and check whether it is prime or not. A number is prime if it has no divisor other than 1 and itself"""

number=int(input("Enter a number: "))

if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is a prime number")