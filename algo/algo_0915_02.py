# 창용 마을 무리의 개수
T = int(input())

def make_set(n):
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)
    return parents, ranks
    
def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return
    
    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        # rank가 동일
        # 한 쪽으로 병합하고 대표자의 rank를 +1
        parents[rep_y] = rep_x
        ranks[rep_x] += 1

for t in range(1, T+1):
    N, M = map(int, input().split())
    parents, ranks = make_set(N)

    for i in range(M):
        a, b = map(int, input().split())
        union(a, b)

    team = [False] * (N+1)
    cnt = 0
    for j in range(1, N+1):
        rep_j = find_set(j)
        if not team[rep_j]:
            team[rep_j] = True
            cnt += 1
    
    print(f'#{t}', cnt)