# 2447. 별 찍기 - 10

N = int(input())

star_line = [['*'] * N for _ in range(N)]

def star(r, c, n):
    global star_line
    if n == 1:
        return
    else:
        size = n // 3
        for i in range(r+size, r+size*2):
            for j in range(c+size, c+size*2):
                star_line[i][j] = ' '
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                star(r+size*i, c+size*j, size)

star(0, 0, N)

for i in range(N):
    print(''.join(star_line[i]))