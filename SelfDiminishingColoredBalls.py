'''
In this question we have used arithmetic sum formula = (n+(n-d)+1)*d//2
'''

def coloredBalls(self,inventory,orders):
    inventory.sort(reverse = True)
    inventory +=[0]
    result = 0
    k = 1

    for i in range(len(inventory)-1):
        if inventory[i]>inventory[i+1]:
            if k*(inventory[i]-inventory[i+1])<orders:
                diffrence = inventory[i]-inventory[i+1]
                result = k*(inventory[i]+inventory[i+1]+1)*diffrence//2
                orders -= diffrence

            else:
                q,r = divmod(orders,k)
                result += k*(inventory[i]+(inventory[i]-q+1))*q//2
                result += r*(inventory[i]-q)
                return result%(10**9+7)

        k+=1
    