print("## code_1.py - Conjunto em python")

print("""## Criando um conjunto""")

set_1 = {1, "a", 3.14}
print(set_1)


print("""## Acessando itens em conjuntos""")
# Nao é possivel acessar a um item do set
# set_1[0] # gera erro
print("a" in set_1)

print("""## Adicionando itens em conjuntos""")
set_1 = {1, "a", 3.14}
set_1.add(2)
print(set_1)
set_2 = {2, "b", 2.72}
set_1.update(set_2)
print(set_1)
list_1 = [3, 4]
# é possivel adicional qq iteravel
set_1.update(list_1)
print(set_1)

print("""## Removendo itens a tupla""")
set_1 = {1, "a"}
print(set_1)
# Se o item nao existe dispara um erro
set_1.remove(1)
print(set_1)

# Se o item nao existe NAO dispara um erro
set_1.discard(1)
print(set_1)

# Remove um item aleaorio, ja que o set nao é ordenado
set_1 = {1, "a"}
set_1.pop()
print(set_1)

# limpa o set por completo
set_1 = {1, "a"}
set_1.clear()
print(set_1)

# limpa o set por completo
set_1 = {1, "a"}
del set_1
# print(set_1) # gera erro pois del apaga o set do codigo

print("## Outros recursos")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union
union_set = set1 | set2
print(union_set)
# Intersection
intersection_set = set1 & set2
print(intersection_set)
# Difference
difference_set = set1 - set2
print(difference_set)


# declare set empty
conjunto_3: set[int] = set()
