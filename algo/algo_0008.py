# 연습 문제 9
# AB
# CD 패턴이 존재하는가?

N = int(input())
text = [list(input()) for _ in range(N)]

is_abcd = False

for i in range(N-1):
    for j in range(N-1):
        if text[i][j] == 'A' and text[i][j+1] == 'B':
            if text[i+1][j] == 'C' and text[i+1][j+1] == 'D':
                is_abcd = True
                break

print(is_abcd)