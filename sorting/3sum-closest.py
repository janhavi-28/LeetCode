class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Sort the array
        nums.sort()

        # Assume the first three numbers give the closest sum
        closest = nums[0] + nums[1] + nums[2]

        # Fix one element
        for i in range(len(nums) - 2):

            # Two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:

                # Calculate current sum
                current = nums[i] + nums[left] + nums[right]

                # Update closest sum if current is nearer to target
                if abs(target - current) < abs(target - closest):
                    closest = current

                # If exact target is found
                if current == target:
                    return current

                # Need a larger sum
                elif current < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return closest