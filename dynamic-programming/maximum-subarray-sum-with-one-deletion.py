class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        no_delete = arr[0]
        one_delete = float('-inf')
        ans = arr[0]
        for i in range(1, n):
            prev_no_delete = no_delete
            prev_one_delete = one_delete
            no_delete = max(prev_no_delete + arr[i], arr[i])
            one_delete = max(prev_no_delete, prev_one_delete + arr[i])
            ans = max(ans, no_delete, one_delete)
        return ans 