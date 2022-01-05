def out(trainers, v):
    for i in range(len(trainers)):
        q = 0 
        while q < len(trainers[i]):
            if(trainers[i][q] == v):
                trainers[i].pop(q)
            q += 1 
    trainers[v] = [-1]

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def loop(a,b):
    c = (a + b) / gcd(a,b)
    return bool(c & (c - 1))

def solution(banana_list):
    #Your code here
    n = len(banana_list)
    trainers = [[] for i in range(n)]
    watchers = 0
    
    for i in range(n):
        for j in range(i,n):
            if i != j and loop(banana_list[i], banana_list[j]):
                trainers[i].append(j)
                trainers[j].append(i)
    
    while n > 0:
        minimum = 0
        for i in range(len(trainers)):
            if(i != 0 and (len(trainers[i]) < len(trainers[minimum]) or trainers[minimum] == [-1]) and trainers[i] != [-1]):
                minimum=i

        if((len(trainers[minimum])) == 0 or (len(trainers[minimum]) == 1 and trainers[minimum][0] == trainers[minimum]) and trainers[minimum] != [-1]):
            out(trainers, minimum)
            n -= 1
            watchers += 1
        else:
            min_v = trainers[minimum][0]
            for i in range(len(trainers[minimum])):
                if(i != 0 and trainers[minimum][i] != minimum and len(trainers[trainers[minimum][i]]) < len(trainers[min_v])):
                    min_v = trainers[minimum][i]
            if(trainers[min_v] != [-1]):
                out(trainers, minimum)
                out(trainers, min_v)
                n -= 2
    return watchers