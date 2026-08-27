class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        low = 0
        total = 0
        res = float('inf')

        for high in range(n):

            # Include current element
            total += nums[high]

            # Shrink window while condition is satisfied
            while total >= target:

                length = high - low + 1

                res = min(res, length)

                # Remove left element
                total -= nums[low]
                low += 1

        if res == float('inf'):
            return 0

        return res