n = int(input())
info = []

for _ in range(n):
  x, y = map(int, input().split())
  info.append((x, y))

for bulk in info:
  rank = 1
  for bulk_1 in info:
    if bulk[0] < bulk_1[0] and bulk[1] < bulk_1[1]:
      rank += 1

  print(rank, end=" ")
