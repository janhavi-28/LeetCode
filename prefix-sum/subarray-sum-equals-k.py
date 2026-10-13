class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        result = 0
        freq = {}
        freq[0] = 1
        for i in range (len(nums)):
            sum += nums[i]
            ques = sum -k
            if ques in freq: 
                result += freq[ques]
            if sum in freq:
                freq[sum] += 1
            else: 
                freq[sum] = 1
        return result