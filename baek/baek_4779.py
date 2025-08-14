# 4779. 칸토어 집합
import sys

def draw_line(n):
    if n == 0:
        return '-'
    else:
        crit = 3 ** (n-1)
        return draw_line(n-1) + ' ' * crit + draw_line(n-1)
    
for line in sys.stdin:
    n = int(line)
    print(draw_line(n))
    