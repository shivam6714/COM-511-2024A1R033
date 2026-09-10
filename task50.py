"""WAP that asks the user to enter a username and password . The user should only only get 3 attempts.
if correct display Login successful ans stop the loop. if all attempts are used, sisplay account blocked"""

name="lorem ipsum"
password="12345"
attempt=3
while True:
    name1=input("Enter your name: ")
    password1=input("Enter password: ")
    if(name1 == name and password1==password):
        print("Login successful")
        break
    else:
        attempt-=1
        if(attempt==0):
            print("Account blocked")
            break
        else:
            print("try again")


