print("Controle if")
# if puro
x = 1
if x > 0:
    print("Positive")


# if else
x = 1
if x > 0:
    print("Positive")
else:
    print("Não Positive")

# if elif
x = 1
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")

# if elif else
x = 1
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


print("# Loop")
print("## for")
list_1 = ["a", "b", "c"]
for item in list_1:
    print(item)

print("## for range")
print("## for range(start, stop, step)")
for item in range(1, 10, 2):
    print(item)

print("## for range(start, stop)")
for item in range(3, 5):
    print(item)

print("## for range(stop)")
for item in range(6):
    print(item)


print("## while")
value = 0
while value < 10:
    print(value)
    value += 1
