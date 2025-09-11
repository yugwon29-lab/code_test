# 수영장
T = int(input())

for t in range(1, T+1):
    d, om, tm, y = map(int, input().split())
    month = [int(x) for x in input().split()]

    min_pay = y
    def pay(cur, cost):
        global min_pay
        if cur >= 12:
            if min_pay is None or min_pay > cost:
                min_pay = cost
            return
        
        if min_pay is not None and min_pay <= cost:
            return
        
        # 이번 달은 일일 요금제로 간다
        if month[cur] * d < om:
            pay(cur+1, cost+(month[cur] * d))
        else:
        # 이번 달은 한달 요금제로 간다
            pay(cur+1, cost+om)
        # 이번 3달은 세달 요금제로 간다
        pay(cur+3, cost+tm)

    pay(0, 0)
    print(f'#{t}', min_pay)
        