num = int(input())
stack = []
result = []
count = 1
status = True

for _ in range(num):
    n = int(input())
    while count <= n:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == n:
        stack.pop()
        result.append('-')
    else:
        status = False
        break

if status == False:
    print('NO')
else:
    for i in result:
        print(i)
