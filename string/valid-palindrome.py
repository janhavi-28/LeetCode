class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        left = 0
        right = len(clean) - 1

        while left < right:

            if clean[left] != clean[right]:
                return False

            left += 1
            right -= 1

        return True  