'''
In this questin we have used sliding window approach
'''

def mostFrequent(self,nums,k    ):
    nums.sort()
    i = 0

    for j in range(len(nums)):
        k += nums[j]
        if k<nums[j]*(j-i+1):
            k-=nums[i]
            i+=1
    return j-i+1