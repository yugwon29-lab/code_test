# 1592. 영식이와 친구들

N, M, L = map(int, input().split())

ball_cnt = [0] * (N+1)
ball = 1
throw_cnt = 0

while True:
    ball_cnt[ball] += 1
    if ball_cnt[ball] == M:
        break
    if ball_cnt[ball] % 2 == 1:
        ball = (ball + L) % N
    else:
        ball = (ball - L) % N
    throw_cnt += 1

print(throw_cnt)