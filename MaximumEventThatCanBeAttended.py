'''
In this question we will use a priority queue and greedily select the days we can attend the meeting
'''
import heapq

def maxEvents(self,events):
    events =sorted(events, key = lambda x:x[0])
    priorityq = []
    i,n = 0,len(events)
    count,day = 0,0

    while i<n:
        if not priorityq:
            day = events[i][0]

        while i<n and day>=events[i][0]:
            heapq.heappush(priorityq,events[i][1])
            i+=1

        heapq.heappop(priorityq)
        count +=1
        day +=1

        if priorityq and priorityq[0]>day:
            heapq.heappop(priorityq)

    return count