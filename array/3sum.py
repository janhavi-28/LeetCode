class Solution(object):
    def threeSum(self, nums):

        # Step 1: Sort the array
        nums.sort()

        # Store the answer
        ans = []

        # Step 2: Fix one element at a time
        for i in range(len(nums)):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers
            left = i + 1
            right = len(nums) - 1

            # Search for remaining two numbers
            while left < right:

                # Calculate current sum
                total = nums[i] + nums[left] + nums[right]

                # Case 1: Triplet found
                if total == 0:

                    ans.append([nums[i], nums[left], nums[right]])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate values on left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values on right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Case 2: Sum is too small
                elif total < 0:
                    left += 1

                # Case 3: Sum is too large
                else:
                    right -= 1

        # Return all unique triplets
        return ans