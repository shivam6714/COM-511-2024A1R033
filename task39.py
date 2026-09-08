"""WAP to take a password and check whether it contains @ and has atleast 8 charcters"""

password=input()

print(password.find("@") and len(password)>=8)