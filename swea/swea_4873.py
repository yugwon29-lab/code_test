T = int(input())

for i in range(1, T + 1):

    # 4873. 반복문자 지우기
    S = input()

    stack = []

    for c in S:
        if len(stack) == 0:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop(-1)
            else:
                stack.append(c)

    print(f"#{i} {len(stack)}")
