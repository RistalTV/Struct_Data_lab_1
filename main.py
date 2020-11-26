def factorization(n):
    p = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            p.append(d)
            n //= d
        d += 1
    if n > 1:
        p.append(n)
    ans = []
    i = 0
    
a, b = int(input()), int(input())   # вводим числа
if a == b == 1:                     # небольшая проверка на 1
    print(1)
else:
