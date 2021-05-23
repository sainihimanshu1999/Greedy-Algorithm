'''
in this question we take investor example, we sort the array by minimum - actual, an investor will either invest 
prev_investment + actual or minimum, whichever one is more
'''

def minimumEnergy(self,tasks):
    tasks.sort(key = lambda x:x[1]-x[0])

    res = 0
    for actual,minimum in tasks:
        res = max(res+actual,minimum)
    return res