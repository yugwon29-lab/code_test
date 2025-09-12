# 9997. 폰트
N = int(input())

FULL = (1 << 26) - 1

words = []
for _ in range(N):
    word = input()
    word_num = 0
    for w in word:
        w_num = ord(w) - ord('a')
        if word_num & (1 << w_num):
            continue
        word_num += (1 << w_num)
    words.append(word_num)

cnt = 0
def choice(idx, cur):
    global cnt
    if idx == N:
        if cur == FULL:
            cnt += 1
        return
    
    choice(idx+1, cur|words[idx])
    choice(idx+1, cur)


choice(0, 0)
print(cnt)