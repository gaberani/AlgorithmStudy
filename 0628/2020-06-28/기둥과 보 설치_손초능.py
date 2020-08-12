def solution(n, build_frame):
    arr, answer = [[[] for _ in range(n+1)] for _ in range(n+1)], []
    def find(type_, x, y):
        nonlocal arr
        if type_:
            if (0 in arr[y-1][x]) or (x+1<=n and 0 in arr[y-1][x+1]) or ((x-1>=0 and 1 in arr[y][x-1]) and (x+1<=n and 1 in arr[y][x+1])):
                return 1
        else:
            if y == 0 or (0 in arr[y-1][x]) or (1 in arr[y][x]) or (x-1>=0 and 1 in arr[y][x-1]):
                return 1
        return 0
    for x, y, type_, command_ in build_frame:
        if command_ and find(type_, x, y): arr[y][x].append(type_)
        elif command_ == 0:
            if type_ in arr[y][x]: arr[y][x].pop(arr[y][x].index(type_))
            else: continue
            if type_:
                if x-1>=0 and 1 in arr[y][x-1] and not(find(1, x-1, y)): arr[y][x].append(1); continue
                if x+1<=n and 1 in arr[y][x+1] and not(find(1, x+1, y)): arr[y][x].append(1); continue
                if 0 in arr[y][x] and not(find(0, x, y)): arr[y][x].append(1); continue
                if x+1<=n and 0 in arr[y][x+1] and not(find(0, x+1, y)): arr[y][x].append(1); continue
            elif y+1<=n:
                if 0 in arr[y+1][x] and not(find(0, x, y+1)): arr[y][x].append(0); continue
                if 1 in arr[y+1][x] and not(find(1, x, y+1)): arr[y][x].append(0); continue
                if x-1>=0 and 1 in arr[y+1][x-1] and not(find(1, x-1, y+1)): arr[y][x].append(0); continue
        for i in range(n, -1, -1): print(arr[i])
        print()
    for x in range(n+1):
        for y in range(n+1):
            if arr[y][x]:
                arr[y][x].sort()
                while arr[y][x]:
                    answer.append([x, y, arr[y][x].pop(0)])
    return answer

# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))