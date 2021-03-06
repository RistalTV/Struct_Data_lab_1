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


if __name__ == "__main__":
    print("Лабораторная работа №1")  # Основная информация
    print("Выполнил: Скребнев Леонид Эдуардович ФИТУ 2-5")  # Основная информация
    a, b = int(input()), int(input())  # вводим числа
    pa, pb = factorization(a), factorization(b)  # разложение на простые множители
    n = 1
    for key in pa:  # пробегаемся по словорю и ищим сам большой одинаковый результат
        if not key in pb:
            n = -1
            break
        k = -(-pa[key] // pb[key])
        if k > n:
            n = k
    print("\n" + str(n))  # вывод числа
