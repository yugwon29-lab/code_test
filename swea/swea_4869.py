T = int(input())

memo = [1, 3]

for i in range(1, T + 1):

    # 4869.종이붙이기
    N = int(input())

    def paper(n):
        global memo
        idx = n - 1
        if n > len(memo):
            memo.append(2 * paper(n-2) + paper(n-1))
        return memo[idx]
    
    n = N // 10

    print(f"#{i} {paper(n)}")