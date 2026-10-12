class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = set()

        for num in nums:
            if num in arr:
                return num
            arr.add(num)