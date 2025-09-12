# 동아리실 관리하기
T = int(input())

for t in range(1, T+1):
    DIV = 1000000007

    # 담당자는 필참
    line = input()
    main = []
    for l in line:
        main.append(ord(l)-ord('A'))
                
    DP = [[0] * 16 for _ in range(len(line))]
    # 점화식
    # DP[i][j] = i번째 날 j 조합(비트 상 DCBA)으로 올 수 있는 경우의 수

    # 초기값
    for j in range(1, 16):
        if j & (1 << 0) and j & (1 << main[0]):
            DP[0][j] += 1

    for i in range(1, len(line)):
        for j in range(1, 16):
            for k in range(1, 16):
                if k & j and j & (1 << main[i]):
                    DP[i][j] += DP[i-1][k] % DIV

    total = 0
    for j in range(1, 16):
        total += DP[len(line)-1][j] % DIV

    print(f'#{t}', total % DIV)