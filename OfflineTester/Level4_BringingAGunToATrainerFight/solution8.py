'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/fox0088/Bringing-a-gun-to-a-guard-fight/blob/master/GuardFight.py"


from math import hypot,atan2

def solution(dimensions, your_position, guard_position, distance):
    ypx=your_position[0]
    ypy=your_position[1]
    yp_list=[]
    gp_list=[]
    targetCnt=0
    angle_n_dist=dict()
    yp_list=matrix(dimensions, your_position, distance)
    gp_list=matrix(dimensions, guard_position, distance)

    for i in range(len(yp_list)):
        x=yp_list[i][0]-ypx
        y=yp_list[i][1]-ypy
        hyp=hypot(x,y)
        if hyp<=distance:
            atan=atan2(x,y)
            if atan not in angle_n_dist: angle_n_dist[atan]=hyp
        x=gp_list[i][0]-ypx
        y=gp_list[i][1]-ypy
        hyp=hypot(x,y)
        if hyp<=distance:
            atan=atan2(x,y)
            if atan not in angle_n_dist or hyp<=angle_n_dist[atan]:
                targetCnt+=1
                angle_n_dist[atan]=hyp
    return targetCnt

def matrix(room_size, position, distance):
    X,Y=position[0],position[1]
    arr,arrx,arry=[],[X],[Y]
    matX=distance//room_size[0]+2
    matY=distance//room_size[1]+2
    for i in range(1,matX):
        x2wall=room_size[0]*i-X
        x=X+2*x2wall
        arrx.append(x)
        X=x
    for i in range(1,matY):
        y2wall=room_size[1]*i-Y
        y=Y+2*y2wall
        arry.append(y)
        Y=y
    for i in arrx:
        for j in arry:
            arr+=[(i,-j)]+[(-i,j)]+[(-i,-j)]+[(i,j)]
    return arr
