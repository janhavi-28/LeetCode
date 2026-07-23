class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        count0 = 0
        count1 = 0
        count2 = 0

        # Count the number of 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        index = 0

        # Fill 0s
        while count0 > 0:
            nums[index] = 0
            index += 1
            count0 -= 1

        # Fill 1s
        while count1 > 0:
            nums[index] = 1
            index += 1
            count1 -= 1

        # Fill 2s
        while count2 > 0:
            nums[index] = 2
            index += 1
            count2 -= 1

        print(nums)  