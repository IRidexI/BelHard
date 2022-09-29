n = int(input("Enter n: "))
users = {}
for i in range(n):
    name = input("Enter name: ")
    email = input("Enter email: ")
    users[i] = {"name": name, "email": email}
print(users)
