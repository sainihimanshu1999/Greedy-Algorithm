from typing import Counter


def minSwaps(self,s):
    s = list(s)
    count = Counter(s)
    mx = max(count['0'],count['1'])
    mn = min(count['0'],count['1'])
    if mx>mn+1: return -1

    res = [0]*2

    for i in range(0,len(s),2):
        res[0] += s[i] == '0'
        res[1] += s[i] == '1'

    if count['0'] == count['1']: return min(res)

    if count['0']>count['1']:
        return res[1]
    else:
        return res[0]
