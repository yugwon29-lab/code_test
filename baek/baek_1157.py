# 1157. 단어 공부

string = input().upper()

cnt_dict = dict()
max_letter = []
max_cnt = 0
for s in string:
    cnt_dict[s] = cnt_dict.get(s, 0) + 1
    if cnt_dict[s] > max_cnt:
        max_letter.clear()
        max_letter.append(s)
        max_cnt = cnt_dict[s]
    elif cnt_dict[s] == max_cnt:
        max_letter.append(s)

if len(max_letter) == 1:
    print(max_letter[0])
else:
    print("?")
