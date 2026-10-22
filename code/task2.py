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

def factorize(num : int) -> list:
    stack = [num]

    while True:
        all_values_simple = True

        for idx in range(len(stack)-1, -1, -1):
            val = stack[idx]

            if not (is_simple(val) or val == 1):
                all_values_simple = False

                for a in range(2, val):
                    if val % a == 0:
                        stack[idx] = val // a
                        stack.append(a)

                        break

        if all_values_simple:
            break

    return stack

def translate_factorize(n: list[int]) -> dict:
    # factorize возвращает неотсортированный список множителей, который надо упорядочить в словарь
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
        self.factorized = translate_factorize(factorize(num))

    def out(self) -> str:
        output = ""
        for divider, count in sorted(self.factorized.items(), key=lambda x: x[0]):
            output += f"{"n = " if not output else " + "}{divider}^{count}"
        return output

print(FactorizedNum(1637564723**2).out())