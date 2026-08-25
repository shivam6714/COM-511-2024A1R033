"""Write a python program to take total minutes as input and convert it into hours and remaining minutes"""

min = int(input())
hours=min//60
mins=min%60
print(f"hours: {hours} minutes : {mins}")