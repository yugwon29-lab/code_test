# 1759. 암호 만들기

L, C = map(int, input().split())
letters = [x for x in input().split()]

def is_password(password):
    mo = ['a', 'e', 'i', 'o', 'u']
    mo_cnt, ja_cnt = 0, 0
    for p in password:
        if p in mo:
            mo_cnt += 1
        else:
            ja_cnt += 1
        if mo_cnt >= 1 and ja_cnt >= 2:
            return True
    return False

def dfs(j, password):
    
    # 종료 조건
    if len(password) == L:
        if is_password(password):
            print(password)
            return
        
    for i in range(j, C):
        dfs(i+1, password+letters[i])
    
# Letter 먼저 오름차순으로 배열
for n, l in enumerate(letters):
    min_l = l
    min_idx = n
    for i in range(n+1, len(letters)):
        if min_l > letters[i]:
            min_l = letters[i]
            min_idx = i
    letters[n], letters[min_idx] = letters[min_idx], letters[n]

dfs(0, '')