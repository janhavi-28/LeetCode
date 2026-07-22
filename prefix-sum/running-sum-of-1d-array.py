class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            ans.append(total)
        return ans 