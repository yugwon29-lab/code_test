T = int(input())

for i in range(1, T + 1):

    # 4864.문자열 비교
    str1 = input()
    str2 = input()
    
    l_str1 = len(str1)
    l_str2 = len(str2)

    # 보이어-무어 알고리즘 딕셔너리
    shift_dict = {}
    for j in range(l_str1):
        shift_dict[str1[j]] = l_str1 - j - 1

    # 보이어-무어 알고리즘
    k = l_str1 - 1  # 찾는 문자열 가장 마지막 인덱스부터 시작

    yes_str1 = False
    while k < l_str2:
        if str2[k] != str1[-1]:
            if str2[k] in shift_dict.keys():
                k = k + shift_dict[str2[k]]
            else:
                k = k + l_str1
        else:
            find_str1 = True
            for m in range(l_str1):
                if str2[k-m] != str1[-1-m]:
                    find_str1 = False
                    break
            
            if find_str1:
                yes_str1 = True
                break
            else:
                k = k + 1

    if yes_str1:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")
