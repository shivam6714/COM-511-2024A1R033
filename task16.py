"""Swap without using thrid variable"""
a=int(input())
b=int(input())

print(f"Original values are {a} {b}")

a=a+b
b=a-b
a=a-b

print(f"Swapped values are {a} {b}")