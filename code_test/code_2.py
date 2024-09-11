import random

num1: int | float = random.randint(0, 10)
operator: str = random.choice(["+", "-", "*", "/"])
if operator == "/":
    num2: int | float = random.randint(1, 10)
else:
    num2: int | float = random.randint(0, 10)
print(f"Qual é o resultado de {num1} {operator} {num2} ?")
result: int | float = eval(f"{num1}{operator}{num2}")
options: list[str] = []
if isinstance(result, int):
    options_temp: list[int] = [
        random.randint(result - 6, result - 3),
        random.randint(result + 1, result + 3),
        random.randint(result + 4, result + 6),
    ]
    options_temp.append(result)
    for option in options_temp:
        options.append(f"{option}")
    result = f"{option}"
else:
    values_diff = True
    while values_diff:
        options_temp = [
            random.random() + result + 0.5,
            1 + random.random() + result,
            -1 + random.random() + result,
        ]
        options_temp.append(result)
        if len(options_temp) == len(set(options_temp)):
            values_diff = False
    for option in options_temp:
        options.append(f"{option:.1f}")
    result = f"{option:.1f}"
random.shuffle(options)
option_dict = {
    "a": options[0],
    "b": options[1],
    "c": options[2],
    "d": options[3],
}
for key in option_dict:
    print(f"{key}) {option_dict[key]}")
print("Informe uma das opções: a,b,c,d ou s para sair.")
response_ok = True
list_response = ["a", "b", "c", "d", "s"]
while response_ok:
    response = input("Sua opção: ")
    if response == "s":
        break
    if response not in list_response:
        print("Opção desconhecida.")
    if response in list_response:
        if option_dict[response] == result:
            response_ok = False
            print("Parabens! Você acertou.")
        else:
            print("Oops! Você errou.")
