"""WAP to input numbers in a list and find the second largest number"""

ls = list(map(int, input("Enter numbers: ").split()))

largest = float('-inf')
second  = float('-inf')

for i in ls:
    if i > largest:
        second  = largest  
        largest = i
    elif i < largest and i > second:
        second = i

print("Second largest: ",second)    