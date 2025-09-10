# 14956. Philosopher's Walk
N, M = map(int, input().split())

def walk(i, m):
    if i == 2:
        if m == 1:
            return 0, 0
        elif m == 2:
            return 0, 1
        elif m == 3:
            return 1, 1
        else:
            return 1, 0
    else:
        half = i // 2
        num = half * half
        if 0 < m <= num:
            x, y = walk(half, m)
            return y, x
        elif num < m <= num * 2:
            x, y = walk(half, m-num)
            return x, y + half
        elif num * 2 < m <= num * 3:
            x, y = walk(half, m-num*2)
            return x + half, y + half
        else:
            x, y = walk(half, m-num*3)
            return half - 1 - y + half, half - 1 - x

x, y = walk(N, M)

print(x+1, y+1)