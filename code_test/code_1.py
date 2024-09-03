from typing import Any


def test(a: str | None = None, b: Any = "ss") -> None:
    print(a)
    print(b)


test("aaa", "bb")
test()
