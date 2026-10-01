class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum =  nums[left] + nums[right]
            if current_sum == target:
                return (left + 1, right + 1)
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []