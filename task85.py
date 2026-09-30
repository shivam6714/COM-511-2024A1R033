"""Binary search"""

num = list(map(int,input("Enter numbers:").split()))
target=int(input("Enter Target:"))

found = False
low = 0 
high = len(num)-1

while low<=high:
    mid=(low+high)//2
    if num[mid]==target:
        found=True
        res=mid
        break
    elif num[mid] > target:
        high=mid-1
    else:
        low=mid+1

if not found:
    print("Target not found")
else:
    print(f"{target} Found at position {res}")