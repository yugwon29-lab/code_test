# 1244. 스위치 켜고 끄기

N = int(input())
switches = [int(x) for x in input().split()]
M = int(input())
students = []
for _ in range(M):
    a, b = map(int, input().split())
    students.append((a, b))

for s in students:
    if s[0] == 1:
        for i in range(0, N):
            if (i+1) % s[1] == 0:
                switches[i] = 1 - switches[i]
    else:
        i = s[1] - 1
        j = 0
        while True:
            if j == 0:
                switches[i] = 1 - switches[i]
            else:
                if i - j < 0 or i + j > N - 1:
                    break
                if switches[i-j] != switches[i+j]:
                    break
                switches[i-j] = 1 - switches[i-j]
                switches[i+j] = 1 - switches[i+j]
            j += 1

for i in range(N):
    print(switches[i], end=' ')
    if i % 20 == 19:
        print()

