from typing import Any

print("## code_1.py - Listas em python")

print("""### Criando lista""")

list_1: list[Any] = [
    1,
    "a",
    3.14,
    [2, 3],
    ("b", 2),
]
print(list_1)

tuple_1 = (1, 2)
list_2 = list(tuple_1)
print(list_2)

print("""### Acessando itens em lista""")
list_1 = [1, "a", 3.14, [2, 3], ("b", 2)]
print(list_1)

print(list_1[1])

print("""### Adicionando itens em lista""")
list_1 = [1]
print(list_1)
list_1.append("a")
print(list_1)

print("""### Removendo itens a tupla""")
list_1 = [1, "a"]
print(list_1)
list_1.remove(1)
print(list_1)

print("""### Editando itens da lista""")
list_1 = [1, "a"]
print(list_1)
list_1[1] = "b"
print(list_1)

print("""### Compreensão para criar lista""")
list_1 = [1, 2, 3, 4]
print(list_1)
list_2 = [i for i in list_1 if i % 2 == 0]
print(list_2)
