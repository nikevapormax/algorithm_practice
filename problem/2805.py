n, m = map(int, input().split())
trees = list(map(int, input().split()))
first, last = 1, max(trees)

# 이분탐색
while first <= last:
    mid = (first + last) // 2
    cut = 0

    for tree in trees:
        if tree >= mid:
            cut += tree - mid

    if cut >= m:
        first = mid + 1
    else:
        last = mid - 1

print(last)
