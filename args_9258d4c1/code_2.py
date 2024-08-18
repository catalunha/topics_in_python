def values(first, *others):
    print("first =", first)
    print("others =", others)
    for i in range(len(others)):
        print(f"others[{i}] =", others[i])


print("***")
values(10, 20, 30)
print("***")
values(10, 20, 30, 40)
