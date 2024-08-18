class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person = {self.name}"


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def __str__(self):
        return f"{self.name}, {self.salary}"


person = Person("Mateus")

print(person)
print(person.name)

employee = Employee("Marcos", 123)
print(employee)
