# 4881. 자리수의 제곱
while True:
    A, B = map(int, input().split())
    if (A, B) == (0, 0):
        break

    a_list, b_list = [], []
    def new_num(num):
        new = 0
        while num > 0:
            mob = num % 10
            new += mob * mob
            num = num // 10
        return new
    
    a_loop, b_loop = False, False
    while True:

        a_list.append(A)
        A = new_num(A)
            
        # 중복 확인
        if A in a_list:
            a_loop = True
            break
    
    while True:

        b_list.append(B)
        B = new_num(B)
            
        # 중복 확인
        if B in b_list:
            b_loop = True
            break

    can_find = False
    min_value = -1
    for idx in range(len(a_list)):
        if a_list[idx] in b_list:
            can_find = True
            value = a_list.index(a_list[idx]) + 1 + b_list.index(a_list[idx]) + 1
            if min_value == -1 or min_value > value:
                min_value = value

    for idx in range(len(b_list)):
        if b_list[idx] in a_list:
            can_find = True
            value = a_list.index(b_list[idx]) + 1 + b_list.index(b_list[idx]) + 1
            if min_value == -1 or min_value > value:
                min_value = value

    if not can_find:
        print(a_list[0], b_list[0], 0)
    else:
        print(a_list[0], b_list[0], min_value)