
from functools import wraps
from math import ceil


def check_input(func):
    @wraps(func)
    def wrapper(p: int) -> bool:
        if p < 2:
            return False

        if p == 2:
            return True

        for x in range(2, ceil(p ** 0.5) + 1):
            if p != 1 and p % x == 0:
                return False

        return func(p)
    return wrapper


@check_input
def is_simple(p: int) -> bool:
    M = 2 ** p - 1

    s = 4
    for _ in range(p-2):
        s = (s**2 - 2) % M

    return s == 0


p = int(input("номер числа Мерсена: "))
print(is_simple(p))














