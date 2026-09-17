"""Take input of two lists and the in 3rd list append all the common elements"""

ls1 = list(map(int, input("Enter numbers: ").split()))
ls2 = list(map(int, input("Enter numbers: ").split()))

ls3=[]
for x in ls1:
    if x in ls1 and x in ls2:
        if x in ls3:
            continue
        else:
            ls3.append(x)

print(ls3)