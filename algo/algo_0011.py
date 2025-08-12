# 연습 문제 12
# 괄호의 짝을 검사하는 프로그램을 작성하고, 이를 이용하여 주어진 괄호 문자열의 올바른 사용 여부를 검사하자.

T = int(input())

for t in range(1, T+1):
    side = input()

    # 스택 정의
    size = 100
    stack = [0] * size
    top = -1

    is_good = True
    for s in side:
        if s == '(':
            top += 1
            stack[top] = s
        elif s == ')':
            if stack[top] != '(' or top == -1:
                is_good = False
                break
            else:
                top -= 1
    
    if top != -1:
        is_good = False
    
    print(f'#{t} {1 if is_good else 0}')