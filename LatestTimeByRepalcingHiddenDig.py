'''
In this question we are given hidden digits ans we have to replace it with the latest time
'''
def latestTime(self,time):
    lst = list(time)
    for i,t in enumerate(lst):
        if t == '?':
            if i ==0:
                lst[i] = 2 if lst[i]<=3 or lst[1] =='?' else '1'
            if i == 1:
                lst[i] = 3 if lst[0] == '2' else '9'

            if i == 2:
                lst[i] = '5'

            if i== 3:
                lst[i] = '9'

    return ''.join(lst)