class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1

        max_water = 0

        while left < right:

            # Width between the two lines
            width = right - left

            # Height is the smaller of the two lines
            h = min(height[left], height[right])

            # Calculate water stored
            area = width * h

            # Update maximum water
            max_water = max(max_water, area)

            # Move the smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water