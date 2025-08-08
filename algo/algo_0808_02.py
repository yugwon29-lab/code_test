# 회문

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())
    text = [list(input()) for _ in range(N)]

    abba = None

    # 가로 체크
    for i in range(N):   
        for j in range(N-M+1):
            find_abba = True
            for k in range(M // 2):
                if text[i][j+k] != text[i][M-N+j-k-1]:
                    find_abba = False
                    break
            if find_abba:
                abba = ''.join(text[i][j:j+M])
    
    for j in range(N):
        for i in range(N-M+1):
            find_abba = True
            for k in range(M // 2):
                if text[i+k][j] != text[M-N+i-k-1][j]:
                    find_abba = False
                    break
            if find_abba:
                abba = ''.join([text[i+s][j] for s in range(M)])

    print(f'#{t} {abba}')
    