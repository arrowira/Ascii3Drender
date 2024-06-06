bg = "."

ink = "X"
screen = None
import os
import math
import time
 


def matmul(a, b):
    res = []
    if len(a[0]) != len(b):
        print("invalid")
        return
    
    for rownum in range(len(a)):
        newrow = []
        for columnnum in range(len(b[0])):
            newitem = []
            for i in range(len(a[0])):
                newitem.append(a[rownum][i]*b[i][columnnum])

            newrow.append(sum(newitem))
        res.append(newrow)
    return res


def plot(coord):
    x = math.floor(coord[0][0])
    y = math.floor(coord[1][0])
    try:
        screen[-y-(math.floor(len(screen)/2)+1)][x+math.floor(len(screen)/2)] = ink
    except:
        pass


    


a = [[0,-1], [1,0]] #90degree rotation

b = [[3],[17]]
d = [[3],[7]]
e = [[13],[7]]
c = [[13],[17]]
center = [[0],[0]]

tendeg = [[0.984808, -0.173648], [0.173648, 0.984808]]
twodeg = [[0.999391, -0.0348995], [0.0348995, 0.999391]]

def rotate(starts,loops):
    global screen
    screen = []
    for i in range(60):
        z = []
        for j in range(60):
            z.append(bg)
        screen.append(z)
    if loops > 250:
        return
    
    newstarts = []
    for i in starts:
        #deplot(i)
        plot(matmul(twodeg,i))
        newstarts.append(matmul(twodeg,i))
    for i in range(len(starts)-1):
        
        for index in range(15):
            multa = index/15
            multb = 1-multa
            p1x = matmul(twodeg,starts[i])[0][0]
            p1y = matmul(twodeg,starts[i])[1][0]
            p2x = matmul(twodeg,starts[i+1])[0][0]
            p2y = matmul(twodeg,starts[i+1])[1][0]

            plot([[p1x*multb+p2x*multa],[p1y*multb+p2y*multa]])
    os.system('cls')
    
    
    for i in screen:
        print(" ".join(i))
    time.sleep(0.02)
    rotate(newstarts,loops+1)
rotate([b,center,c,center,e,center,d,center,b,c,e,d,b],0)





    
    
