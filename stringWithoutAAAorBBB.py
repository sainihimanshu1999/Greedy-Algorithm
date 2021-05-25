'''
we have give quatity of a and b in string we have to print them without making aaa and bbb come together
'''
def stringWithout(self,a,b):
    if b == 0:
        return 'a'*a
    elif a ==0:
        return 'b'*b

    elif a==b:
        return 'ab'*a
    
    elif a>b:
        return 'aab'+self.stringWithout(a-2,b-1)
    else:
        return self.stringWithout(a-1,b-2)  + 'abb'