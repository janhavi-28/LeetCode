class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in h:
                return [h[needed], i]

            h[nums[i]] = i