n = int(input())
coord = []

for _ in range(n):
    x, y = map(int, input().split())
    coord.append([y, x])

for c in sorted(coord):
    print(c[1], c[0])
