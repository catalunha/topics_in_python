from typing import Optional, TypedDict

# Sem checagem de tipo para dict
data_1 = {
    "key_str": "str_1",
    "key_int": 1,
}
data_1a = {
    "key_str": "str_1",
    "key_int": "1",
}


# construindo a class para mapear json
class Data(TypedDict):
    key_str: str
    key_int: int
    key_bool: bool | None


# Com checagem de tipo
data_2: Data = {
    "key_str": "str_1",
    "key_int": 1,
    "key_bool": None,
}
print("data_2", data_2)
data_3 = Data(
    key_str="str_1",
    key_int=1,
    key_bool=None,
)
print("data_3", data_3)


# "key_bool": False,
# Se descomentar o analisador pega o erro de tipo
# data_2a: Data = {
#     "key_str": "str_1",
#     "key_int": "1",
# }
