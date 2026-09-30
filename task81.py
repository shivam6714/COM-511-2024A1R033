"""WAP to find the longest consecutive in which marks are strictly greater than previous marks
Display sequnce,length, and starting and ending
"""


marks=list(map(int,input().split()))

# leng=1
# l=0
# first=0
# last=0
# for i in range(1,len(marks)):
#     if marks[i]<=marks[i-1]:
#         l=i
#     leng = max(leng,i-l+1)

# print(leng)

start=0
best_start=0
best_length=1
for i in range(1,len(marks)):
    if marks[i]<=marks[i-1]:
        start=i
    length=i-start+1

    if length>best_length:
        best_start=start
        best_length=length

sequence=marks[best_start:best_start+best_length]
test_range=(best_start+1,best_start + best_length)

print("Longest improving sequence:",sequence)
print("Number of Tests:",best_length)
print("Test range:",test_range)