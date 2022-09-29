VarN = int(input("Enter the first number: "))
VarM = int(input("Enter second number: "))
VarK = int(input("Enter last number: "))

for num in range(1, VarN+1):
    if num % VarM == 0 and num > VarK:
        print(num)
