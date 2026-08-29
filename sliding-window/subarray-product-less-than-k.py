class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0
        low = 0
        res = 0
        product = 1
        for high in range(len(nums)):
            product *= nums[high]    
            while product  >= k:
                product //= nums[low]
                low += 1
            res += high - low + 1
        return res    