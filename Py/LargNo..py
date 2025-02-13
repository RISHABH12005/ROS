''' Code of Find the Large No. '''
A=float(input("Enter the 1st No.:"))
B=float(input("Enter the 2nd No.:"))
C=float(input("Enter the 3rd No.:"))
if A>=B and A>=C:
    largest=A
elif B>=A and B>=C:
    largest=B
else:
    largest=C
print(f"The largest No. among {A},{B},{C} is {largest}")
