with open('1/Lost.txt', 'r', encoding='utf-8') as file:
    lines = [list(map(int, line.strip().replace(' ', '').split(','))) for line in file]
print(lines)
