# 10872. 팩토리얼

N = int(input())

def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n-1)
    
print(facto(N))
