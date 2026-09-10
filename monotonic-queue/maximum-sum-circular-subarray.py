class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)

        # Maximum Kadane
        max_ending = nums[0]
        max_sum = nums[0]

        # Minimum Kadane
        min_ending = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            # Maximum subarray
            max_ending = max(nums[i], max_ending + nums[i])
            max_sum = max(max_sum, max_ending)

            # Minimum subarray
            min_ending = min(nums[i], min_ending + nums[i])
            min_sum = min(min_sum, min_ending)

        # If all elements are negative
        if max_sum < 0:
            return max_sum

        # Circular answer
        return max(max_sum, total - min_sum)