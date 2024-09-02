def somar(a: int, b: int) -> int:
    return a + b


a = 1
b = 2
print(a)
print(b)
print(a, b)
print("a", a, "b", b)
print("a", a, "b", b, "soma", somar(a, b))
print(f"a={a} b={b} soma= {somar(a,b)}")
c: float = 0.000123456
print("c", f"{c:.6f}")
print("c", f"{c:.2e}")

# Imprimindo json formatado
import json
from typing import Any

dict_1 = {
    "key_str": "Abc",
    "key_int": 2,
    "key_float": 3.14,
    "key_list": ["a", 1],
    "key_bool": True,
    "key_None": None,
    "key_dict": {"a": 1},
}


def printjson(data: dict[str, Any]) -> None:
    print(json.dumps(data, indent=2))


printjson(dict_1)
