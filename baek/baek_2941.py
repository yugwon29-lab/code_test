# 2941.크로아티아 알파벳

alpha = input()

two = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
three = ['dz=']

idx = 0
cnt_alpha = 0
while idx < len(alpha):
    if alpha[idx:idx+2] in two:
        idx += 2
        cnt_alpha += 1
    elif alpha[idx:idx+3] in three:
        idx += 3
        cnt_alpha += 1
    else:
        idx += 1
        cnt_alpha += 1

print(cnt_alpha)