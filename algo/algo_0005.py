# 연습 문제 6
# 두 개의 문자열 s1과 s2, s1의 각 글자가 s2에 모두 존재하는가?

s1 = list(input())
s2 = list(input())

all_ok = True
for s in s1:
    if s not in s2:
        all_ok = False
        break

print(all_ok)