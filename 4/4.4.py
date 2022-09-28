Number2 = int(input("Enter the range number: "))
counter = 0
s = ""

for num in range(1, Number2 + 1):
    if num % 1 == 0:
        counter += 1
        s += str(num) + " "

        if counter > 4:
            print(s)
            s = ""
            counter = 0
