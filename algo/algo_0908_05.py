# 전봇대
T = int(input())

for t in range(1, T+1):
    N = int(input())
    lines = []

    # 교차점 개수
    cnt = 0
    for _ in range(N):
        a, b = map(int, input().split())
        for l in lines:
            if (a > l[0] and b < l[1]) or (a < l[0] and b > l[1]):
                cnt += 1
        lines.append((a, b))

    print(f'#{t} {cnt}')
        