"""write a pyhton program to take two inputs a and b , swap their values"""
a=int(input())
b=int(input())
print(f"original values are {a} {b}")
temp=a
a=b
b=temp

print(f"swapped values are {a} {b}")
