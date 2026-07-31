class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       # return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)