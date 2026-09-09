"""WAP to create a simple password validation system..
The program should repeatedly ask the user to enter a password until a valid password is entered.
A password will be considered valid only if it has atleast 8 characters and coontains the @ symbol.

Once the user enters a valid password, the program should display "Password Accepted" and stop. 
Otherwise, it should display "Weak password. Try again" and ask for the passwprd again.

"""

password=input("Enter your password: ")
while len(password) < 8 or '@' not in password:
    print("Weak password. Try again")
    password=input("Enter your password: ")
print("Password Accepted")