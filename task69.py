"""wap to make two list of even or odd number"""

ls = list(map(int, input("Enter numbers: ").split()))
odd=[]
even=[]

for x in ls:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)


print("Even: ",even)
print("Odd: ",odd)
