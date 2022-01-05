from math import factorial
from collections import Counter

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def num_cycle(c, n):
    nc = factorial(n)
    for i, j in Counter(c).items():
        nc //= (i ** j) * factorial(j)
    return nc      

def part_cycle(n, i=1):
    yield [n]
    for i in range(i, n//2+1):
        for p in part_cycle(n-i, i):
            yield [i]+p

def solution(w, h, s):
    # Your code here
    mat = 0
    for cycle_w in part_cycle(w):
        for cycle_h in part_cycle(h):            
            n = num_cycle(cycle_w, w) * num_cycle(cycle_h, h)
            mat += n * (s ** sum([sum([gcd(i, j) for i in cycle_w]) for j in cycle_h]))
    return str(mat // (factorial(w) * factorial(h)))