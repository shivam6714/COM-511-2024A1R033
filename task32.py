"""Write a pyhton program to take a 10-digit mobile number and display only the last 4 digits. Replace the first 6 digits with ******"""

num=input()
result="*"*6+num[-4:]
print(result)