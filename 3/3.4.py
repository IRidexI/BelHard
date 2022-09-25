n = int(input("Enter n: "))
numbers = {}
for i in range(n):
    numb = input("Enter numbers: ")
    numbers[i] = {"Numbers": numb}

print(max(numbers))
