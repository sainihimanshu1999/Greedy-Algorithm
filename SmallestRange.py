'''
in this question we have the choice to do x = -k or x = k and add it num, but we figure out that it means
x = 0 and x = 2k
'''

def smallestRange(self,nums,k):
    nums.sort()
    result = nums[-1]-nums[0]

    for i in range(len(nums)-1):
        max_num = max(A[-1],A[i]+2*k)
        min_num = min(A[i+1],A[0]+2*k)
        result  = min(result,max_num-min_num)

    return result