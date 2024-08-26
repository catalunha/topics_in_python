def contador(maximo: int):
    n: int = 0
    while n < maximo:
        yield n
        n += 1


for i in contador(5):
    print(i)
