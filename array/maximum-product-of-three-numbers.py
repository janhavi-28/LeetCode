class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = float('-inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):  
                    product = nums[i] * nums[j] * nums[k]
                    maximum = max(maximum, product)
        return maximum
        