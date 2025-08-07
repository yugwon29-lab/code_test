# 1267. 작업순서
# from collections import deque

# T = 10

# for test_case in range(1, T + 1):

#     V, E = map(int, input().split())

#     lane = [int(x) for x in input().split()]

#     last_dict = {}
#     done = [False] * (V + 1)
#     can_work = [True] * (V + 1)

#     for i in range(E):
#         first, last = lane[2*i], lane[2*i+1]
#         # 이 일을 완료하려면 선행 작업이 필요하다.
#         can_work[last] = False
#         last_dict[last] = last_dict.get(last, list()) + [first]

#     work_list = []
#     queue = deque(range(1, V+1))

#     while queue:
#         now = queue.popleft()
#         if done[now]:
#             continue

#         # 할 수 있는 상태인지 확인
#         if not can_work[now]:
#             can_do = True
#             for todo in last_dict[now]:
#                 if not done[todo]:
#                     can_do = False
#                     queue.appendleft(todo)
#             # 아직 할 수 없다면 보류
#             if can_do:
#                 done[now] = True
#                 work_list.append(now)
#             else:
#                 queue.append(now)
#         else:
#             done[now] = True
#             work_list.append(now)


#     print(f'#{test_case}', end=' ')
#     print(*work_list)

# 위상 정렬을 사용한 재도전

from collections import deque

T = 10

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    lane = [int(x) for x in input().split()]

    graph = [[] for _ in range(V + 1)]
    in_degrees = [0] * (V + 1)

    for i in range(E):
        first, last = lane[2*i], lane[2*i+1]
        graph[first].append(last)
        in_degrees[last] += 1

    queue = deque()

    for i in range(1, V + 1):
        if in_degrees[i] == 0:
            queue.append(i)

    work_list = []
    while queue:
        now = queue.popleft()
        work_list.append(now)
        for nxt in graph[now]:
            in_degrees[nxt] -= 1
            if in_degrees[nxt] == 0:
                queue.append(nxt)
    
    print(f'#{test_case}', end=' ')
    print(*work_list)