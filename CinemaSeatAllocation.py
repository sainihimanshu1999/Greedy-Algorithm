'''
Every row can have at max 2 adjacent 4 seats 
'''
import collections

def cinema(self,n,reservedSeats):
    seats = collections.defaultdict(set)

    for i,j in reservedSeats:
        if j in [2,3,4,5]:
            seats[i].add(0)
        if j in [4,5,6,7]:
            seats[i].add(1)

        if j in [6,7,8,9]:
            seats[i].add(2)

    
    total = 2*n
    for i in seats:
        if len(seats[i])==3:
            total -=2
        else: 
            total -=1

    return total