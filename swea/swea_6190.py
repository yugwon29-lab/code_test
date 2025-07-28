T = int(input())

for test_case in range(1, T + 1):

    # 6190. 정곤이의 단조 증가하는 수
    N = int(input())
    num = [int(x) for x in input().split()]

    def is_increase(num):
        last_num = num % 10
        num = num // 10
        incr = True
        while num != 0:
            if last_num < num % 10:
                incr = False
                break
            last_num = num % 10
            num = num // 10
        
        return incr
    
    max_value = 0
    for i in range(N):
        for j in range(N):
            if j > i:
                if is_increase(num[i] * num[j]):
                    max_value = max(max_value, num[i] * num[j])

    if max_value > 0:
        print(f'#{test_case} {max_value}')
    else:
        print(f'#{test_case} -1')
                