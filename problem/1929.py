def prime(m, n):
    prime = []

    for i in range(m, n + 1):
        if i == 1:
            continue

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            prime.append(i)

    return [print(p) for p in prime]


m, n = map(int, input().split())
prime(m, n)
