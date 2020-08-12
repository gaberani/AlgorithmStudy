def solution(n, t, m, p):
    answer = ''
    num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    num = ''
    total_num = '0'
    decimal = 0
    for _ in range(t*m):
        tmp = decimal
        while decimal:
            num += num_lst[decimal % n]
            decimal //= n
        total_num += num[::-1]
        num = ''
        decimal = tmp + 1
        print(total_num)
    for rs in range(t):
        answer += total_num[rs*m+p-1]
    return answer

# print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 2))