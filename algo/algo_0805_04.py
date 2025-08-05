# Flatten

T = 10

for test_case in range(1, T + 1):

    # 입력 받기
    dump = int(input())
    boxes = [int(x) for x in input().split()]

    # 박스 층수에 따른 개수
    box_cnt = [0] * 101

    # 평탄화층 기준 잡기
    total_box = 0
    for box in boxes:
        total_box += box
        box_cnt[box] += 1
    
    flat_floor = total_box // 100

    # 채운 횟수
    cnt_dump = 0

    low = 1
    empty_box = 0
    while cnt_dump < dump:
        empty_box += box_cnt[low]
        cnt_dump += empty_box
        low += 1
        if low == flat_floor:
            break
    
    if cnt_dump > dump:
        low -= 1
        cnt_dump = dump

    # 높은 곳에 있는 박스
    high_box = 0
    high = 100

    # 내린 박스 수
    cnt_down = 0

    while cnt_down < cnt_dump:
        high_box += box_cnt[high]
        cnt_down += high_box
        high -= 1
        if high == flat_floor:
            break
    
    if cnt_down > cnt_dump:
        high += 1
        cnt_down = cnt_dump

    print(f'#{test_case} {high - low}')