"""Take an email and check if it contains @ and .com"""

email=input()

print(email.__contains__("@") and email.__contains__(".com"))