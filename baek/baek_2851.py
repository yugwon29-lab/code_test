# 2851.슈퍼 마리오

mush = []
for _ in range(10):
    mush.append(int(input()))

score = 0
min_diff = 100
max_score = 0
for i in range(10):
    score += mush[i]
    if score > 100:
        if min_diff >= score - 100:
            max_score = score
            min_diff = score - 100
        break
    else:
        min_diff = 100 - score
        max_score = score
        
print(max_score)
