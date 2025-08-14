# Forth
from collections import deque

T = int(input())

for t in range(1, T+1):
    formula = input().split()

    stack = deque()
    is_error = False
    result = None

    for f in formula:
        if f.isdecimal():
            stack.append(int(f))
        else:
            if f == '.':
                if len(stack) == 0:
                    is_error = True
                    break
                result = stack.pop()
                if result in ['+', '-', '*', '/', '.'] or len(stack) != 0:
                    is_error = True
                    break
            else:
                if len(stack) < 2:
                    is_error = True
                    break
                b = stack.pop()
                a = stack.pop()
                if a in ['+', '-', '*', '/', '.'] or b in ['+', '-', '*', '/', '.']:
                    is_error = True
                    break
                if f == '+':
                    stack.append(a+b)
                elif f == '-':
                    stack.append(a-b)
                elif f == '/':
                    stack.append(a//b)
                elif f == '*':
                    stack.append(a*b)
    
    print(f'#{t} {result if not is_error else "error"}')