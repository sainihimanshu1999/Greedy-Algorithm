'''
In this question we have to give minimum swaps to make all the couples to sit togehter and hold hands
'''

def minSwap(self,row):
    dic = {x:i for i,x in enumerate(row)}
    swap = 0

    for i in range(len(row)):
        x = row[i]
        y = x+1 if x%2==0 else x-1
        j = dic[y]

        if abs(i-j)>1:
            row[i+1],row[j] = row[j],row[i+1]
            dic[row[i+1]] = i+1
            dic[row[j]] = j
            swap += 1
    return swap