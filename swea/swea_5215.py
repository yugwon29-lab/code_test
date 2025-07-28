T = int(input())

for test_case in range(1, T + 1):

    # 5215. 햄버거 다이어트
    N, L = map(int, input().split())
    food = []
    for _ in range(N):
        S, C = map(int, input().split())
        food.append((S, C))

    max_score = 0

    def check_food(idx, score, cal):
        global max_score
        
        if cal > L:
            return
        
        max_score = max(max_score, score)
        # print(max_score)
        
        for i in range(idx, N):
            check_food(i + 1, score + food[i][0],  cal + food[i][1])


    check_food(0, 0, 0)
    print(f'#{test_case} {max_score}')