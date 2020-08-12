n = int(input())
if n == 1: print(9)
else:
    answer = [1] * 10
    answer[0] = 0
    for i in range(n-1):
        arr = [0] * 10
        for j in range(10):
            if j-1 >= 0: arr[j-1] = (arr[j-1] + answer[j]) % 1000000000
            if j+1 < 10: arr[j+1] = (arr[j+1] + answer[j]) % 1000000000
        answer = arr[:]
    print(sum(answer)%1000000000)