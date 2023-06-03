'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/Li-MingQing/Bringing-a-gun-to-a-trainer-fight/blob/main/solution.py"


import math

def solution(dimensions, your_position, trainer_position, distance):
    # Your code here
    if getDistance(your_position, trainer_position) > distance:
        return 0
    res = {getRootBearing(your_position, trainer_position): getDistance(your_position, trainer_position)}
    maxRoom = findMaxRoom(dimensions, distance, your_position)
    set = {}
    # check if the position in the same direction as your_position mirroring
    for num in range(maxRoom):
        for position in getPosition(dimensions, your_position, num):
            if checkPoint(your_position, position, dimensions) and getDistance(your_position, position) < distance and getRootBearing(your_position, position) not in set:
                set[getRootBearing(your_position, position)] = getDistance(your_position, position)
            else:
                continue
    #check every position of mirroring
    for num in range(maxRoom):
        for position in getPosition(dimensions, trainer_position, num):
            if checkPoint(your_position, position, dimensions) and getRootBearing(your_position, position) not in res and getDistance(your_position, position) <= distance and getRootBearing(your_position, position) not in set:
                res[getRootBearing(your_position, position)] = getDistance(your_position, position)
            elif getRootBearing(your_position, position) in set:
                if set[getRootBearing(your_position, position)] > getDistance(your_position, position):
                    res[getRootBearing(your_position, position)] = getDistance(your_position, position)
                else:
                    continue
            else:
                continue
    return len(res)

def checkPoint(your_position, position, dimension):  # check not hitting corner or vertically horizonally hitting
    x, y = dimension
    a1, b1 = position
    leftUp = getRootBearing(your_position, [0, y])
    rightDown = getRootBearing(your_position, [x, 0])
    leftDown = getRootBearing(your_position, [0, 0])
    rightUp = getRootBearing(your_position, [x, y])
    if position[0] != your_position[0] and position[1] != your_position[1]:
        if a1 < 0 and b1 > 0 and getRootBearing(your_position, position) != leftUp:
            return True
        elif a1 > 0 and b1 > 0 and getRootBearing(your_position, position) != rightUp:
            return True
        elif a1 < 0 and b1 < 0 and getRootBearing(your_position, position) != leftDown:
            return True
        elif a1 > 0 and b1 < 0 and getRootBearing(your_position, position) != rightDown:
            return True
        else:
            return False
    else:
        return False

def getDistance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

def getRootBearing(start, end):
    #get the direction
    return math.atan2(end[1] - start[1], end[0] - start[0])

def findMaxRoom(dimension, distance, your_position):
    a, b = your_position
    x, y = dimension
    roomsAboveX = (distance + b) // y + 1
    roomsRightY = (distance + a) // x + 1
    return max(roomsRightY, roomsAboveX)

def getPosition(dimension, trainer_position, n):
    res = []
    a, b = trainer_position
    x, y = dimension
    if n % 2 == 0:
        res.extend([(-a - n * x, (n + 2) * y - b), ((n + 2) * x - a, (n + 2) * y - b), (-a - n * x, -b - n * y), ((n + 2) * x - a, -b - n * y), ((-a - n * x), b), (a, (n + 2) * y - b), ((n + 2) * x - a, b), (a, -b - n * y)])
    else:
        res.extend(
            [(a - (n + 1) * x, (n + 1) * y + b), ((n + 1) * x + a, (n + 1) * y + b), (a - (n + 1) * x, b - (n + 1) * y), ((n + 1) * x + a, b - (n + 1) * y), (a - (n + 1) * x, b), (a, (n + 1) * y + b), ((n + 1) * x + a, b), (a, b - (n + 1) * y)])
    while n > 0:
        if n % 2 == 1:
            res.extend(
                [(-a - (n - 1) * x, res[0][1]), (res[0][0], (n + 1) * y - b), ((n + 1) * x - a, res[1][1]), (res[1][0], (n + 1) * y - b), (res[2][0], -b - (n - 1) * y), (-a - (n - 1) * x, res[2][1]), ((n + 1) * x - a, res[3][1]), (res[3][0], -b - (n - 1) * y)])
                 # 0.right                      # 0.down                      # 1.left                      # 1.down                      # 2.up                        # 2.right                       # 3.left                      # 3.up
        if n % 2 == 0:
            res.extend([(a - n * x, res[0][1]), (res[0][0], n * y + b), (n * x + a, res[1][1]), (res[1][0], n * y + b), (res[2][0], b - n * y), (a - n * x, res[2][1]), (n * x + a, res[3][1]), (res[3][0], b - n * y)])
                        # 0.right                # 0.down                # 1.left                # 1.down               # 2.up                  # 2.right                 # 3.left                 # 3.up
        n -= 1
    return res
