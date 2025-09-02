# 1138. 한 줄로 서기
N = int(input())
people = [0] + [int(x) for x in input().split()]
queue = [N+1] * N

for i in range(1, N+1):
    taller = 0
    idx = 0
    while True:
        if queue[idx] == N+1:
            if taller < people[i]:
                taller += 1
            else:
                break
        idx += 1
    queue[idx] = i

print(*queue)