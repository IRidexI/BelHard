Number = int(input())
Number2 = int(input())
Number3 = int(input())

while Number % Number2 > Number3:
    Number += 2
    Number3 += 1
print(Number)
# Doesn't work
