"""WAP to detect whether a comment is spam or not. A comment shoould be treated as spam if it contains 
any of these keywords: "make a lot of money", "buy now", "subscribe this" or "click this"
"""

comment = input().lower()
a= "make a lot of money"
b= "buy now"
c= "subscribe this"
d= "click this"

if a in comment or b in comment or c in comment or d in comment:
    print("SPAM!!!!!!!!")
else:
    print("No spam")
