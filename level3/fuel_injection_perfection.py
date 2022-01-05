def solution(n):
    # Your code here
    n = int(n)
    step = 0
    while n > 1:
        if n%2 != 0:
            if (n&3) == 1 or n == 3:
                n -= 1
            else:
                n += 1
        else:
            n /= 2
        step += 1
    return step