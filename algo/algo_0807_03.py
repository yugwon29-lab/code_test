# 부분집합의 합

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    array = list(range(1, 13))

    cnt_num = 0

    for i in range(1 << 12):
        sum_v = 0
        cnt_elem = 0
        for j in range(12):
            if i & (1 << j):
                cnt_elem += 1
                sum_v += array[j]
                if cnt_elem > N:
                    break
    
        if cnt_elem == N:
            if sum_v == K:
                cnt_num += 1

    print(f'#{t} {cnt_num}')
