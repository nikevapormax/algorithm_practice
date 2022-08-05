k = int(input())
stack = []

for _ in range(k):
    i = int(input())

    if i > 0:
        stack.append(i)
    else:
        del(stack[-1])

print(sum(stack))
