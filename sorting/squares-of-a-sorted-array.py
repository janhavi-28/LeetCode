class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        result = [0]*len(nums)
        index = len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left +=1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return result