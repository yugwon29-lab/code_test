T = int(input())

for i in range(1, T + 1):

    # 4874. Forth
    S = input().split()

    stack = []

    for s in S:
        if s in ['+', '-', '*', '/']:
            if len(stack) < 2:
                print(f"#{i} error")
                break
            b = stack.pop(-1)
            a = stack.pop(-1)
            # 숫자인지 확인
            if a in ['+', '-', '*', '/', '.'] or b in ['+', '-', '*', '/', '.']:
                print(f"#{i} error")
                break
            else:
                if s == '+':
                    stack.append(int(a)+int(b))
                elif s == '-':
                    stack.append(int(a)-int(b))
                elif s == '*':
                    stack.append(int(a)*int(b))
                else:
                    stack.append(int(a)//int(b))
        elif s == '.':
            r = stack.pop(-1)
            if r in ['+', '-', '*', '/', '.'] or len(stack) != 0:
                print(f"#{i} error")
                break
            else:
                print(f"#{i} {r}")
                break
        else:
            stack.append(int(s))
