"""WAP to calculate the final bill amount after applying a discount. The program should take the total bill amount as input from the user and apply 
the discount according to the the following rules. After calculating the discount, the program should display the discount amount and the final
bill amount payable by the customer.
"""

bill=int(input())

if bill>5000:
    discount=bill*20/100
    print("Total amount:",bill)
    print("After Discount:",bill-discount)
elif bill>=3000 and bill<=5000:
    discount=bill*10/100
    print("Total amount:",bill)
    print("After Discount:",bill-discount)
else:
    print("No discount")
    print("Total amount:",bill)