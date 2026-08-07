class Solution:
    def sortedSquares(self, nums):

        # Left pointer starts from the beginning
        left = 0

        # Right pointer starts from the end
        right = len(nums) - 1

        # Create an array to store the final sorted squares
        result = [0] * len(nums)

        # Fill the result array from the last index
        index = len(nums) - 1

        # Continue until both pointers meet
        while left <= right:

            # Compare absolute values because
            # the largest square comes from the largest absolute value
            if abs(nums[left]) > abs(nums[right]):

                # Store the square of the left element
                result[index] = nums[left] * nums[left]

                # Move the left pointer forward
                left += 1

            else:

                # Store the square of the right element
                result[index] = nums[right] * nums[right]

                # Move the right pointer backward
                right -= 1

            # Move to the previous position in the result array
            index -= 1

        # Return the sorted squares array
        return result