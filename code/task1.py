

def gcd(a : int, b : int) -> int:
    while a and b:
        a, b = (a % b, b) if a > b else (a, b % a)
    return a or b


class GCD: # нечётный вариант
    def __init__(self, *nums):
        self.nums = list(nums)

    def count(self) -> int:
        nums = self.nums
        while len(nums) > 1:
            nums = [gcd(*nums[0:2])] + nums[2:]

        return nums[0]


a = [24, 36, 72]
print(GCD(*a).count()) # работает для люого кол-ва чисел

