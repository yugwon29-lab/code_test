# 25501. 재귀의 귀재

T = int(input())

for t in range(1, T+1):
    in_str = input()
    cnt = 0

    def recursion(st, l, r):
        global cnt
        if l >= r:
            return 1
        elif st[l] != st[r]:
            return 0
        else:
            cnt += 1
            return recursion(st, l+1, r-1)
        
    def isPalindrome(st):
        global cnt
        cnt += 1
        return recursion(st, 0, len(st)-1)
    
    print(isPalindrome(in_str), cnt)