TC = int(input())

for t in range(1, TC+1):
    N, min_s, max_s = map(int, input().split())
    score = [int(x) for x in input().split()]

    score_cnt = [0] * (100 + 1)
    for s in score:
        score_cnt[s] += 1

    low_class = 0
    mid_class = 0
    high_class = 0

    diff = 10000

    score1 = 0
    while True:
        if score1 > 100:
            break
        low_class += score_cnt[score1]
        score1 += 1

        if min_s <= low_class <= max_s:
            mid_class = 0
            score2 = score1
            while True:
                if score2 > 100:
                    break
                mid_class += score_cnt[score2]
                score2 += 1

                if min_s <= mid_class <= max_s:
                    if min_s <= N - low_class - mid_class <= max_s:
                        high_class = N - low_class - mid_class
                        diff = min(max(low_class, mid_class, high_class) - min(low_class, mid_class, high_class), diff)
                    else:
                        break
                
    if diff == 10000:
        print(f'#{t} -1')
    else:
        print(f'#{t} {diff}')

