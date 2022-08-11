import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list = sorted(num_list)

print(int(round(sum(num_list) / n, 0)))
print(num_list[n // 2])

frequency = Counter(num_list).most_common()
if len(frequency) > 1 and frequency[0][1] == frequency[1][1]:
    print(frequency[1][0])
else:
    print(frequency[0][0])

print(max(num_list) - min(num_list))
