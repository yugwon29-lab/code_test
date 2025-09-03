# 단순 이진 암호코드
T = int(input())

def to_num(code):
    num_code = []
    for i in range(8):
        if code[4*i:4*i+4] == [3, 2, 1, 1]:
            num_code.append(0)
        elif code[4*i:4*i+4] == [2, 2, 2, 1]:
            num_code.append(1)
        elif code[4*i:4*i+4] == [2, 1, 2, 2]:
            num_code.append(2) 
        elif code[4*i:4*i+4] == [1, 4, 1, 1]:
            num_code.append(3) 
        elif code[4*i:4*i+4] == [1, 1, 3, 2]:
            num_code.append(4) 
        elif code[4*i:4*i+4] == [1, 2, 3, 1]:
            num_code.append(5) 
        elif code[4*i:4*i+4] == [1, 1, 1, 4]:
            num_code.append(6) 
        elif code[4*i:4*i+4] == [1, 3, 1, 2]:
            num_code.append(7) 
        elif code[4*i:4*i+4] == [1, 2, 1, 3]:
            num_code.append(8) 
        elif code[4*i:4*i+4] == [3, 1, 1, 2]:
            num_code.append(9)
    return num_code

def check(code):
    even, odd = 0, 0
    for i in range(7):
        if i % 2 == 0:
            odd += code[i]
        else:
            even += code[i]

    if (odd * 3 + even + code[7]) % 10 == 0:
        return even + odd + code[7]
    else:
        return 0

for t in range(1, T+1):
    R, C = map(int, input().split())
    pattern = [[int(x) for x in input()] for _ in range(R)]
    
    find_pattern = False
    si, sj = -1, -1
    for i in range(R):
        for j in range(C-1, -1, -1):
            if pattern[i][j] == 1:
                find_pattern = True
                si, sj = i, j
                break
        if find_pattern:
            break
    
    si, sj = si, sj - 56 + 1
    code = []
    cnt = 0
    is_zero = True
    for k in range(56):
        if pattern[si][sj+k] == 1:
            if is_zero:
                code.append(cnt)
                cnt = 0
                is_zero = False
            cnt += 1
        else:
            if not is_zero:
                code.append(cnt)
                cnt = 0
                is_zero = True
            cnt += 1
    code.append(cnt)

    num_code = to_num(code)
    
    print(f'#{t} {check(num_code)}')
    
    
