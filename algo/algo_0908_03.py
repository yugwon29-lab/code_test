# 컨테이너 운반
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = [int(x) for x in input().split()]
    trucks = [int(x) for x in input().split()]

    max_weights = 0

    # 그리디 - 각각의 트럭이 최대한 무거운 것을 들면 된다.
    weights.sort(reverse=True)
    trucks.sort(reverse=True)

    w = 0
    t = 0
    while t < M and w < N:
        if weights[w] <= trucks[t]:
            max_weights += weights[w]
            t += 1
        w += 1
    
    print(f'#{tc} {max_weights}')