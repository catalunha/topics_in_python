print("Comprehensions com list")

comp_list = [var for var in range(10) if var % 2 == 0]
print(comp_list)

print("Comprehensions com set")

comp_set = {var for var in range(10) if var % 2 == 0}
print(comp_set)

print("Comprehensions com dict")

comp_dict = {f"Par{str(var)}": var for var in range(10) if var % 2 == 0}
print(comp_dict)

print("Comprehensions com generator")

comp_generator = (var for var in range(10) if var % 2 == 0)
print(type(comp_generator))
print(comp_generator)
for i in comp_generator:
    print(i)
