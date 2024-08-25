print("# Herança")


class Animal:
    _som = "..."

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def som(self) -> str:
        return f"O {self.nome} emite um {self._som}"


class Cachorro(Animal):
    _som = "latir"

    def __init__(self, nome: str, idade: int, raca: str):
        super().__init__(nome, idade)
        self.raca = raca

    def som(self) -> str:
        return super().som()


animal = Animal("animal1", 1)
print(animal.som())
cao = Cachorro("cao1", 2, "raca1")
print(cao.som())
