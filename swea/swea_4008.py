T = int(input())

for test_case in range(1, T + 1):

    # 4008. 숫자 만들기
    N = int(input())
    pmmd = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_value, min_value = -1E8, 1E8

    def calculate(op_list, plus, minus, times, divide, result):
        global max_value, min_value

        cur = len(op_list)

        if cur == N - 1:
            if max_value < result:
                max_value = result
            if min_value > result:
                min_value = result
            return
        
        if plus < pmmd[0]:
            calculate(op_list+['+'], plus+1, minus, times, divide, result + numbers[cur+1])
        if minus < pmmd[1]:
            calculate(op_list+['-'], plus, minus+1, times, divide, result - numbers[cur+1])
        if times < pmmd[2]:
            calculate(op_list+['*'], plus, minus, times+1, divide, result * numbers[cur+1])
        if divide < pmmd[3]:
            calculate(op_list+['/'], plus, minus, times, divide+1, result // numbers[cur+1] if result >= 0 else - ((- result) // numbers[cur+1]))

    calculate([], 0, 0, 0, 0, numbers[0])
    print(f'#{test_case} {max_value - min_value}')