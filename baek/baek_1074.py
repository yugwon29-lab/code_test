# 1074. Z
N, r, c = map(int, input().split())


def zet(n, r, c):
    if n == 1:
        return 2 * r + c
    else:
        half = 2 ** (n - 1)
        if r < half:
            if c < half:
                return zet(n - 1, r, c)
            else:
                return half * half * 1 + zet(n - 1, r, c - half)
        else:
            if c < half:
                return half * half * 2 + zet(n - 1, r - half, c)
            else:
                return half * half * 3 + zet(n - 1, r - half, c - half)


print(zet(N, r, c))
