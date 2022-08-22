def arrayNum(num):
    if len(list) == m:
        print(" ".join(map(str, list)))
        return

    for i in range(num, n+1):
        if i not in list:
            list.append(i)
            arrayNum(i+1)
            list.pop()


n, m = map(int, input().split())
list = []
arrayNum(1)
