# 1715. 카드 정렬하기
import heapq

N = int(input())
pq = []
for _ in range(N):
    heapq.heappush(pq, int(input()))

cnt = 0
while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    cnt += a + b
    heapq.heappush(pq, a + b)
print(cnt)