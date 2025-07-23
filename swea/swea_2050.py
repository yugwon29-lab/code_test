# 2050. 알파벳을 숫자로 변환
string = input()

alpha = list('abcdefghijklmnopqrstuvwxyz')

alpha_dict = {}
for v, k in enumerate(alpha):
    alpha_dict[k] = v

string = string.lower()

for st in string:
    print(alpha_dict[st] + 1, end=' ')
