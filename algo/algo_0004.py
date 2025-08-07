# 연습 문제 5
# 10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지 확인하기

T = int(input())

for test_case in range(1, T + 1):
    # 입력 받기
    # N = int(input())
    numbers = [int(x) for x in input().split()]

    is_sum_zero = False
    for i in range(1<<len(numbers)):
        sum_value = 0
        for j in range(len(numbers)):
            if i & (1<<j):
                sum_value += numbers[j]
        if sum_value == 0:
            is_sum_zero = True
            break

    if is_sum_zero:
        print(f'#{test_case} True')
    else:
        print(f'#{test_case} False')
