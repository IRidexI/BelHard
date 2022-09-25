text = (input("Enter text: "))

data = {i: text.count(i) for i in text}

print(data)
