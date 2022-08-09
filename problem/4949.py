while True:
    sentence = input()
    stack = []
    status = True

    if sentence == ".":
        break

    for s in sentence:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if not stack or stack[-1] == '[':
                status = False
                break
            elif stack[-1] == "(":
                stack.pop()
        elif s == "]":
            if not stack or stack[-1] == "(":
                status = False
                break
            elif stack[-1] == "[":
                stack.pop()

    if status == True and len(stack) == 0:
        print("yes")
    else:
        print("no")
