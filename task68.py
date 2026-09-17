"""WAP to input a list of nummbers create new list with only unique elements"""

ls = list(map(int, input("Enter numbers: ").split()))

lst=[]

for i in ls:
    if i in lst:
        continue
    else:
        lst.append(i)

print(lst)