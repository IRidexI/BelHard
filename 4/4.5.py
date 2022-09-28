s = ""
num = 1
for col in range(1, 4):
    for row in range(1, 4):
        s += str(num) + " "
        num += 1

        if num < 10:
            print(s)
            s = ""

