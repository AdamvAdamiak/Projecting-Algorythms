def aczp(x, y):  # 2.1 classic
    while x != y:
        x, y = max(x, y), min(x, y)
        x = x - y
    return x


def aeuc(x, y):  # 2.1 euklides
    if y == 0:
        return x
    return aeuc(y, x % y)


x = 122
y = 1500
print(aczp(x, y))
print(aeuc(x, y))
