print("# Operadores aritméticos")
num1 = 5
num2 = 2
print("num1", "=", num1)
print("num2", "=", num2)
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)
print(num1, "**", num2, "=", num1**num2)
print("Quociente", num1, "//", num2, "=", num1 // num2)
print("Resto", num1, "%", num2, "=", num1 % num2)
temp = num1
num1 += num2
print(temp, " += ", num2, " = ", num1)

print("# Operadores relacionais")
num1 = 1
num2 = 2
print("num1", "=", num1)
print("num2", "=", num2)
print(num1, "==", num2, "=", num1 == num2)
print(num1, "!=", num2, "=", num1 != num2)
print(num1, ">", num2, "=", num1 > num2)
print(num1, "<", num2, "=", num1 < num2)
print(num1, ">=", num2, "=", num1 >= num2)
print(num1, "<=", num2, "=", num1 <= num2)
print(num1, "!=", num2, "and", num1, ">", num2, "=", num1 != num2 and num1 > num2)
print(num1, "!=", num2, "or", num1, ">", num2, "=", num1 != num2 or num1 > num2)

print("## Tabela verdade")
print("F and T = F")
print("F and F = F")
print("T and F = F")
print("T and T = T")

print("T or F = T")
print("F or T = T")
print("T or T = T")
print("F or F = F")

print("all ao inves de and")
dict_1: dict[str, int] = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# list_1: list[str] = ["a", "b"]
required_list_1: list[str] = ["a", "b", "d"]

if all(key in dict_1 for key in required_list_1):
    print("Todos os requeridos foram encontrados")
else:
    print("Algum requerido NAO foi encontrado")


print("any ao inves de or")
list_1: list[str] = ["a", "b", "c"]

# required_list_2: list[str] = ["a", "d"]
required_list_2: list[str] = ["d", "e"]

if any(value in list_1 for value in required_list_2):
    print("Algum foi encontrado")
else:
    print("Nenhum foi encontrado")
