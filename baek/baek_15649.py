# 15649. N과 M (1)

# 입력 받기
N, M = map(int, input().split())
visit = [0] * (N+1)

def n_m(cur, num_list=[]):
    if cur == M:
        print(*num_list)
        return
    
    for i in range(1, N+1):
        if visit[i]:
            continue
        num_list.append(i)
        visit[i] = 1
        n_m(cur+1, num_list)
        num_list.pop()
        visit[i] = 0

n_m(0, [])