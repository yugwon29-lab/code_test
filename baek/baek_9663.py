# 9663. N-Queen

N = int(input())
check_1 = [False] * N
check_2 = [False] * (2*N)
check_3 = [False] * (2*N)

# 경우의 수 세기
cnt = 0

def dfs(i):
    global cnt

    # 종료 조건
    # Queen이 N개 놓였을 때
    if i == N:
        cnt += 1
        return
    
    for j in range(N):
        if check_1[j] or check_2[i+j] or check_3[i-j+N]:
            continue
        check_1[j] = check_2[i+j] = check_3[i-j+N] = True
        dfs(i+1)
        check_1[j] = check_2[i+j] = check_3[i-j+N] = False   

dfs(0)
print(cnt)