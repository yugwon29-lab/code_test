# 초심자의 회문 검사

T = int(input())

for t in range(1, T+1):

    text = list(input())

    is_pali = True
    for i in range(len(text) // 2):
        if text[i] != text[-i-1]:
            is_pali = False
            break

    print(f'#{t} {1 if is_pali else 0}')