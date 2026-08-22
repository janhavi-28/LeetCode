class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        low = 0
        res = 0
        freq = {}

        for high in range(len(fruits)):

            # Add current fruit
            freq[fruits[high]] = freq.get(fruits[high], 0) + 1

            # Shrink window if more than 2 distinct fruits
            while len(freq) > 2:
                freq[fruits[low]] -= 1

                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]

                low += 1

            # Window has at most 2 distinct fruits
            res = max(res, high - low + 1)

        return res