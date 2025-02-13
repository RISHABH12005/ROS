A=int(input("Enter the no."))
for i in range (1,100):
    print("Fizz"*(i%3==0)+"Bizz"*(i%5==0)or i)