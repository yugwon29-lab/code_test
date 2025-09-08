# 2810.컵홀더

N = int(input())
seat = [x for x in input()]

seat_cuphold = []

i = 0
while i < len(seat):
    if seat[i] == 'S':
        seat_cuphold.append('*')
        seat_cuphold.append('S')
        i += 1
    elif seat[i] == 'L':
        seat_cuphold.append('*')
        seat_cuphold.append('L')
        seat_cuphold.append('L')
        i += 2
seat_cuphold.append('*')

max_cup = 0
used = [False] * len(seat_cuphold)
for j in range(len(seat_cuphold)):
    if seat_cuphold[j] == 'S' or seat_cuphold[j] == 'L':
        if seat_cuphold[j-1] == '*':
            if not used[j-1]:
                max_cup += 1
                used[j-1] = True
                continue
        if seat_cuphold[j+1] == '*':
            if not used[j+1]:
                max_cup += 1
                used[j+1] = True
                continue
        
print(max_cup)