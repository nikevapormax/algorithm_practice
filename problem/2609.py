a, b = map(int, input().split())
list_a = []
list_b = []
list_c = []

for i in range(1, a+1):
    if a % i == 0:
        list_a.append(i)

for j in range(1, b+1):
    if b % j == 0:
        list_b.append(j)

for factor in list_a:
    for factor_b in list_b:
        if factor == factor_b:
            list_c.append(factor)

print(max(list_c))
print(max(list_c) * (a // max(list_c)) * (b // max(list_c)))
