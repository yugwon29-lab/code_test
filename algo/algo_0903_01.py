# 암호코드 스캔
T = int(input())

for t in range(1, T+1):
    R, C = map(int, input().split())
    pattern = []

    code_set = list()

    def hex_to_bin(x):
        hex_str = '0x' + x
        integer = int(hex_str, 16)
        b3 = (integer // 8) % 2
        b2 = (integer // 4) % 2
        b1 = (integer // 2) % 2
        b0 = integer % 2
        return b3, b2, b1, b0

    for i in range(R):
        line = input()
        p_line = []
        for j in range(C):
            bin_code = hex_to_bin(line[j])
            for b in bin_code:
                p_line.append(b)
        pattern.append(p_line)

    # 암호 코드 인식 중인지?
    is_code = False
    # 0을 카운트 중인지?
    is_zero = True
    # 현재 0 또는 1의 카운트
    cnt = 0
    # 전체 카운트 수
    total_cnt = 0
    # Stack으로 동작할 예정
    zero_one = []
    # 연속된 블록이면 패스 가능
    pass_one = [0] * (C * 4)
    pass_idx = -1

    for i in range(R):
        # 뒤에서부터 본다.
        j = (C * 4) - 1
        while j >= 0:
            if pass_one[j] != 0 and not is_code and pattern[i][j] == 0:
                pass_one[j] = 0
            # 암호코드의 시작
            elif not is_code and pattern[i][j] == 1:
                if pass_one[j] != 0:
                    j -= pass_one[j]
                    continue
                is_code = True
                is_zero = False

                cnt += 1
                total_cnt += 1

                pass_idx = j
            
            elif is_code:
                if is_zero:
                    if pattern[i][j] == 1:
                        is_zero = False

                        zero_one.append(cnt)
                        cnt = 0

                    cnt += 1
                    total_cnt += 1
                else:
                    if pattern[i][j] == 0:
                        is_zero = True

                        zero_one.append(cnt)
                        cnt = 0
                    
                    cnt += 1
                    total_cnt += 1

                if len(zero_one) == 31 and total_cnt % 56 == 0:
                    zero_one.append(cnt)
                    cnt = 0

                    times = total_cnt // 56
                    pass_one[pass_idx] = total_cnt
                    total_cnt = 0

                    code = []
                    while zero_one:
                        code.append(zero_one.pop() // times)
                    code_set.append(code)

                    is_code = False

            
            j -= 1

    def get_reult(code_set):
        total = 0
        for code in code_set:
            real_number = []
            for i in range(8):
                if code[4*i:4*i+4] == [3, 2, 1, 1]:
                    real_number.append(0)
                elif code[4*i:4*i+4] == [2, 2, 2, 1]:
                    real_number.append(1)
                elif code[4*i:4*i+4] == [2, 1, 2, 2]:
                    real_number.append(2)
                elif code[4*i:4*i+4] == [1, 4, 1, 1]:
                    real_number.append(3)
                elif code[4*i:4*i+4] == [1, 1, 3, 2]:
                    real_number.append(4)
                elif code[4*i:4*i+4] == [1, 2, 3, 1]:
                    real_number.append(5)
                elif code[4*i:4*i+4] == [1, 1, 1, 4]:
                    real_number.append(6)
                elif code[4*i:4*i+4] == [1, 3, 1, 2]:
                    real_number.append(7)
                elif code[4*i:4*i+4] == [1, 2, 1, 3]:
                    real_number.append(8)
                elif code[4*i:4*i+4] == [3, 1, 1, 2]:
                    real_number.append(9)

            even, odd = 0, 0
            for j in range(7):
                if j % 2 == 0:
                    odd += real_number[j]
                else:
                    even += real_number[j]
            if (odd * 3 + even + real_number[7]) % 10 == 0:
                total += (odd + even + real_number[7])

        return total
    
    print(f'#{t} {get_reult(code_set)}')

