def maxProdSubaaray(self,nums):
    res=pos=neg = 0
    for x in nums:
        if x>0: pos,neg = 1+pos,1+neg if neg else 0
        if x<0: pos,neg = 1+neg if neg else 0,1+pos
        else: pos=neg=0
        res = max(pos,res)


    return res