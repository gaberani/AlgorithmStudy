def solution(n):
    shape = ''
    '''
    n=1       0
    n=2   0   0   1
    n=3 0 0 1 0 0 1 1
    '''
    for _ in range(n):
        tmp = '0'
        for i in range(len(shape)):
            if i%2:
                tmp += shape[i]+'0'
            else:
                tmp += shape[i]+'1'
        shape = tmp
    return list(map(int, list(shape)))

n = 3

print(solution(n))