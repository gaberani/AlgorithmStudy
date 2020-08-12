import math
def solution(w, h):
    min_value, max_value = min(w, h), max(w, h)
    result = 0
    for i in range(1, min_value+1):
        result += math.ceil(max_value*i / min_value) - int(max_value*(i-1) / min_value)
        if max_value * i % min_value == 0: break
    return w*h - result*(min_value//i)

print(solution(3, 7))
