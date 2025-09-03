# 암호코드 스캔
T = int(input())

for t in range(1, T+1):
    R, C = map(int, input().split())
    pattern = []

    code_set = set()

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

    is_code = False
    is_zero = True
    cnt = 0
    total_cnt = 0
    # Stack으로 동작할 예정
    zero_one = []
    # 연속된 블록이면 패스 가능
    pass_one = []
    pass_cnt = []

    for i in range(R):
        j = C-1
        while j >= 0:
            # 이 때는 확정적
            if len(zero_one) == 7:
                if total_cnt % 56 == 0:
                    times = total_cnt // 56
                    pass_cnt.append(total_cnt)
                    code = []
                    for zo in range(zero_one):
                        code.append(zo // times)
                    
                else:
                    cnt += 1
                    total_cnt += 1
                continue
            # 첫 1이면 카운트 시작
            if not is_code and pattern[i][j] == 1:
                is_code = True
                is_zero = False
                cnt += 1
                total_cnt += 1
                pass_one.append(j)
            elif is_code:
                if pattern[i][j] == 1:
                    if is_zero:
                        is_zero = False
                        zero_one.append(cnt)
                        cnt = 0
                    total_cnt += 1
                    cnt += 1
                else:
                    if not is_zero:
                        is_zero = True
                        zero_one.append(cnt)
                        cnt = 0
                    total_cnt += 1
                    cnt += 1
            j -= 1
            

