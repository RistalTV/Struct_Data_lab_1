def factorization(n):
    """
    Разложение на простые множители
    :param n: число которое надо декомпозицировать
    :return p: простые множители
    """
    p = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            p[d] = p.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        p[n] = p.get(n, 0) + 1
    return p


if "__name__" == "__main__":
    a, b = int(input()), int(input())  # вводим числа
