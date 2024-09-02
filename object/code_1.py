print("Id do endereçço na memoria")
data_1 = "Aaa"
print(data_1)

print(id(data_1))

print("Tamanho da memoria")
data_2 = "Aaa"
print(data_2)

print(data_2.__sizeof__())

print("Tipo do objeto")
data_3 = "Aaa"
print(data_3)

print(type(data_3))

print("È instancia de um objeto int")
data_4: int = 123
print(isinstance(data_4, str))
