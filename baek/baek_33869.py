# 33869. 일기 암호화하기
W = input()
S = input()

alpha_used = [False] * 26
alpha_list = []

for alpha in W:
    alpha_idx = ord(alpha) - ord('A')
    if not alpha_used[alpha_idx]:
        alpha_used[alpha_idx] = True
        alpha_list.append(alpha)

for idx in range(26):
    if not alpha_used[idx]:
        alpha_used[idx] = True
        alpha = chr(ord('A') + idx)
        alpha_list.append(alpha)

new_word = ""
for s in S:
    idx = ord(s) - ord('A')
    new_word += alpha_list[idx]

print(new_word)