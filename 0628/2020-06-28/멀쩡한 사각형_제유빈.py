import math
def solution(w, h):
    return w*h-(h+w-math.gcd(w, h))


# def solution(w,h):
#     ans = 0
#     for i in range(w):
#         minus = math.ceil(h-i*(h/w))-math.floor(h-(i+1)*(h/w))
#         ans += minus
#     return w*h-ans
#
# def solution(w,h):
#     ans = 0
#     s = h
#     for i in range(w):
#
#         minus = math.ceil(s)-math.floor(s-(h/w))
#         ans += minus
#         s -= h/w
#     return w*h-ans
print(solution(8, 12))  # 80
print(solution(1, 100))   # 0
print(solution(2, 100))   # 100
print(solution(1, 1))   # 0
print(solution(1000, 1000))  # 999000
print(solution(10000, 10000))   # 99990000
print(solution(10**5, 10**5))
print(solution(10**6, 99999))   # 99997900002
