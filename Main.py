# Just Text

print("Life is a quality that distinguishes matter that has biological processes, such as signaling and "
      "self-sustaining processes,\n from that which does not, and is defined by the capacity for growth, reaction to "
      "stimuli, metabolism, energy transformation,\n and reproduction. Various forms of life exist, such as plants, "
      "animals, fungi, protists, archaea, and bacteria.\n Biology is the science that studies life.")

# Simple calculator

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")
result = float(num_1) + float(num_2)

print(result)

# Something

n = input("Number: ")

a = int(n[0])
b = int(n[1])
c = int(n[2])

print("Sum:", a + b + c)

# Next
n = int(input("Enter n: "))
numbers = []
for i in range(n):
    numbers.append(int(input("number: ")))

print(max(numbers))


# Next
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
