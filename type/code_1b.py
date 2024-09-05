# Tipos básicos - com tipagem

print("# Tipagem de variaveis")
print("## Tipos básicos")
integer: int = 1
print("integer", integer, type(integer))

decimal: float = 3.14
print("decimal", decimal, type(decimal))

string: str = "a"
print("string", string, type(string))

boolean: bool = True
print("boolean", boolean, type(boolean))

lista: list[int | str] = [1, "a"]
print("lista", lista, type(lista))

tupla: tuple[int, str] = (1, "a")
print("tupla", tupla, type(tupla))

tupla_2: tuple[int, ...] = (1, 2, 3, 4)
print("tupla_2", tupla_2, type(tupla_2))

lista_de_tuplas: list[tuple[str, int]] = [("a", 1), ("b", 2)]
print("lista_de_tuplas", lista_de_tuplas, type(lista_de_tuplas))

lista_de_tuplas2: list[tuple[str, str | int]] = [("a", 1), ("b", "2")]
print("lista_de_tuplas2", lista_de_tuplas2, type(lista_de_tuplas2))

conjunto_2: set[int] = {1, 2}
print("conjunto", conjunto, type(conjunto))


dictionary: dict[str, int] = {"a": 1}
print("dictionary", dictionary, type(dictionary))
