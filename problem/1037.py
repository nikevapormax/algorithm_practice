n = int(input())

num = sorted(list(map(int, input().split())))
if len(num) == 1:
    print(num[0]**2)
else:
    print(num[0] * num[-1])
