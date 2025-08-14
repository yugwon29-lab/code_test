# 2775. 부녀회장이 될테야

T = int(input())

for t in range(1, T+1):
    K = int(input())
    N = int(input())

    house = [[0] * 15 for _ in range(15)]

    for k in range(0, K+1):
        for n in range(1, N+1):
            if k == 0:
                house[k][n] = n
            else:
                house[k][n] = house[k][n-1] + house[k-1][n]
    
    print(house[k][n])
            