# 1655. 가운데를 말해요
import heapq

N = int(input())
max_heap = []
min_heap = []
result = []

for _ in range(N):
    n = int(input())
    if len(max_heap) == 0:
        heapq.heappush(max_heap, -n)
    elif len(min_heap) == 0:
        if -max_heap[0] >= n:
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        else:
            heapq.heappush(min_heap, n)
    elif len(max_heap) == len(min_heap):
        if -max_heap[0] >= n:
            heapq.heappush(max_heap, -n)
        else:
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    else:
        if -max_heap[0] >= n:
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        else:
            heapq.heappush(min_heap, n)
    
    if len(max_heap) > len(min_heap):
        result.append(str(-max_heap[0]))
    else:
        result.append(str(min(-max_heap[0], min_heap[0])))

print('\n'.join(result))