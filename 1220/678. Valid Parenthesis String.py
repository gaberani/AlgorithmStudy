# Given a string containing only three types of characters:
# '(', ')' and '*', write a function to check whether this string is valid.
# We define the validity of a string by these rules:
#
# 1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# 2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
# 3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# 4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# 5. An empty string is also valid.

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0 or s == '*': return True
        if len(s) == 1: return False

        # 왼쪽 기준으로 잡고 세기
        Left = 0
        for i in s:
            if i == ')':
                Left -= 1
            else:
                Left += 1

            if Left < 0: return False

        if Left == 0: return True

        Right = 0
        for i in s[::-1]:
            if i == '(':
                Right -= 1
            else:
                Right += 1
            if Right < 0: return False


        return True

test = Solution()
print(test.checkValidString('()'))