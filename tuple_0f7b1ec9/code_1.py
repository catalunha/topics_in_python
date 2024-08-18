print("""## code_1.py comentado""")


print("""### Criando tuplas""")

tupla_1 = (1, "a", [11, 12, 13])
print(tupla_1)

tupla_2 = 2, "b", [21, 22, 23]
print(tupla_2)

tupla_3 = (3,)
print(tupla_3)
list_1 = [4, "c"]
tupla_4 = tuple(list_1)
print(tupla_4)


print("""### Acessando itens da tupla""")
tupla_1 = (1, "a", [2, 3, 4])
print(tupla_1)

print(tupla_1[1])

print("""### Adicionando itens a tupla""")
# A lista é imutável e nao pode ser adicionada

print("""### Removendo itens a tupla""")
# A lista é imutável e nao pode ser removido seus itens

print("""### Editando itens a tupla""")
# A lista é imutável e nao pode ser editado seus itens


print("""### Criando nova tupla""")
tupla_1 = (1, "a")

tupla_1 += ([2, 3, 4],)
print(tupla_1)

print("""### Componentes imutaveis e mutaveis na tupla""")
tupla_1 = (1, "a", [2, 3, 4])
print(tupla_1)

# Gera erro. Elemento da tupla é imutavel
# tupla_1[1] = "b"

# Nao gera erro. O elemento lista da tupla é mutável
tupla_1[2].append(5)
print(tupla_1)

print("""### Desempacotando tupla""")
tupla_1 = (1, "a", [2, 3, 4])
print(tupla_1)
a, b, *c = tupla_1
print(a)
print(b)

print("""### Busca em tupla""")
tupla_1 = (1, "a", [2, 3, 4])
print(tupla_1)

print("a" in tupla_1)
