N = int(input("Enter the first number: "))
M = int(input("Enter second number: "))
K = int(input("Enter last number: "))

for num in range(1, N+1):
    if num % M == 0 and num > K:
        print(num)
