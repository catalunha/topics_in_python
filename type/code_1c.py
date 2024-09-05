# Conversoes
print("## Conversoes")
integer2string = str(1)
print("integer2string", integer2string, type(integer2string))

decimal2string = str(3.14)
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
