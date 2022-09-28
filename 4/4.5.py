s = ""
num = 1
for col in range(0, 4):
    for row in range(0, 4):
        if num < 10:
            s += " "
        s += str(num) + " "
        num += 1
    print(s)
    s = ""

