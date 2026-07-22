class Solution:
    def fib(self, N):
        # Base case
        if N <= 1:
            return N

        # Recursive calls
        last = self.fib(N - 1)     # (N-1)th term
        slast = self.fib(N - 2)    # (N-2)th term

        return last + slast

# Driver code
sol = Solution()
N = 4
print(sol.fib(N))
