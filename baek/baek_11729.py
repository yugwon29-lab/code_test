# 11729. 하노이 탑 이동 순서


def hanoi(a, b, n):
    if n == 1:
        print(a, b)
    else:
        hanoi(a, 6 - a - b, n - 1)
        print(a, b)
        hanoi(6 - a - b, b, n - 1)


N = int(input())

print(2**N - 1)
hanoi(1, 3, N)
