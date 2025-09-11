# 16637. 괄호 추가하기
N = int(input())
foluma = list(input())

max_value = None
def calculate(idx, result):
    global max_value
    if idx == N:
        if max_value is None or max_value < result:
            max_value = result
        return

    # 괄호를 쓰지 않고 계산
    if foluma[idx] == "+":
        number = int(foluma[idx+1])
        calculate(idx+2, result+number)
    elif foluma[idx] == "-":
        number = int(foluma[idx+1])
        calculate(idx+2, result-number)
    elif foluma[idx] == "*":
        number = int(foluma[idx+1])
        calculate(idx+2, result*number)

    # 괄호를 써서 계산
    if idx + 4 <= N:
        a, b = int(foluma[idx+1]), int(foluma[idx+3])
        # 괄호 계산
        if foluma[idx+2] == "+":
            number = a + b
        elif foluma[idx+2] == "-":
            number = a - b
        elif foluma[idx+2] == "*":
            number = a * b

        # 그 후 계산
        if foluma[idx] == "+":
            calculate(idx+4, result+number)
        elif foluma[idx] == "-":
            calculate(idx+4, result-number)
        elif foluma[idx] == "*":
            calculate(idx+4, result*number)

calculate(1, int(foluma[0]))
print(max_value)