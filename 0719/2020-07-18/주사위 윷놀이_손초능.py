import sys
input = sys.stdin.readline

def dfs(arr, score, turn):
    global board, game, cube, max_score
    if turn == 10:
        max_score = max(max_score, score)
        return
    ahead = cube[turn]-1
    if len(arr) < 4:
        if not visit[board[0][ahead]]:
            visit[board[0][ahead]] = 1
            dfs(arr+[board[0][ahead]], score+game[board[0][ahead]], turn+1)
            visit[board[0][ahead]] = 0
    for i in range(len(arr)):
        if arr[i] == 32: continue
        else:
            temp = arr[i]
            arr[i] = board[arr[i]][ahead]
            if not visit[arr[i]]:
                if arr[i] != 32:
                    visit[arr[i]] = 1
                visit[temp] = 0
                dfs(arr, score+game[arr[i]], turn+1)
                visit[temp] = 1
                visit[arr[i]] = 0
            arr[i] = temp

board = {
    0: [1, 2, 3, 4, 5],
    1: [2, 3, 4, 5, 6],
    2: [3, 4, 5, 6, 7],
    3: [4, 5, 6, 7, 8],
    4: [5, 6, 7, 8, 9],
    5: [21, 22, 23, 24, 30],
    6: [7, 8, 9, 10, 11],
    7: [8, 9, 10, 11, 12],
    8: [9, 10, 11, 12, 13],
    9: [10, 11, 12, 13, 14],
    10: [28, 29, 24, 30, 31],
    11: [12, 13, 14, 15, 16],
    12: [13, 14, 15, 16, 17],
    13: [14, 15, 16, 17, 18],
    14: [15, 16, 17, 18, 19],
    15: [27, 26, 25, 24, 30],
    16: [17, 18, 19, 20, 32],
    17: [18, 19, 20, 32, 32],
    18: [19, 20, 32, 32, 32],
    19: [20, 32, 32, 32, 32],
    20: [32, 32, 32, 32, 32],
    21: [22, 23, 24, 30, 31],
    22: [23, 24, 30, 31, 20],
    23: [24, 30, 31, 20, 32],
    24: [30, 31, 20, 32, 32],
    25: [24, 30, 31, 20, 32],
    26: [25, 24, 30, 31, 20],
    27: [26, 25, 24, 30, 31],
    28: [29, 24, 30, 31, 20],
    29: [24, 30, 31, 20, 32],
    30: [31, 20, 32, 32, 32],
    31: [20, 32, 32, 32, 32],
}

game = [
    0,
    2, 4, 6, 8, 10,
    12, 14, 16, 18, 20,
    22, 24, 26, 28, 30,
    32, 34, 36, 38, 40,
    13, 16, 19, 25, 26,
    27, 28, 22, 24, 30,
    35, 0,
]

cube = list(map(int, input().split()))
visit = [0] * 33

max_score = 0

dfs([], 0, 0)

print(max_score)