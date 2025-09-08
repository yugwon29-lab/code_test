# 11286. 절댓값 힙
import heapq

N = int(input())
pq_p = []
pq_m = []

for _ in range(N):
    cmd = int(input())
    if cmd != 0:
        if cmd > 0:
            heapq.heappush(pq_p, abs(cmd))
        if cmd < 0:
            heapq.heappush(pq_m, abs(cmd))
    else:
        if len(pq_p) == 0 and len(pq_m) == 0:
            print(0)
        elif len(pq_m) == 0:
            print(heapq.heappop(pq_p))
        elif len(pq_p) == 0:
            print(-heapq.heappop(pq_m))
        else:
            if pq_p[0] >= pq_m[0]:
                print(-heapq.heappop(pq_m))
            elif pq_p[0] < pq_m[0]:
                print(heapq.heappop(pq_p))