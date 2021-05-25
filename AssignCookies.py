'''
In this question we have to find the content children, they have green array and cookie size array
'''

def satisfaction(self,g,s):
    g.sort()
    s.sort()

    child_i,cookie_i =0,0

    while cookie_i<len(s) and child_i<len(g):
        if s[cookie_i]>=g[child_i]:
            child_i+=1

        cookie_i +=1

    return child_i