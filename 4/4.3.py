Number2 = int(input("Enter the range number: "))
counter = 0

for num in range(2, Number2 + 1):
    if num % 2 == 0:
        counter += 1
        print(num)

        if counter > 4:
            print("\n")
            counter = 0

