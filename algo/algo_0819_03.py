# 계산기2
from collections import deque

T = 10

for t in range(1, T+1):
    N = int(input())
    mid = [x for x in input()]
    front = []

    rank = {'+': 0, '*': 1}

    stack = deque()
    for m in mid:
        if m.isdecimal():
            front.append(int(m))
        else:
            if len(stack) == 0:
                stack.append(m)
            else:
                # 스택에 있는 연산자가 우선순위가 더 높거나 같다면, pop하기
                if rank[stack[-1]] >= rank[m]:
                    while stack and rank[stack[-1]] >= rank[m]:
                        front.append(stack.pop())
                stack.append(m)
    
    while stack:
        front.append(stack.pop())
    
    for f in front:
        if f in ['+', '*']:
            b = stack.pop()
            a = stack.pop()
            if f == '+':
                stack.append(a+b)
            elif f == '*':
                stack.append(a*b)
        else:
            stack.append(f)

    result = stack.pop()

    print(f'#{t} {result}')