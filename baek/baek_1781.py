# 1781. 컵라면
import heapq

N = int(input())
hw = []
for _ in range(N):
    dl, cup = map(int, input().split())
    hw.append((dl, cup))

hw.sort()
work = []
idx = 0
while idx < N:
    dl, cup = hw[idx]
    heapq.heappush(work, cup)
    if dl < len(work):
        heapq.heappop(work)
    idx += 1

print(sum(work))