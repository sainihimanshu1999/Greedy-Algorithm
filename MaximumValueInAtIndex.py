'''
In this question we have to find A[index] of the array of length n and having sum == maxSum. A[index] 
if the maximize of the index, and the array nums in array is 0<=num<n. 
'''
def max_val(self,n,index,maxSum):

    def check(x):
        b = max(x-index,0)
        res = (x+b)*(x-b+1)/2
        b = max(x-((n-1)-index),0)
        res += (x+b)*(x-b+1)/2
        return res-x


    maxSum -= n
    left,right = 0,maxSum
    while left<right:
        mid = (left+right+1)/2
        if check(mid) <= maxSum:
            left = mid
        else:
            right = mid-1
    return left+1
