# 숫자 카드

T = int(input())

for test_case in range(1, T + 1):

    # 입력 받기
    N = int(input())
    cards = [int(x) for x in input()]

    # 카운트 세는 리스트
    cnt = [0] * 10

    # 카드 수 세기
    for card in cards:
        cnt[card] += 1

    # 가장 많은 카드 찾기
    max_cnt = cnt[0]
    max_idx = 0
    
    for i in range(1, 10):
        if max_cnt <= cnt[i]:
            max_cnt = cnt[i]
            max_idx = i
    
    print(f'#{test_case} {max_idx} {max_cnt}')
