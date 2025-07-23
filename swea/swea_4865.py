T = int(input())

for i in range(1, T + 1):

    # 4865.글자수
    str1 = input()
    str2 = input()

    cnt_dict = {}

    for c in str1:
        if c in cnt_dict.keys():
            continue
        else:
            cnt = 0
            for cc in str2:
                if c == cc:
                    cnt += 1
            cnt_dict[c] = cnt
    
    max_cnt = 0
    for k in cnt_dict.keys():
        if max_cnt < cnt_dict[k]:
            max_cnt = cnt_dict[k]
    
    print(f"#{i} {max_cnt}")