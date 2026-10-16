



def random_generator(start=14_563, count=10) -> list[int]:
    result = []

    for _ in range(count):
        start = (start ** 2 // 100) % 100_000
        result.append(start)

    return result



print(random_generator())