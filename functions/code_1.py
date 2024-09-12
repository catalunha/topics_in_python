## Uma função pode receber qq variável em quantidade e tipo e ate outra funcao
## uma funcao pode retornar variável em quantidade e tipo e ate outra funcao


## Basica
def funcao_basica():
    print("faz algo na funcao_basica")


funcao_basica()


## Com argumento
def funcao_com_argumentos(name, sobrenome):
    print("nome é " + name + " " + sobrenome)


funcao_com_argumentos("Jose", "Souza")


## Argumento nomeado
def funcao_com_argumento_nomeado(name, sobrenome):
    print("nome é " + name + " " + sobrenome)


funcao_com_argumento_nomeado(sobrenome="Batista", name="Joana")


## Argumento com valor padrao
def funcao_com_argumento_padrao(nome, sobrenome="Brasileiro"):
    print("nome é " + nome + " " + sobrenome)


funcao_com_argumento_padrao("Mauro")


## Retorna valor
def funcao_que_retorna_valor(nome, sobrenome):
    return nome + " " + sobrenome


fullname = funcao_que_retorna_valor("Marcio", "Catalunha")
print(fullname)


## Vazia
def funcao_vazia1():
    pass


## Também usamos ... para vazia mas menos visto e recomendado
def funcao_vazia2(): ...


## Parametro opcional
def function_parameter_optional(name: str, last_name=None, age: int = 10) -> str:
    return f"{name} {last_name} tem {age}"


result = function_parameter_optional("a", age=20)
print(result)
print(type(result))


## Parametros em tupla
## Se nao sabemos a quantidade de parametros
## podemos agrupa-lo numa tupla com *args
def funcao_com_argumentos_em_tuple(*args):
    print(args)
    print(type(args))
    print("nome é " + args[0] + " " + args[1])


funcao_com_argumentos_em_tuple("Maria", "Fernanda")


## Parametros em dict
## Se nao sabemos a quantidade de parametros nomeados
## podemos agrupa-los num dicionario com **kwargs
def funcao_com_argumentos_em_dict(**kwargs):
    print(type(kwargs))
    print("nome é " + kwargs["name"] + " " + kwargs["sobrenome"])


funcao_com_argumentos_em_dict(sobrenome="Teixeira", name="Carla")


## Envolvendo todos os casos acima
def funcao_exemplo1(equipe, *team, **day):
    print(equipe)
    print(team)
    print(day)
    return "Ok"


result = funcao_exemplo1("DevsPython", "Jorge", "Almeida", reuniao=5, festa=15)
print(result)


## Functions com tipagem
print("Functions com tipagem")


def function_1_with_typing(name: str, age: int = 10) -> str:
    return f"{name} tem {age}"


result = function_1_with_typing("b", 20)
print(result)
print(type(result))


def function_2_with_typing(
    name: str, last_name: str | None = None, age: int = 10
) -> str:
    return f"{name} {last_name} tem {age}"


result = function_2_with_typing("a", age=20)
print(result)
print(type(result))
