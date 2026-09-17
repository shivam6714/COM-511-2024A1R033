"""Write a program to rotate a list one position to the right"""

ls = list(map(int, input("Enter numbers: ").split()))

front = ls[-1]

for i in range(len(ls)-1,0,-1):
    ls[i]=ls[i-1]

ls[0]=front
print(ls)