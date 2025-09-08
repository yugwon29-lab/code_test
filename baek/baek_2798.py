# 2798.블랙잭

N, M = map(int, input().split())
cards = [int(x) for x in input().split()]

max_sum = 0
is_used = [False] * N
def dfs(cur, i, now_sum):
    global max_sum

    if now_sum > M:
        return

    if cur == 3:
        if max_sum < now_sum:
            max_sum = now_sum
        return
    
    for j in range(i, N):
        if not is_used[j]:
            is_used[j] = True
            dfs(cur+1, j, now_sum+cards[j])
            is_used[j] = False

for k in range(N):
    dfs(0, k, 0)

print(max_sum)

