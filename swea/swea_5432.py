T = int(input())

for test_case in range(1, T + 1):

    # 5432. 쇠막대기 자르기
    laser_stick = input()

    # 열린 괄호, 닫힌 괄호 확인
    stack = []
    cnt = 0
    num = 0
    for c in laser_stick:
        if stack:
            if stack[-1][0] == '(' and c == ')':
                prev = stack.pop(-1)
                # 레이저
                if num - prev[1] == 1:
                    cnt += len(stack)
                else:   # 쇠막대
                    cnt += 1
                
            else:
                stack.append([c, num])
        else:
            stack.append([c, num])
        num += 1


    print(f'#{test_case} {cnt}')
