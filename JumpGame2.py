'''
In this question we have to reach the destination. we play by the index, we maintain a curr_coverage which
stores the maximum of curr coverage we can achieve and last index jump which maintain the index to which
we last jumped too
'''

def jumpGame2(self,nums):
    n = len(nums)
    destination =  n-1

    max_coverage = 0
    last_jump_index = 0
    jumps = 0

    for i in range(n):
        max_coverage = max(max_coverage, i+nums[i])

        if i == last_jump_index:
            last_jump_index = max_coverage
            jumps+=1
            if max_coverage>=destination:
                return jumps

    return jumps