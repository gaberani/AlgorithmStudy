# Given a string containing only digits '0'-'9',
# write a function to determine if it's an additive number.
# A valid additive sequence should contain at least three numbers.

# Note: Numbers in the additive sequence cannot have leading zeros,
# so sequence 1, 2, 03 or 1, 02, 3 is invalid.

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

test = Solution()
print(test.isAdditiveNumber("112358"))
# true
print(test.isAdditiveNumber("199100199"))
# true