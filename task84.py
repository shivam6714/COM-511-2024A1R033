"""Linear search"""

num = list(map(int,input("Enter numbers:").split()))
target=int(input("Enter Target:"))

found = False

for i in range(len(num)):
    if num[i]==target:
        found=True
        res=i
        break

if not found:
    print("Target not found")
else:
    print(f"{target} Found at position {res}")