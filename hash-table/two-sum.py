class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        # Step 1: Store every number with its index
        for i, num in enumerate(nums):
            h[num] = i

        # Step 2: Find the required number
        for i, num in enumerate(nums):

            desired = target - num

            if desired in h and h[desired] != i:
                return [i, h[desired]]
                break