class Solution:
    def moveZeroes(self, nums):
        writePos = 0
        for readPos in range(len(nums)):
            if nums[readPos] != 0:
                nums[writePos], nums[readPos] = nums[readPos], nums[writePos]
                writePos += 1    
       