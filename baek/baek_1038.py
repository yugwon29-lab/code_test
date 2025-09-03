# 1038. 감소하는 수

N = int(input())

def check_dec(num):
    is_dec = True

    max_d = 10
    mod = num % 10
    diff = max_d - mod

    while True:
        num = num // 10
        if num == 0:
            break
        if num % 10 <= mod:
            is_dec = False
            break

        max_d *= 10
        mod = num % 10
        diff = max_d - (mod * max_d // 10)

    return is_dec, diff

i = 0
num = 0
while True:
    is_dec, diff = check_dec(num)
    if is_dec:
        if i == N:
            print(num)
            break
        i += 1
        
    else:
        num += diff - 1
    num += 1
    if num > 9876543210:
        print(-1)
        break

    
    
