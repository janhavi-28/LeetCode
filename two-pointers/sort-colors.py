class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        lo, cur, hi = 0, 0, len(nums) - 1
        while cur <= hi:
            if nums[cur] == 0:
                nums[lo], nums[cur] = nums[cur], nums[lo]
                lo += 1
                cur += 1
            elif nums[cur] == 2:
                nums[hi], nums[cur] = nums[cur], nums[hi]

                hi -= 1
            else: 
                cur += 1