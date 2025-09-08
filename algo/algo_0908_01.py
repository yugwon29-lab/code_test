# 베이비진 게임
T = int(input())

for t in range(1, T+1):
    cards = [int(x) for x in input().split()]

    pc = [[0] * 10 for _ in range(2)]
    win = False

    for i in range(12):
        next_card = cards[i]
        player = i % 2
        pc[player][next_card] += 1

        # 플레이어가 3장 이상을 소유하고 있다면...
        if i >= 4:
            # Run 확인
            if pc[player][next_card] == 3:
                win = True
            # Triplet 확인
            for j in range(next_card-2, next_card+1):
                if j < 0 or j + 2 >= 10:
                    continue
                if pc[player][j] and pc[player][j+1] and pc[player][j+2]:
                    win = True
            if win:
                break
    
    if win:
        if player % 2 == 0:
            print(f'#{t} 1')
        else:
            print(f'#{t} 2')
    else:
        print(f'#{t} 0')