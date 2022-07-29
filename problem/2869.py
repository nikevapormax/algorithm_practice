a, b, v = map(int, input().split())
move_day = (v-b) / (a-b)

if move_day == int(move_day):
    print(int(move_day))
else:
    print(int(move_day) + 1)
