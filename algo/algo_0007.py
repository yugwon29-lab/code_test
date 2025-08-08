# 연습 문제 8
# #의 수는?

N = int(input())
text = [list(input()) for _ in range(N)]

cnt_dmg = 0
for i in range(N):
    for j in range(N):
        if '#' == text[i][j]:
            cnt_dmg += 1

print(cnt_dmg)