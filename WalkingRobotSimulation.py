'''
when robot moves right, x becomes y and y becomes -x, when robot moves left, x becomes -y and y becomes x
'''

def robotSim(commands,obstacles):
    obstacles = {(x,y) for x,y in obstacles}
    x,y = 0,0
    dx,dy = 0,1
    distance = 0
    for move in commands:
        if move == -2:
            dx,dy = -dy,dx

        elif move ==-1:
            dx,dy = -dy,dx

        else:
            for i in range(move):
                if (x+dx,y+dy) in obstacles:
                    break
                x,y = x+dx,y+x

            distance = max(distance,x*x+y*y)

    return distance