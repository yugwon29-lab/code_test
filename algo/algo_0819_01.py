# 배열 최소 합

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input().split()] for _ in range(N)]

    min_total = float('inf')
    # 열 선택 배열 (i열 선택 시, i번째 원소 True)
    select = [False] * N

    def dfs(cur, total):
        global min_total

        # 완성 시, min_total 값 저장
        if cur == N:
            if min_total > total:
                min_total = total
            return

        # 백트래킹 : 이미 합이 최소를 넘겼다면 그만두기
        if min_total < total:
            return
        
        for i in range(N):
            if not select[i]:
                select[i] = True
                dfs(cur+1, total+arr[cur][i])
                select[i] = False

    dfs(0, 0)
    print(f'#{t} {min_total}')