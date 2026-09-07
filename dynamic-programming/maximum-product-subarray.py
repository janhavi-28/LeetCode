class Solution:
    def maxProduct(self, nums):
        # Maximum product ending at current index
        max_ending = nums[0]

        # Minimum product ending at current index
        min_ending = nums[0]

        # Final answer
        ans = nums[0]

        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = max_ending * nums[i]
            v3 = min_ending * nums[i]

            # Update max and min products ending here
            max_ending = max(v1, v2, v3)
            min_ending = min(v1, v2, v3)

            # Update overall maximum product
            ans = max(ans, max_ending)

        return ans