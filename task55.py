"""Perfect number"""

n=int(input("Enter number: "))

org=n

sum = 0
divisor = 1

while divisor<n:
    if n%divisor==0:
        sum+=divisor
    divisor+=1

if sum==org and org>1:
    print("Perfect NUmmber")
else:
    print("Not Perfect Number")