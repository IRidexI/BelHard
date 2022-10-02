numbers = [98, 83, 4, 6, 8, 180]

j = -1
for i in range(int(len(numbers) / 2)):
    numbers[i], numbers[j] = numbers[j], numbers[i]
    j -= 1

print(*numbers)