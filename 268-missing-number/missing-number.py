class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        missing = n

        for i in range(n):
            missing ^= i
            missing ^= nums[i]

        return missing