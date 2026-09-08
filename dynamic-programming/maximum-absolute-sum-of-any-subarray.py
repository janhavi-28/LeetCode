class Solution:
    def maxAbsoluteSum(self, nums):
        # Maximum subarray ending here
        max_ending = nums[0]

        # Minimum subarray ending here
        min_ending = nums[0]

        # Best maximum subarray sum
        max_sum = nums[0]

        # Best minimum subarray sum
        min_sum = nums[0]

        for i in range(1, len(nums)):
            # Maximum subarray
            max_ending = max(nums[i], max_ending + nums[i])
            max_sum = max(max_sum, max_ending)

            # Minimum subarray
            min_ending = min(nums[i], min_ending + nums[i])
            min_sum = min(min_sum, min_ending)

        return max(max_sum, abs(min_sum))