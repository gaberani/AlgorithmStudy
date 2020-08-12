n = int(input())
arr = [0]*n
for i in range(n):
    value = int(input())
    if i == 0: max_value = value
    elif i == 1: max_value = arr[0]+value
    elif i == 2: max_value = max(arr[i-2]+value, b_value+value, arr[i-1])
    else:
        max_value = max(arr[i-3]+b_value+value, arr[i-2]+value, arr[i-1])
    arr[i] = max_value
    b_value = value
print(max_value)