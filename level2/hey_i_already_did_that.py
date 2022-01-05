def to_base_b(num, b):
    n = int(num)
    digits = []
    while n >= b:
        digits.append(str(n%b))
        n = n//b
    digits.append(str(n))
    return ''.join(digits[::-1])

def to_base_10(num, b):
    digits = list(num[::-1])
    n = 0
    for i, d in enumerate(digits):
        n += int(d)*(b**i)
    return str(n)

def solution(n, b):
    #Your code here
    k = len(n)
    start = n
    minion_order = []
    while start not in minion_order:
        minion_order.append(start)
        x = ''.join(sorted(start)[::-1])
        y = ''.join(sorted(start))
        if b == 10:
            next_minion = int(x) - int(y)
            start = str(next_minion)
        else:
            next_minion = int(to_base_10(x,b)) - int(to_base_10(y,b))
            start = to_base_b(str(next_minion),b)
        start = '0'*(k-len(start))+start
    return len(minion_order)-minion_order.index(start)