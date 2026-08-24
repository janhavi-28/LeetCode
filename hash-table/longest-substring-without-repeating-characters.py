class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        low = 0          # Left pointer
        res = 0          # Maximum length
        freq = {}        # Store frequency of characters

        # Move right pointer
        for high in range(len(s)):

            # Include current character
            freq[s[high]] = freq.get(s[high], 0) + 1

            # If duplicate exists, shrink window
            while freq[s[high]] > 1:
                freq[s[low]] -= 1

                if freq[s[low]] == 0:
                    del freq[s[low]]

                low += 1

            # Update answer
            res = max(res, high - low + 1)

        return res