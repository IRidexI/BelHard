Number2 = int(input("Enter the range number: "))
counter = 0
s = ""

for num in range(2, Number2 + 1):
    if num % 2 == 0:
        counter += 1
        s += str(num)
        print(s)

        if counter > 4:
            print()
            s = ""
            counter = 0

