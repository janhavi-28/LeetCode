class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low = 0
        window_sum = 0
        max_sum = float('-inf')

        for high in range(len(nums)):
            #include current element
            window_sum += nums[high]
            #window size becomes k
            if high - low + 1 == k:
                #update ans 
                max_sum = max(max_sum, window_sum)
                #remove left element 
                window_sum -= nums[low]
                low += 1
        return max_sum/k    