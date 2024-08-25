from typing import Iterable


def soma_numeros(numeros: Iterable[int]) -> int:
    soma = 0
    for numero in numeros:
        soma += numero
    return soma


print(soma_numeros([1, 2, 3]))
print(soma_numeros((1, 2, 3)))
print(soma_numeros({1, 2, 3}))
print(soma_numeros({"a": 1, "b": 2, "c": 3}))
