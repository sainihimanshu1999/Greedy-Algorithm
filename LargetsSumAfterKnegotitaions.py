'''
we have to flip a number k times in an array and the find a largest sum, flip: nums[i] = - nums[i],we can
flip same number more than once too
'''

def largestSum(self,nums,k):
    nums.sort()
    i = 0
    while i<len(nums) and i<k and nums[i]<0:
        nums[i] = - nums[i]
        i+=1

    return sum(nums) - (k-i)%2*min(nums)*2
