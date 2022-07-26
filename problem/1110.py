n = int(input())
result_n = n
cycle = 0

while True:
    new_first = (result_n % 10) * 10
    new_second = (result_n // 10 + result_n % 10) % 10

    result_n = new_first + new_second

    cycle += 1

    if result_n == n:
        break

print(cycle)
