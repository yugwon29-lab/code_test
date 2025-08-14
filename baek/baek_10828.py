# 10828. 스택

N = int(input())

size = 10000
stack = [0] * size
top = -1

for i in range(N):
    cmd = input()
    if cmd[:4] == 'push':
        num = int(cmd.split()[1])
        top += 1
        stack[top] = num
    elif cmd[:3] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
    elif cmd[:3] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif cmd[:5] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif cmd[:4] == 'size':
        print(top+1)