# 계산기1
from collections import deque

T = 10

for t in range(1, T+1):
    
    N = int(input())
    formula = input()

    stack = deque()
    back_formula = ''

    for f in formula:
        if f.isdecimal():
            back_formula += f
        else:
            if f == '+':
                while len(stack) > 0:
                    back_formula += stack.pop()
                stack.append(f)

    while len(stack) > 0:
        back_formula += stack.pop()

    for bf in back_formula:
        if bf.isdecimal():
            stack.append(int(bf))
        else:
            if bf == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
    
    result = stack.pop()

    print(f'#{t} {result}')