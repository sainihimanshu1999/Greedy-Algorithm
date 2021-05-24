'''
we will solve this question using two sum
'''
def minimumOperations(self,nums,x):
    n = len(nums)
    dic = {}
    dic[0] = -1
    left = 0
    for i in range(n):
        left += nums[i]
        if left not in dic:
            dic[left] = i

    right = 0
    ans = n+1
    for i in range(n,-1,-1):
        if i>0: right += nums[i]
        left = x- right
        if left in dic:
            ans = min(ans,dic[left]+1+n-i)
    
    if ans == n+1: return -1
    return ans

    
