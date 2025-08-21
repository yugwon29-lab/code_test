# 1931. 회의실 배정

N = int(input())
confer = []
for _ in range(N):
    start, end = map(int, input().split())
    confer.append((end, start))

confer.sort()

# 가장 빨리 끝나는 회의를 계속 찾는다.
n_conf = 0
end_time = 0
for i in range(N):
    # 현재 회의 종료 시간보다 다음 회의 시작 시간이 빠른 경우 패스
    if end_time > confer[i][1]:
        continue
    n_conf += 1
    end_time = confer[i][0]

print(n_conf)