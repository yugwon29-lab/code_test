T = int(input())

for test_case in range(1, T + 1):

    # 5110. 수열 합치기
    N, M = map(int, input().split())
    num_row = [[int(x) for x in input().split()] for y in range(M)]

    result = []

    for i in range(M):
        if i == 0:
            result = result + num_row[i]
        else:
            crit = num_row[i][0]
            find_big = False
            for j in range(len(result)):
                if crit < result[j]:
                    result[j:j] = num_row[i]
                    find_big = True
                    break
            if not find_big:
                result += num_row[i]

    for i in range(11):
        if i == 0:
            print(f"#{test_case}", end=" ")
        elif i != 10:
            print(result[-i], end=" ")
        else:
            print(result[-i])

