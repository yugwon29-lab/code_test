# 1629. 곱셈

A, B, C = map(int, input().split())


def timemod(a, b, c):
    if b == 1:
        return a % c
    else:
        half = timemod(a, b // 2, c)
        if b % 2 == 0:
            return (half * half) % c
        else:
            return (half * half * (a % c)) % c


print(timemod(A, B, C))
