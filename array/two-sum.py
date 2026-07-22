class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            y = target - nums[i]
            if y in h:
                return [h[y], i]
            h[nums[i]] = i   
       

    

        