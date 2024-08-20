# Tipos básicos
print("## Tipos básicos")
integer = 1
print("integer", integer, type(integer))

decimal = 3.14
print("decimal", decimal, type(decimal))

string = "a"
print("string", string, type(string))

boolean = True
print("boolean", boolean, type(boolean))

lista = [1, "a"]
print("lista", lista, type(lista))

tupla = (1, "a")
print("tupla", tupla, type(tupla))

conjunto = {1, "a"}
print("conjunto", conjunto, type(conjunto))

dictionary = {"a": 1}
print("dictionary", dictionary, type(dictionary))

# Conversoes
print("## Conversoes")
integer2string = str(integer)
print("integer2string", integer2string, type(integer2string))

decimal2string = str(decimal)
print("decimal2string", decimal2string, type(decimal2string))

string2integer = int("1")
print("string2integer", string2integer, type(string2integer))

string2float = float("3.14")
print("string2float", string2float, type(string2float))

tupla2lista = list(tupla)
print(tupla, "tupla2lista", tupla2lista, type(tupla2lista))

lista2tupla = tuple(lista)
print(lista, "lista2tupla", lista2tupla, type(lista2tupla))

listaDetupla = [("a", 1), (2, "b")]
listaDetupla2dict = dict(listaDetupla)
print(listaDetupla, "listaDetupla2dict", listaDetupla2dict, type(listaDetupla2dict))

dictionary = {"a": 1, "b": 2}
dictionary2tupla_keys = tuple(dictionary)
print(
    dictionary,
    "dictionary2tupla_keys",
    dictionary2tupla_keys,
    type(dictionary2tupla_keys),
)
dictionary2tupla_values = tuple(dictionary.values())
print(
    dictionary,
    "dictionary2tupla_values",
    dictionary2tupla_values,
    type(dictionary2tupla_values),
)
dictionary = {"a": 1, "b": 2, "c": 2}

dictionary2set_values = set(dictionary.values())
print(
    dictionary,
    "dictionary2set_values",
    dictionary2set_values,
    type(dictionary2set_values),
)

# Tipos com tipagem
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
