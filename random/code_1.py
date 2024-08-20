import random

random_1: float = random.random()
print(random_1)

random_2: int = random.randint(1, 5)
print(random_2)

list_1: list[str] = list("python")
# list_1: list[str] = ["a", "b", "c"]
print(list_1)
print(random.choice(list_1))
# choices, é possível que haja repetição de valores, ou seja,
# essa função pode selecionar mais de uma vez o mesmo número dentro da lista.
# Então poderíamos ter como resultado uma lista com [7, 7], por exemplo.
print(random.choices(list_1, k=2))
# Para selecionar elementos aleatórios evitando a repetição de valores, podemos utilizar a função sample.
print(random.sample(list_1, k=2))
# embaralhar lista
random.shuffle(list_1)
print(list_1)
