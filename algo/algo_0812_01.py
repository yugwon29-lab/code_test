# 파스칼의 삼각형

T = int(input())

for t in range(1, T+1):
    N = int(input())

    # 스택 선언
    stack = [0] * N
    top = -1

    n = 1
    print(f'#{t}')
    while n <= N:

        for k in range(n):
            if k == 0 or k == n - 1:
                value = 1
            else:
                value = temp + stack[top+1]
            top += 1
            temp = stack[top]
            stack[top] = value

        for k in range(n):
            top -= 1
            print(stack[top+1], end=' ')

        print()
        n += 1
