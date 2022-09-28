N = int(input("Enter the first number: "))
M = int(input("Enter second number: "))
K = int(input("Enter last number: "))

if N % M == 0 and N > K:
    print(N)
else:
    print("error")
