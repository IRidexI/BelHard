Number1 = int(input("Enter the first number: "))
Number2 = int(input("Enter second number: "))
Number3 = int(input("Enter last number: "))

if Number1 % Number2 == 0 and Number1 > Number3:
    print(Number1)
else:
    print("error")
