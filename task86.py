"""Lab 6 : Write a program to reverse every kth row in a matrix"""

n, m = map(int,input().split())

matrix = []

for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

k = int(input())

for i in range(1,n+1):
    if i%k==0:
        matrix[i-1].reverse()

for i in range(n):
    print(matrix[i])