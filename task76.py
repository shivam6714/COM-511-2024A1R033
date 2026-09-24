"""WAP to show that tuple values cannot be changed directly. Convert Tuple into list, updat eit , convert it back to tuple"""

tup = ("Hello","Mr","Chimpanze")
print("Original Tuple: ",tup)
lst = []
print("Tuple cannot be updated")
for i in tup:
    lst.append(i)

lst[0]="Bye"

print("Updated List: ",lst)

tup2=tuple(lst)

print("Converted and Updated Tuple: ",tup2)