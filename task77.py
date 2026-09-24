"""WAP to store repeated values in a tuple and count how many times a given value appears"""
from collections import Counter

tup = (1,2,3,3,4,1,1,1,1,6,7)

counts = Counter(tup)

repeated_items = {item: count for item, count in counts.items() if count >1}

target=int(input("Enter target value: "))

print(f"{target} appears {counts[target]} times")