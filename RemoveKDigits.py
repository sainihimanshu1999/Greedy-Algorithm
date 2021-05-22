'''
we have to remove k digits from the number to make the smalles number
'''

def removingKdig(self,number,k):
    stack = []
    for digit in number:
        if k>0 and len(stack)>0 and stack[-1]>digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    if k>0:
        stack = stack[:-k]
    return ''.join(stack).lstrip('0') or '0'
        