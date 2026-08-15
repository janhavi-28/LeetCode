class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in range (len(nums)):
            needed = target - nums[i]
            if needed in h:
                return [h[needed], i]
            h[nums[i]] = i

        