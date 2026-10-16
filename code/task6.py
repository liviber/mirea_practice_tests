from math import ceil





def sundaram_sieve(n : int) -> list[int]:
    M = (n - 1) // 2

    prime_mask = [1] * (M + 1)
    primes = [2]

    # вычеркивание неправильных позиций
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            buffer = i + j + 2 * i * j

            if buffer <= M:
                prime_mask[buffer] = 0

    # формирование самих чисел
    for n in range(1, M + 1):
        if prime_mask[n]:
            primes.append(2 * n + 1)

    return primes



print(sundaram_sieve(1004))























