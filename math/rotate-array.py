class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # Reverse the entire array
        nums.reverse()

        # Reverse first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse remaining elements
        nums[k:] = reversed(nums[k:])


        
        """n = len(nums)

        # If k is greater than array size
        k = k % n

        # Rotate one step, k times
        for _ in range(k):

            # Save the last element
            temp = nums[-1]

            # Shift all elements to the right
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]

            # Place the last element at the beginning
            nums[0] = temp"""