#First Type of solution
def canJump(self,nums):
    goal = len(nums) - 1
    coverage = 0
    last_index = 0

    for i in range(len(nums)):
        coverage = max(coverage,i+nums[i])

        if i == last_index:
            last_index = coverage
            if coverage>=goal:
                return True

    return False


#Second Solution

def canJumpx(self,nums):
    destination = len(nums)-1
    curr = 0
    steps = nums[curr]

    while curr<destination  and steps>0:
        curr += 1

        steps = max(steps-1,nums[curr])

    return curr == destination