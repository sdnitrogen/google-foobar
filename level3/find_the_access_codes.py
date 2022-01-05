def solution(l):
    # Your code here
    n = len(l)
    divisible = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if l[j] % l[i] == 0:
                divisible[i] += 1
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if l[j] % l[i] == 0:
                res += divisible[j]
    return res