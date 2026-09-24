"""WAP to store all months names in a tuple. Input a month number and display the corresponding month name"""

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

Number = int(input("Enter Month number: "))

print(months[Number-1])