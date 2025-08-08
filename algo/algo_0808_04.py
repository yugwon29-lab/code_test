# GNS

T = int(input())

for t in range(1, T+1):

    test_case, num = input().split()
    num = int(num)
    other_num = input().split()

    num_dict = {
        "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
        "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9,
    }

    # 카운팅 정렬
    cnt_list = [0] * 10
    num_list = [0] * num
    for on in other_num:
        cnt_list[num_dict[on]] += 1

    for i in range(1, 10):
        cnt_list[i] = cnt_list[i-1] + cnt_list[i]

    for on in other_num:
        cnt_list[num_dict[on]] -= 1
        num_list[cnt_list[num_dict[on]]] = on

    print(test_case)
    print(*num_list)