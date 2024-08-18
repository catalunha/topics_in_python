print("Lendo um arquivo")
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

print("Escrevendo num arquivo")
with open("new_file.txt", "w") as new_file:
    new_file.write("Hello, Python!")
