def solution(x, y):
    # Your code here
    m = int(x)
    f = int(y)
    cycle = 0
    max_mf = max(m,f)
    min_mf = min(m,f)
    while min_mf > 0:
        cycle += max_mf//min_mf
        max_mf, min_mf = min_mf, max_mf%min_mf
    if max_mf != 1:
        return "impossible"
    return str(cycle-1)