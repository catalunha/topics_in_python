def somar(a: int, b: int) -> int:
    return a + b


a = 1
b = 2
print(a)
print(b)
print(a, b)
print("a", a, "b", b)
print("a", a, "b", b, "soma", somar(a, b))
print(f"a={a} b={b} soma= {somar(a,b)}")
c: float = 0.000123456
print("c", f"{c:.6f}")
print("c", f"{c:.2e}")
