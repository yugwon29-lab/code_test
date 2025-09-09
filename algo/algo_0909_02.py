# 자기 방으로 돌아가기
T = int(input())

for t in range(1, T+1):
    N = int(input())
    student = []
    for _ in range(N):
        s, e = map(int, input().split())
        if s >= e:
            student.append(((e+1)//2, (s+1)//2))
        else:
            student.append(((s+1)//2, (e+1)//2))
    student.sort()

    come_back = [False] * N
    cnt = 0
    while True:
        change = False
        end = 0
        for i in range(N):
            if not come_back[i]:
                if student[i][0] > end and student[i][1] > end:
                    end = student[i][1]
                    change = True
                    come_back[i] = True
        if not change:
            break
        cnt += 1

    print(f'#{t} {cnt}')