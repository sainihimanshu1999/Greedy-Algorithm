'''
In this matrix we have to find maximum non negative path from top to bottom, we will do this by maintaining
two matrices one for maximum and one for minimum
'''

def nonnegvPath(self,grid):

    m,n = len(grid),len(grid[0])

    maxDp = [[0]*n for _ in range(m)]
    minDp = [[0]*n for _ in range(m)]

    maxDp[0][0] = minDp[0][0] = grid[0][0]

    for i in range(1,m):
        maxDp[i][0] = maxDp[i-1][0]*grid[i][0]
        minDp[i][0] = minDp[i-1][0]*grid[i][0]

    for j in range(1,n):
        minDp[0][j] = minDp[0][j-1]*grid[0][i]
        maxDp[0][j] = maxDp[0][j-1]*grid[0][i]


    for i in range(1,m):
        for j in range(1,n):
            if grid[i][j]>0:
                maxDp = max(maxDp[i-1][j],maxDp[i][j-1])*grid[i][j]
                minDp = min(minDp[i-1][j], minDp[i][j-1])*grid[i][j]

            else:
                maxDp = min(minDp[i-1][j], minDp[i][j-1])*grid[i][j]
                minDp = max(maxDp[i-1][j],maxDp[i][j-1])*grid[i][j]

    return maxDp[-1][-1] if maxDp[-1][-1]>=0 else -1
