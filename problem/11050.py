n, k = map(int, input().split())
result_a = 1
result_b = 1

cnt_a = 0
for i in range(n, 1, -1):
    if cnt_a == k:
        break
    result_a *= i
    cnt_a += 1

cnt_b = 0
for j in range(k, 1, -1):
    if cnt_b == k:
        break
    result_b *= j
    cnt_b += 1

print(result_a // result_b)
