# 1992. 쿼드트리

N = int(input())
monitor = [[int(x) for x in input()] for _ in range(N)]

def is_same(monitor):
    color = monitor[0][0]
    same = True
    length = len(monitor)
    for idx in range(length * length):
        if color != monitor[idx // length][idx % length]:
            same = False
            break
    return same

def quad_tree(monitor):
    if is_same(monitor):
        print(monitor[0][0], end='')
    else:
        length_div = len(monitor) // 2
        print('(', end='')
        quad_tree([[monitor[y][x] for x in range(0, length_div)] for y in range(0, length_div)])
        quad_tree([[monitor[y][x] for x in range(length_div, length_div*2)] for y in range(0, length_div)])
        quad_tree([[monitor[y][x] for x in range(0, length_div)] for y in range(length_div, length_div*2)])
        quad_tree([[monitor[y][x] for x in range(length_div, length_div*2)] for y in range(length_div, length_div*2)])
        print(')', end='')

quad_tree(monitor)