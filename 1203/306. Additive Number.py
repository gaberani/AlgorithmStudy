# Given a string containing only digits '0'-'9',
# write a function to determine if it's an additive number.
# A valid additive sequence should contain at least three numbers.

# Note: Numbers in the additive sequence cannot have leading zeros,
# so sequence 1, 2, 03 or 1, 02, 3 is invalid.

# 1. 연결되는 3개의 숫자만 찾으면 끝
# 2. 0으로 시작하는건 안됨!
class Solution(object):
    def isAdditiveNumber2(self, num):
        """
        :type num: str
        :rtype: bool
        """
        Length = len(num)
        answer = False
        def dfs(l, r, cnt):
            global answer
            if cnt == 1:
                return True
            else:
                for i in range(r[1]+1, Length+1):
                    # 더한 숫자가 뒤랑 같을 경우에만 cnt + 1 해줌
                    if int(num[l[0]:l[1]]) + int(num[r[0]:r[1]]) == int(num[r[1]:i]):
                        return dfs(r, [r[1], i], cnt+1)
                    # 더한 숫자가 작은 경우
                    elif int(num[l[0]:l[1]]) + int(num[r[0]:r[1]]) < int(num[r[1]:i]):
                        return dfs([l[0], l[1]+1], [r[0]+1, r[1]+1], cnt) or dfs(l, [r[0], r[1]+1], cnt)
                    # 더한 숫자가 뒤보다 큼(더 비교할 필요가없음)
                    elif int(num[l[0]:l[1]]) + int(num[r[0]:r[1]]) > int(num[r[1]:i]):
                        continue
        if dfs([0, 1], [1, 2], 0):
            return True
        return False

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        Length = len(num)
        answer = False
        def dfs(l, r):
            for i in range(r+1, Length+1):
                if (len(num[0:l]) == 1 or num[0:l][0] != "0") and (len(num[l:r]) == 1 or num[l:r][0] != "0") and (len(num[r:i]) == 1 or num[r:i][0] != "0"):
                    # 더한 숫자가 뒤랑 같을 경우에만 cnt + 1 해줌
                    if int(num[0:l]) + int(num[l:r]) == int(num[r:i]):
                        if i == Length:
                            return True
                        else:
                            print(int(num[0:l]), int(num[l:r]), int(num[r:i]))
                            dfs(r, r+1)
                    # 더한 숫자가 작은 경우
                    elif int(num[0:l]) + int(num[l:r]) < int(num[r:i]):
                        return dfs(l+1, r+1) or dfs(l, r+1)
                    # 더한 숫자가 뒤보다 큼(더 비교할 필요가없음)
                    elif int(num[0:l]) + int(num[l:r]) > int(num[r:i]):
                        continue
        if dfs(1, 2):
            return True
        return False


test = Solution()
print(test.isAdditiveNumber("112358"))
# true
# print(test.isAdditiveNumber("199100199"))
# true
# print(test.isAdditiveNumber("101"))
# print(test.isAdditiveNumber("123"))
# print(test.isAdditiveNumber("1023"))
print(test.isAdditiveNumber("121224036"))