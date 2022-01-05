def solution(x):
    # Your code here
    n = len(x)
    decrypted = list(x)
    for i in range(n):
        if 'a' <= x[i] <= 'z':
            decrypted[i] = chr(ord('a')+25-ord(x[i])+ord('a'))
    return ''.join(decrypted)  