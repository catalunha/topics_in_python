class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        self.data = kwargs


person = Person("Mateus", age=10)

print(person.data)
print(person.data["age"])
