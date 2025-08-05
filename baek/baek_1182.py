# 1182. 부분수열의 합

N, S = map(int, input().split())
num_list = [int(x) for x in input().split()]

cnt = 0

def add_list(cur, total=0):
    global cnt

    if cur == N:
        if total == S:
            cnt += 1
        return
    
    # 선택한 경우
    add_list(cur + 1, total + num_list[cur])
    # 선택하지 않은 경우
    add_list(cur + 1, total)

add_list(0, 0)
if S == 0:
    cnt -= 1
print(cnt)