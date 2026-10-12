class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        l = len(s)
        right = l-1

        while left<right:
            s[left] , s[right] = s[right] , s[left]
            left += 1
            right -=1


        print(s)