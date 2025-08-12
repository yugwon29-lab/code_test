# 괄호검사

T = int(input())

for t in range(1, T+1):
    in_str = input()

    size = 1000
    stack = [None] * size
    top = -1

    is_ok = True
    for s in in_str:
        if s in ['{', '(']:
            top += 1
            stack[top] = s
        elif s == '}':
            if stack[top] != '{':
                is_ok = False
                break
            else:
                top -= 1
        elif s == ')':
            if stack[top] != '(':
                is_ok = False
                break
            else:
                top -= 1
    if top != -1:
        is_ok = False
    
    print(f'#{t} {1 if is_ok else 0}')
