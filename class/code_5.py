from enum import Enum


class ExampleClassEnum(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


print(ExampleClassEnum.choices())
print(ExampleClassEnum.APPROVED.value)
print(ExampleClassEnum.APPROVED.name)
