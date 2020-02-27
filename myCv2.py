import math
import cv2
import numpy as np

def cut( arr , bools ):

    n = len(bools)
    if not n:
        return arr*0
    bools = list(bools)
    anglePerN = 2*math.pi / n
    
    staA , endA = 0,0

    sizex,sizey = arr.shape[:2]
    r = math.hypot(sizex,sizey) / 2
    r /= math.cos(math.pi/n)

    mx,my = sizex/2 , sizey/2
    sectorPoints = [ [mx,my] ]

    bools.append(1) 

    while bools:

        if bools.pop(0):

            if staA != endA:
                cutSector( arr, sectorPoints )
                
            endA += 1
            staA = endA
            sectorPoints = [ [mx,my] ]

        else:

            if staA == endA:
                sectorPoints.append( pointFromAngle( mx,my,r, staA*anglePerN) )
           
            endA += 1
            sectorPoints.append( pointFromAngle( mx,my,r, endA*anglePerN) )

    return arr


def pointFromAngle( mx,my,r, angle ):

    x = mx - r * math.sin( angle )
    y = my - r * math.cos( angle )

    return x,y


def cutSector( arr, points ):    

    points = np.array( points, dtype = np.int32 )
    cv2.fillPoly( arr, [points], (0) )

    return arr


def test():
        
    arr = np.ones( (23,23,3), dtype=int )
    cut( arr , [0,1,0,0,0,0,1,0] )


def cutCircle( arr, r ):

    sx,sy = arr.shape[:2]
    mx,my = int(sx/2),int(sy/2)

    r-=3
    if r<=0:
        r=1

    cv2.circle( arr, (mx,my) , r , (0), -1 ) #here officer

    return( arr )


def makeCircle( sx,sy , r ):

    tempArr = np.zeros( (2*r+1,2*r+1) )
    cv2.circle( tempArr , (r,r) , r, (1) )
    if r-1:
        cv2.circle( tempArr , (r,r) , r-1, (0) )

    pointslist = [ (x,y) for y in range(2*r+1) for x in range(2*r+1) if tempArr[x,y] ]

    #sort u idiot
    def angle( point , r ):
        dx,dy = point[0]-r , point[1]-r
        return math.atan2(dy,dx)

    pointslist.sort( key = lambda p: angle(p,r) )

    # make positions relative
    pointslist = [ (item[0]-r+sx , item[1]-r+sy) for item in pointslist ]


    return pointslist

    
def drawCircle(arr):

    cv2.circle( arr , (10,10) , 10 , (0) )


def test2():

    pygame.init()
    screen = pygame.display.set_mode()

    surf = pygame.Surface( (100,100) )

    red = pygame.surfarray.pixels_red()












    


    
