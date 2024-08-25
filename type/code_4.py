from typing import TypedDict

# Sem checagem de tipo
data_1 = {
    "key_str": "str_1",
    "key_int": 1,
}
data_1a = {
    "key_str": "str_1",
    "key_int": "1",
}


class Data(TypedDict):
    key_str: str
    key_int: int


# Com checagem de tipo
data_2: Data = {
    "key_str": "str_1",
    "key_int": 1,
}
# Se descomentar o analisador pega
# data_2a: Data = {
#     "key_str": "str_1",
#     "key_int": "1",
# }
