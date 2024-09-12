print("""## code_1.py comentado""")


print("""## Criando dicionários""")

contacts_tuple_in_list = [("Aaa", 111), ("Bbb", 222), ("Ccc", 333)]
print(contacts_tuple_in_list)
print(contacts_tuple_in_list[1][0])
contacts_dict_of_tuple__in_list = dict(contacts_tuple_in_list)
print(contacts_dict_of_tuple__in_list)


contacts = {"Aaa": 111, "Bbb": 222, "Ccc": 333}
print(contacts)

print("""## Acessando itens""")
contacts = {"Aaa": 111, "Bbb": 222, "Ccc": 333}
print(contacts)

print(contacts["Aaa"])  # Se existir não gera erro, mas ...
# print(contacts["Ddd"])  # Se key não existe, gera erro

print(contacts.get("Aaa"))
print(contacts.get("Ddd"))
print(contacts.get("Ddd", "Ddd: Valor não existe"))

print("Aaa" in contacts)
print("Ddd" in contacts)
print(111 in contacts)
print(111 in contacts.values())

print("""## Adicionando itens""")
contacts = {"Aaa": 111, "Bbb": 222, "Ccc": 333}
print(contacts)

contacts["Ddd"] = 444
print(contacts)

print("""## Removendo itens""")
contacts = {"Aaa": 111, "Bbb": 222, "Ccc": 333}
contacts["Ddd"] = 444
print(contacts)

del contacts["Ddd"]
print(contacts)
# del contacts["Ddd"]  # Se key nao existe, gera erro

# print(contacts.pop("Ddd")) # Se key nao existe, gera erro
print(contacts.pop("Ddd", 999))  # tem q ter valor de retorno

print("""## Juntando dicionarios""")
contacts = {"Aaa": 111, "Bbb": 222, "Ccc": 333}
print(contacts)

contacts_old = {"Ddd": 444, "Eee": 555}
print(contacts_old)
for name in contacts_old:
    contacts[name] = contacts_old[name]
print(contacts)

contacts = {"Aaa": 111, "Bbb": 222, "Ccc": 333}
print(contacts)
contacts_old = {"Ddd": 444, "Eee": 555}
print(contacts_old)
contacts.update(contacts_old)
print(contacts)

print("""## Compreensões em dicionários""")
contacts = {"Aaa": 111, "Bbb": 222, "Ccc": 333}
print(contacts)

contacts_new = {name: 1000 + contacts[name] for name in contacts}
print(contacts_new)


print("""## Views em dicionários""")
contacts = {"Aaa": 111, "Bbb": 222, "Ccc": 333}
print(contacts)
print(contacts.values())
print(type(contacts))
print(type(contacts.values()))

print("""""")
