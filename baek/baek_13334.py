# 13334. 철로
import heapq

N = int(input())

going = []
for _ in range(N):
    s, e = map(int, input().split())
    if e < s:
        s, e = e, s
    going.append((e, s))
going.sort()

D = int(input())

idx = 0
max_p = 0

# 선로의 끝점
end = None
road = []

while idx < N:
    e, s = going[idx]

    # 현재 끝점에 선로의 끝점 맞추기
    end = e

    # 우선순위 큐에는 시작점을 넣는다.
    heapq.heappush(road, s)

    while road and road[0] < end - D:
        heapq.heappop(road)
    
    max_p = max(max_p, len(road))

    idx += 1

print(max_p) 