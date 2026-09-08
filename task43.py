"""Write a pyhton program to simulate a digital lock system
    The lock should ask the user to enter a 4-digit pin. If the entered pin doesnot contain exactly 4 digits
    , the program should display and error message and ask again, if the entered pin is correct, the lock should open.
    Otherwise, the program should ask the user to try again.
"""

pin=input()
if len(pin)==4 and pin.isdigit():
    print("Lock opened")
else:
    print("Please enter pin again!!!!!!!!")