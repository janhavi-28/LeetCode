class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        
        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)
