from math import ceil

def is_simple(num: int) -> bool:
    # генерировать целый массив простых чисел для проверки одного из них нецелесообразно, поэтому используется перебор а не решето
    if num == 1:
        return False
    if num == 2:
        return True

    for x in range(2, ceil(num ** 0.5) + 1):
        if num != 1 and num % x == 0:
            return False
    return True


def ferma_factorize(n: int) -> list[int]:

    if is_simple(n) or n in [1, 2]: # простое число или 1 нельзя разложить
        return [n]

    if n % 2 == 0: # входное число нечетное, но его делители могут оказаться четными
        return [2, *ferma_factorize(n // 2)]

    temp = n ** 0.5

    if temp % 1 == 0: # мы берем x от 1 по алгоритму из файла, но это исключает вариант, когда входное число - квадрат другого
        return [*ferma_factorize(temp)] * 2

    m = temp // 1

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

print(FactorizedNum(231).out()) # n = 2^5 + 7^1 + 13^1

