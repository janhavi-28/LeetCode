class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h = {}

        for num in nums:

            if num in h:
                return True

            h[num] = 1

        return False
                