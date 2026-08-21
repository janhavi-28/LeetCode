class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        low = 0
        res = 0
        freq = {}
        for high in range(len(s)):
        #include current character
            freq[s[high]] = freq.get(s[high], 0) + 1
        #shirnk window if duplicate found
            while freq[s[high]] > 1:
                freq[s[low]] -= 1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1
            #Update maximum length
                res = max(res, high - low + 1)
        return res        