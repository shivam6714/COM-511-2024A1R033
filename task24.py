"""Write a pythin program to fill the given letter template with custom name and date
    letter="
    Dear <Name>,
    You are selected!
    <Date>
    "
"""
letter='''
Dear <Name>,
You are selected!
<Date>
'''
name=input()
date=input()

letter=letter.replace("<Name>",name)
letter=letter.replace("<Date>",date)

print(letter)