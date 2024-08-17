print("Iniciando um programa")
# Use o \# para comentar uma linha em python
"""
Isto seria um comentario de multiplas linhas
É usado também para documentar classe e outros códigos
"""


class AnyClass:
    """
    Documentando a classe

    Esta classe calcula
    """

    def __init__(self, name) -> None:
        """Documentando o construtor ..."""
        self.name = name

    def doSomething(self) -> None:
        """Documentando um método ..."""
        print(self.name)


print(AnyClass.__doc__)
print(AnyClass.doSomething.__doc__)

print("Terminando um programa")
