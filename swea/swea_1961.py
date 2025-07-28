T = int(input())

for test_case in range(1, T + 1):

    # 1961. 숫자 배열 회전
    N = int(input())
    array = [[int(x) for x in input().split()] for _ in range(N)]

    print(f"#{test_case}")
    for i in range(N):
        rot_1, rot_2, rot_3 = [], [], []
        for j in range(N):
            rot_1.append(str(array[-1-j][i]))
            rot_2.append(str(array[-1-i][-1-j]))
            rot_3.append(str(array[j][-1-i]))
        print(f'{"".join(rot_1)} {"".join(rot_2)} {"".join(rot_3)}')

                