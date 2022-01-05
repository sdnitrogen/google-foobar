from itertools import combinations

def solution(num_buns, num_required):
    # Your code here
    dist = [[] for i in range(num_buns)]
    if num_required == 0:
        return dist
    elif num_required == 1:
        for i in range(num_buns):
            dist[i].append(0)
        return dist
    elif num_required == num_buns:
        for i in range(num_buns):
            dist[i].append(i)
        return dist
    else:
        total=len(list(combinations(range(num_buns),num_required))) * num_required
        keys = list(combinations(range(num_buns),num_buns - num_required + 1))
        for i in range(total / (num_buns - num_required + 1)):
            for j in keys[i]:
                dist[j].append(i)
    return dist