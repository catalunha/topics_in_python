print("# ClassComAtributo")


class ClassComAtributo:
    atributo = 1


classComAtributo = ClassComAtributo()
print(classComAtributo.atributo)


print("# ClassComConstrutor")


class ClassComConstrutor:
    def __init__(self, nome):
        self.atributo = nome


classComConstrutor = ClassComConstrutor("Maria")
print(classComConstrutor.atributo)


print("# ClassComToString")


class ClassComToString:
    def __str__(self):
        return "Class..."


classComToString = ClassComToString()
print(classComToString)


print("# ClassComMethodos")


class ClassComMethodos:
    def fazAlgo(self):
        print("Fazendo algo...")


classComMethodos = ClassComMethodos()
classComMethodos.fazAlgo()


print("# Tudo junto")


class ClassTudoJunto:
    def __init__(self, nome):
        self.atributo = nome

    def __str__(self):
        return f"Class: atributo={self.atributo}"

    def fazAlgo(self):
        print("Fazendo algo...")


classTudoJunto = ClassTudoJunto("Tudo Junto")
classTudoJunto.fazAlgo()
print(classTudoJunto)
