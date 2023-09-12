n1 = int(input("Enter your number"))

factorial = 1
i = 1

if n1 < 0:
    print("Factorial is 0")
elif n1 == 1 or n1 == 0:
    print("Factorial is 1")
else:
    while n1!=1:
        factorial *= n1
        n1 -= 1
    
    print("Factorial is: ",factorial)
    



        