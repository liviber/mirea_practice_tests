
def eratosthenes_sieve(nums) -> list[int]:
    nums = set(nums)
    addition = []

    while nums:
        p, u = min(nums), 1

        while p * u <= max(nums):
            u += 1
            nums.discard(p * u)

        addition.append(p)
        nums.discard(p)

    return sorted(addition + list(nums))

def factorize(num : int) -> dict:
    nums_field = list(range(2, num // 2 + 1))
    sorted_sieve = eratosthenes_sieve(nums_field)

    result = dict()
    while num > 1:
        for p in sorted_sieve:
            if num % p == 0:
                result[p] = 1 if not p in result else result[p] + 1
                num /= p

        if not result:
            break

    return result if result else {num: 1}

class FactorizedNum:
    def __init__(self, num: int):
        if num <= 0:
            raise ValueError
        self.factorized = factorize(num)

    def out(self) -> str:
        output = ""
        for divider, count in sorted(self.factorized.items(), key=lambda x: x[0]):
            output += f"{"n = " if not output else " + "}{divider}^{count}"
        return output

print(FactorizedNum(9876).out())