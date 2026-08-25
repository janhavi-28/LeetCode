class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        left = 0
        max_freq = 0
        result = 0

        count = {}

        for right in range(len(s)):

            # Add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Maximum frequency in the current window
            max_freq = max(max_freq, count[s[right]])

            # Shrink the window if more than k replacements are needed
            while (right - left + 1) - max_freq > k:

                count[s[left]] -= 1
                left += 1

            # Update the maximum length
            result = max(result, right - left + 1)

        return result