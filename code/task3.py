import random

def eratosthenes_sieve(nums) -> set:
    nums = set(nums)
    addition = []

    while nums:
        p, u = min(nums), 1

        while p * u <= max(nums):
            u += 1
            nums.discard(p * u)

        addition.append(p)
        nums.discard(p)

    return set(addition + list(nums))

# используется как кеш для малых, часто встречающихся значений
SIEVE = eratosthenes_sieve(list(range(2, 501)))

def ferma_prime_test(num : int, k : int) -> bool:
    for _ in range(k): # k случайных тестов
        a = random.randint(2, num - 2)

        if pow(a, num - 1, num) != 1:
            return False # тут 100 %
    return True # тут не 100 %

def is_simple(num : int) -> bool:
    if num in SIEVE:
        return True

    if num % 2 == 0 or num == 1:
        return False

    return ferma_prime_test(num, 37)


def ferma_factorize(n: int) -> list[int]:

    if n == 1 or is_simple(int(n)): # простое число или 1 нельзя разложить
        return [n]

    if n % 2 == 0: # входное число нечетное, но его делители могут оказаться четными
        return [2, *ferma_factorize(n // 2)]

    buffer = n ** 0.5

    if buffer % 1 == 0: # мы берем x от 1 по алгоритму из файла, но это исключает вариант, когда входное число - квадрат другого
        return [*ferma_factorize(buffer)] * 2

    m = buffer // 1

    for x in range(1, int(n)): # метод ферма по описанию из файла
        q = (m + x) ** 2 - n

        if q ** 0.5 % 1 == 0:
            a = m + x
            b = q ** 0.5

            return [*ferma_factorize(a - b), *ferma_factorize(a + b)]

    raise ValueError("return statements missed something")

def translate_factorize(n: list[int]) -> dict:
    # ferma factorize возвращает неотсортированный список множителей, который надо упорядочить в словарь
    res = map(int, n)
    answ = dict()
    for v in res:
        if v not in answ:
            answ[v] = 1
        else:
            answ[v] += 1
    return answ

class FactorizedNum:
    def __init__(self, num: int):
        if num <= 0:
            raise ValueError
        self.factorized = translate_factorize(ferma_factorize(num))

    def out(self) -> str:
        output = ""
        for divider, count in sorted(self.factorized.items(), key=lambda x: x[0]):
            output += f"{"n = " if not output else " + "}{divider}^{count}"
        return output

print(FactorizedNum(163756472321**2).out())

