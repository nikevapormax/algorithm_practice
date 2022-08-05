t = int(input())

for _ in range(t):
    test = input()
    ps = []

    for i in test:
        if i == "(":
            ps.append("(")
        elif i == ")":
            if len(ps) > 0:
                ps.pop()
            else:
                print("NO")
                break
    else:
        if len(ps) == 0:
            print("YES")
        else:
            print("NO")
