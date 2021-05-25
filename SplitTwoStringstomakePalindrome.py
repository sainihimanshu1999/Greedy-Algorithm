'''
We have to split two string to make palindrom, when aprefix == bsuffix[::-1] (or vice versa) then only the both combine
can make palindrome
'''

def palindrome(self,a,b):
    result = []

    i,j=0,len(a)-1

    while i<j and a[i]==b[j]:
        i,j = i+1,j-1

    result.append(a[i:j+1])
    result.append(b[i:j+1])

    i,j=0,len(a)-1

    while i<j and b[i]==a[j]:
        i,j = i+1,j-1
    
    result.append(a[i:j+1])
    result.append(b[i:j+1])

    for s in result:
        if s == s[::-1]: return True
    return False
    
