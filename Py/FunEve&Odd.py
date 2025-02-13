''' Code using the Function to find the Even & Odd No. '''
def f1(n):
    if (n%2==0):
        return("Even")
    else:
        return("Odd")

n=int(input("Enter any No.:"))
print(f1(n))
