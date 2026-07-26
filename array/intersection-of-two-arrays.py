class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """ans = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if nums1[i] not in ans:
                        ans.append(nums1[i])

        return ans"""

        set1 = set(nums1)
        ans = []

        for num in set(nums2):
            if num in set1:
                ans.append(num)

        return ans