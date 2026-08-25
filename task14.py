"""write a python program to take an amout in rupees and calculate how many 500 and 100 notes are needed"""

money=int(input())
five_hundred=money//500
money%=500
one=money//100
print(f"Five hundred are {five_hundred} and one hundred are {one}")