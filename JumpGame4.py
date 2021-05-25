'''
In this question we are give two variable, maxJump and minJump, here we are given binary string
'''
import collections

def jumpGame(self,s,minJump,maxJump):

    q = collections.defaultdict([0])
    max_reach = 0

    while q:
        curr_i = q.popleft()
        if curr_i == len(s)-1:
            return True

        start = max(curr_i+minJump,max_reach)

        for i in range (start,min(curr_i+maxJump+1,len(s))):
            if s[i] == '0':
                q.append(i)
        
        max_reach = curr_i+maxJump
    return False
    