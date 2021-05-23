'''
we use basic comparison here
'''

def isSubsequence(self,s,t):
    pos_t,pos_s =0,0

    while pos_s<len(s) and pos_t<len(t):
        pos_s,pos_t = pos_s+(s[pos_s]==t[pos_t]), pos_t+1
    
    return len(s)==pos_s