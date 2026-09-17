"""WAP to count how many times a particular element appears in the list"""

ls = list(map(int, input("Enter numbers: ").split()))

freq={}

for i in ls:
    freq[i]=freq.get(i,0)+1
print(freq)