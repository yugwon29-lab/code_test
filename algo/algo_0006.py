# 연습 문제 7
# 첫 줄에 N, 다음에 N x N 문자열, 'Z'가 존재하는가?

N = int(input())
text = [list(input()) for _ in range(N)]

available = False
for i in range(N):
    for j in range(N):
        if 'Z' == text[i][j]:
            available = True
            break

print(available)