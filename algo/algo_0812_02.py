# 반복문자 지우기

T = int(input())

for t in range(1, T+1):
    in_str = input()

    size = 1000
    stack = [None] * size
    top = -1

    for s in in_str:
        if top == -1 or stack[top] != s:
            top += 1
            stack[top] = s
        elif stack[top] == s:
            top -= 1
    
    print(f'#{t} {top+1}')
