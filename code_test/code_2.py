def inc(x: int) -> int:
    return x + 1


def test_inc():
    assert inc(3) == 4


if __name__ == "__main__":
    print(inc(3))
