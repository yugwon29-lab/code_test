# 11723. 집합
import sys

M = int(sys.stdin.readline())
S = 0
for m in range(M):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'add':
        x = int(cmd[1])
        if not S & (1 << (x-1)):
            S = S | (1 << (x-1))
    elif cmd[0] == 'remove':
        x = int(cmd[1])
        if S & (1 << (x-1)):
            S = S & ~(1 << (x-1))
    elif cmd[0] == 'check':
        x = int(cmd[1])
        if S & (1 << (x-1)):
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        x = int(cmd[1])
        S = S ^ (1 << (x-1))
    elif cmd[0] == 'all':
        S = (1 << 20) - 1
    elif cmd[0] == 'empty':
        S = 0