# 연습 문제 14
# 큐를 구현하여 다음 동작을 확인하기

# 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고
# 큐에서 세 개의 데이터를 차례로 꺼내서 출력한다.
# 1, 2, 3이 출력되어야 한다.

front = rear = -1
queue = [0] * 10

# enq(1)
rear += 1
queue[rear] = 1

# enq(2)
rear += 1
queue[rear] = 2

# enq(3)
rear += 1
queue[rear] = 3

# deq()
front += 1
print(queue[front])

# deq()
front += 1
print(queue[front])

# deq()
front += 1
print(queue[front])