class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        arr = []
# conver 2d to 1d first
        for row in grid:
            arr.extend(row)
#rotate the list
        k %= len(arr)
        arr = arr[-k:] + arr[:-k]

#convert back to 2d array
        ans = []
        index = 0

        for i in range(m):
            row = []
            for j in range (n):
                row.append(arr[index])
                index += 1
            ans.append(row)
        return ans 