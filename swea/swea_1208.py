T = 10

for test_case in range(1, T + 1):

    # 1208. Flatten
    N = int(input())
    box_array = [int(x) for x in input().split()]

    num_array = [0] * 101
    total_box = 0

    # 층별 개수
    for box in box_array:
        num_array[box] += 1
        total_box += box

    # print(num_array)

    # print(min_height, max_height)

    # 평탄화 최고 층 (low가 여기까지 연산을 다하면 최대로 평탄화된 것)
    limit_height = total_box // 100

    # 덤프 횟수
    dump_cnt = 0
    down_cnt = 0

    # 시작 위치
    low, high = 0, 101

    # 채워야 하거나 채우는 박스의 개수
    small_box = 0
    big_box = 0

    while dump_cnt <= N:
        low += 1
        # 평탄화층을 초과하면 끝내기
        if low > limit_height:
            break
        small_box += num_array[low]
        dump_cnt += small_box

    dump_cnt = dump_cnt if dump_cnt <= N else N

    while down_cnt <= dump_cnt:
        high -= 1
        # 평탄화층 이하로 내려가면 끝내기
        if high <= limit_height:
            break
        big_box += num_array[high]
        down_cnt += big_box

    print(f"#{test_case} {high - low}")
