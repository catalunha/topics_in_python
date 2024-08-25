print("ola")
cpf = "123"
cnpj = "456"
data = {
    "q": f"doc{{{cpf or cnpj}}}",
}
print(data)
