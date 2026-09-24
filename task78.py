"""WAP to check whether a given values is present in a tuple. If present, display its position"""

tup = (1,2,3,4,5,6)
target=int(input("Enter target value: "))
found=False
for i in range(len(tup)):
    if tup[i]==target:
        print(f"Present at position {i}")
        found=True
        break

if not found:
    print("Target not found")