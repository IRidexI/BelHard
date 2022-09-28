Number = 2
Number2 = int(input("Enter the range number: "))

for num in range(Number, Number2 + 1):
    if num % 2 == 0:
        print(num, )
