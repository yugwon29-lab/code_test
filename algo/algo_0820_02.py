# 피자
from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    cheeze = [int(x) for x in input().split()]

    # 치즈로 피자 만들기
    pizza = deque()
    for m in range(1, M+1):
        pizza.append([m, cheeze[m-1]])

    hwaduck = [[0, 0] for _ in range(N)]
    # 입구 위치
    now = 0
    last_pizza = -1
    num_pizza = 0

    # 우선 피자를 먼저 다 처리한다.
    while pizza:

        # 피자가 1바퀴 돌면, 치즈가 절반으로 녹는다.
        if hwaduck[now][1]:
            hwaduck[now][1] = hwaduck[now][1] // 2
            # 치즈가 다 녹아사라지면, 해당 피자 번호를 저장
            if hwaduck[now][1] == 0:
                last_pizza = hwaduck[now][0]
                num_pizza += 1

        # 피자가 없다면, 피자 넣기
        if not hwaduck[now][1]:
            hwaduck[now] = pizza.popleft()

        now = (now + 1) % N
    
    # 남은 피자가 없다면, 화덕의 모든 피자가 구워질 때까지 대기
    while True:
        # 피자가 1바퀴 돌면, 치즈가 절반으로 녹는다.
        if hwaduck[now][1]:
            hwaduck[now][1] = hwaduck[now][1] // 2
            # 치즈가 다 녹아사라지면, 해당 피자 번호를 저장
            if hwaduck[now][1] == 0:
                last_pizza = hwaduck[now][0]
                num_pizza += 1

        now = (now + 1) % N

        if num_pizza == M:
            break

    print(f'#{t} {last_pizza}')
