try:
    a = int(input("informe o 1 numero: "))
    b = int(input("informe o 2 numero: "))
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("divide ok")
finally:
    print("Execution completed.")
