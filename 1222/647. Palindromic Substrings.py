class Solution(object):
    # 832 ms
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)
        if L == 1: return s

        answer = []
        for i in range(L):
            l, r = i, i
            while r < L:
                r += 1
                if l < r:
                    if s[l:r] == s[l:r][::-1]:
                        answer.append(s[l:r])
        return answer

    #


# a = '123456'
# print(a[::-1])

# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

test = Solution()
print(test.countSubstrings("abc"))
print(test.countSubstrings("aaa"))