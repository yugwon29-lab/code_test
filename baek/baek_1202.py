# 1202. 보석 도둑
import heapq

N, K = map(int, input().split())
jewel = []
bag = []

for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(jewel, (value, -weight))

for _ in range(K):
    b = int(input())
    heapq.heappush(bag, -b)

max_value = 0
while bag and jewel:
    # 보석 꺼내기
    v, w = heapq.heappop(jewel)
    # 넣을 수 있으면 넣기
    if -w <= -bag[0]:
        max_value += v
        heapq.heappop(bag)
        

print(max_value)