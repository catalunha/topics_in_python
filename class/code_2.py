print("# Métodos estáticos")
"""
Um @staticmethod (ou método estático) é um método que se comporta como uma função regular, mas pertence a uma classe. 
Internamente, o método não tem acesso nem à classe (cls), nem à instância (self) na qual é chamado. 
Isso significa que ele não pode modificar o estado da instância do objeto nem o estado da classe.
Em geral, métodos estáticos são usados para agrupar funções que têm uma conexão lógica com uma classe, apesar de não usar seus atributos diretamente.
"""


class Calculadora:
    @staticmethod
    def somar(x: int, y: int) -> int:
        return x + y


# Método estático chamado usando o nome da classe
print(Calculadora.somar(5, 3))  # Saída: 8


print("# Métodos de classe")
"""
Por outro lado, um @classmethod (método de classe) é um método que recebe a classe como o primeiro argumento. 
Isso é útil para casos em que você precisa ter acesso ao objeto da classe, por exemplo, quando você quer criar métodos alternativos para inicializar uma instância da classe.
"""


class Bebida:
    nome = "Bebida"

    @classmethod
    def imprimir_nome(cls):
        print(f"Esta é uma {cls.nome}")


class Café(Bebida):
    nome = "Café"


# Método de classe chamado usando o nome da classe
Bebida.imprimir_nome()  # Saída: Esta é uma Bebida
Café.imprimir_nome()  # Saída: Esta é um Café

print("# Resumindo")
"""
Um método de instância requer uma instância da classe e pode acessar a instância através de self.
Um método de classe não requer uma instância. Ele não pode acessar a instância (self), mas pode acessar o objeto da classe via cls.
Um método estático não tem acesso a cls ou self. Ele funciona como uma função regular, mas pertence ao namespace da classe.
"""


class MinhaClasse:
    def metodo_de_instancia(self):
        return "método de instância chamado", self

    @classmethod
    def metodo_de_classe(cls):
        return "método de classe chamado", cls

    @staticmethod
    def metodo_estatico():
        return "método estático chamado"
