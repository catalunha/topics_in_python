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
