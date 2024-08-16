def payments(value, **exps):
    print("value =", value)
    print("exps =", exps)
    if "exp_1" in exps:
        return value ** exps["exp_1"]
    if "exp_2" in exps:
        return value ** exps["exp_2"]


print("***")
print(payments(2, exp_1=2))
print("***")
print(payments(2, exp_2=3))
