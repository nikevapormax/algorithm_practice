c = int(input())

for _ in range(c):
    input_num = list(map(int, input().split()))

    input_sum = 0
    for num in input_num[1:]:
        input_sum += num

    input_avg = input_sum / input_num[0]

    count = 0
    for num in input_num[1:]:
        if num > input_avg:
            count += 1

    print(f'{(count/input_num[0]) * 100:.3f}%')
