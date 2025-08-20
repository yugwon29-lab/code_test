# 회전
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    queue = [int(x) for x in input().split()]

    # 현재 위치
    now = 0

    # 맨 뒤로 보내면 맨 앞에 있는 원소가 1칸씩 오른쪽으로 간다.
    now = (now + M) % N

    print(f'#{t} {queue[now]}')