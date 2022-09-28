num1 = float(input("Enter first number : "))
action = input("What we gonna do? : ")
num2 = float(input("Enter second number : "))
result = 0

if action == "+":
    result = num1 + num2
    print("Result: ")


elif action == "-":
    result = num1 - num2
    print("Result: ")


elif action == "/":
    result = num1 / num2
    print("Result: ")


elif action == "*":
    result = num1 * num2
    print("Result: ")


elif action == "**":
    result = num1 ** num2
    print("Result: ")


elif action == "%":
    result = num1 % num2
    print("Result: ")

print(result)
