"""
   Take students details like name,roll no, cgpa, hostel status from the user. Type cast them into appropriate type
   and print them along with their detected type
"""
name=input()
roll=input()
cgpa=input()
hostel=input()

n=str(name)
r=int(roll)
c=float(cgpa)
h=bool(hostel)

print(n)
print(type(n))
print(r)
print(type(r))
print(c)
print(type(c))
print(h)
print(type(h))