T = int(input())

for i in range(1, T + 1):

    # 4866.괄호검사
    line = input()
    stack = []

    good = True
    for ch in line:
        if ch in ['{', '(']:
            stack.append(ch)
        elif ch == '}':
            if len(stack) == 0:
                good = False
                break
            if stack[-1] == '{':
                stack.pop(-1)
                continue
            else:
                good = False
                break
        elif ch == ')':
            if len(stack) == 0:
                good = False
                break
            if stack[-1] == '(':
                stack.pop(-1)
                continue
            else:
                good = False
                break

    if len(stack) != 0:
        good = False

    if good:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")