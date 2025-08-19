# 토너먼트 카드게임

T = int(input())

for t in range(1, T+1):
    N = int(input())
    cards = [int(x) for x in input().split()]

    def rsp_tour(s, e):
        if s == e:
            return s
        elif e - s == 1:
            return rsp(s, e)
        mid = (s+e) // 2
        return rsp(rsp_tour(s, mid), rsp_tour(mid+1, e))
        
    def rsp(a, b):
        i = cards[a]
        j = cards[b]
        if i == j:
            return a
        else:
            if i == 1:
                if j == 2:
                    return b
                elif j == 3:
                    return a
            elif i == 2:
                if j == 1:
                    return a
                elif j == 3:
                    return b
            elif i == 3:
                if j == 1:
                    return b
                elif j == 2:
                    return a
                
    winner = rsp_tour(0, N-1)
    print(f'#{t} {winner+1}')