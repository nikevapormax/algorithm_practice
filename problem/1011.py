t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    distance = y - x
    cnt = 0
    move = 1
    total_move = 0

    while distance > total_move:
        cnt += 1
        total_move += move
        if cnt % 2 == 0:
            move += 1
    print(cnt)
