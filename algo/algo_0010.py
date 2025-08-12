# 연습 문제 11
# 스택을 구현한 후, 이를 이용해 3개의 데이터를 저장하고 다시 3번 꺼내어 출력해보자.

# 크기가 정해진 스택을 정의한다.
size = 10
stack = [0] * size
top = -1

# A push
top += 1
stack[top] = 'A'

# B push
top += 1
stack[top] = 'B'

# C push
top += 1
stack[top] = 'C'

# C pop
top -= 1
print(stack[top+1])

# B pop
top -= 1
print(stack[top+1])

# A pop
top -= 1
print(stack[top+1])