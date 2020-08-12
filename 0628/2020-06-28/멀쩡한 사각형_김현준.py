import math
def solution(w, h):
    # 해설 참조
    return w*h - (w+h-math.gcd(w, h))

w = 8
h = 12
# result = 80

print(solution(w, h))