def solution(n, arr1, arr2):
    answer = [[] for _ in range(n)]
    grid = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            check1 = arr1[i] - 2**(n-j-1)
            check2 = arr2[i] - 2**(n-j-1)
            if check1 >= 0:
                arr1[i] -= 2 **(n-j-1)
                grid[i][j] = '#'
            else:
                grid[i][j] = ' '
            if check2 >= 0:
                arr2[i] -= 2 **(n-j-1)
                if grid[i][j] == ' ':
                    grid[i][j] = '#'
            else:
                if grid[i][j] == ' ':
                    grid[i][j] = ' '
    # print(grid)
    for i in range(n):
        answer[i].append(''.join(grid[i]))
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))