T = int(input())

for i in range(1, T + 1):

    # 4834.숫자 카드
    N = int(input())
    a = [int(x) for x in input()]

    cnt_list = [0 for i in range(10)]
    for card in a:
        cnt_list[card] += 1
    
    max_cnt = 0
    max_num = 0
    for j, cnt in enumerate(cnt_list):
        if cnt >= max_cnt:
            max_cnt = cnt
            max_num = j
    
    print(f'#{i} {max_num} {max_cnt}')
