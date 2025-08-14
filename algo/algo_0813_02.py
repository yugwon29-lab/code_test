# 종이붙이기

T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    f = [0] * (N//10 + 1)

    for i in range(1, N//10 + 1):
        if i == 1:
            f[i] = 1
        elif i == 2:
            f[2] = 3
        else:
            f[i] = 2 * f[i-2] + f[i-1]

    print(f'#{t} {f[N//10]}')