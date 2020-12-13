# Given an array of strings arr.
# String s is a concatenation of a sub-sequence of arr which have unique characters.
# Return the maximum possible length of s.

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.
class Solution(object):
    def maxLength2(self, arr):

        if len(arr) == 1:
            return len(arr[0])

        answer = 0
        L = len(arr)
        for i in range(L-1):
            for j in range(i+1, L):
                one_case = len(arr[i]+arr[j])
                if one_case > answer and len(set(arr[i]+arr[j])) == one_case:
                    print(arr[i]+arr[j])
                    answer = one_case

        return answer

    def maxLength(self, arr):

        uniqELements = ['']
        answer = 0
        for i in range(len(arr)):
            sz = len(uniqELements)
            print(sz)
            for j in range(sz):
                x = arr[i] + uniqELements[j]
                # print(x)
                if (len(x) == len(set(x))):
                    uniqELements.append(x)
                    print(uniqELements)
                    answer = max(answer, len(x))
        print(uniqELements)
        return answer

test = Solution()
print(test.maxLength(["un","iq","ue"])) # 4
print(test.maxLength(["cha","r","act","ers"])) # 6
print(test.maxLength(["abcdefghijklmnopqrstuvwxyz"])) # 26