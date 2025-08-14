# 10870. 피보나치 수 5

N = int(input())

memo = [0] * 21
memo[0] = 0
memo[1] = 1

def fibo(n):
    if n >= 2:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(N))