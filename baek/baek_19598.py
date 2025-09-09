# 19598. 최소 회의실 개수
import heapq

N = int(input())
meetings = []

for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort()

room = []
for i in range(N):
    if len(room) == 0:
        heapq.heappush(room, meetings[i][1])
    else:
        if meetings[i][1] >= room[0]:
            heapq.heappop(room)
        heapq.heappush(room, meetings[i][1])

print(len(room))