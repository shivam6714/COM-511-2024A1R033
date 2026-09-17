"""WAP to input marks of n students in a list. Display hisghest,lowest , average and number of students who failed"""



ls = list(map(int,input("Enter marks: ").split()))

print("Max marks: ",max(ls))
print("Min marks: ",min(ls))
print("Average marks: ",sum(ls)/len(ls))
passed=0
for x in ls:
    if x>40:
        passed+=1


print("Passed:",passed)
    