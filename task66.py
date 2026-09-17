"""WAP to input marks of 10 students. STore only valid marks bw 0 and 100 in a list. skip invalid marks."""


ls = list(map(int, input("Enter marks: ").split()))

lst = []

for i in ls:
    if 0 <= i <= 100:
        lst.append(i)

for i in lst:
    print(i)