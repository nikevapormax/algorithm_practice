t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    a_a, b_b = a, b
    while b_b != 0:
        a_a = a_a % b_b
        a_a, b_b = b_b, a_a

    print(a*b // a_a)
