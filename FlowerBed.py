'''
In this question we have to find wheter we can place flower in this flower bed or not. Greedily we have
to plant flowers in every available spot and just count them
'''

def flowerBed(self,flowerbed,N):
    flower_count = 0
    flowerBed = [0]+flowerbed+[0]
    for i in range(1,len(flowerBed)-1):
        if flowerBed[i] == 1:
            continue
        
        if not flowerBed[i-1]+flowerBed[i+1]:
            flowerBed[i] = 1
            flower_count +=1
    return flower_count>=N