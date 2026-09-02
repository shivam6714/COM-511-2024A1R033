"""Write a pyhton program to take student full name and dispaly the following:
    Total number of characters
    First Character
    Last Character
    Name in uppercase form

"""

name=input()

print("Total characters: ",len(name))
print("First Character: ",name[0])
print("Last Character: ",name[-1])
print("Upper case: ",name.upper())