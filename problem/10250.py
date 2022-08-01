t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    room = []

    for ho in range(1, w+1):
        for height in range(1, h+1):
            room.append(height*100 + ho)

    print(room[n-1])
