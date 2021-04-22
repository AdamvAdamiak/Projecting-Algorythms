import random


def fermat(p, k=40):
    i = 0

    while i < k:
        a = random.randint(1, p - 1)
        if pow(a, (p - 1), p) == 1:
            i = i + 1
        else:
            return False

    return True


def miller_rabin(n, k=40):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == '__main__':
    print(fermat(5))
    print(miller_rabin(1621))
