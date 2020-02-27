
import math
import numpy as np
import pygame

import myCv2 as mycv2


class Sun():

    def __init__(self,world):

        self.world = world

        self.x = 100
        self.y = 100

        self.edgeColor = None

        self.circles = 15
        self.glowsize = (400,400)


    def draw(self):

        baseArr =  glow( self.glowsize )
        narr = np.zeros( self.glowsize )

        for r in range( 1, self.circles ):

            layerArr = np.copy(baseArr)
            circle = mycv2.makeCircle( self.x, self.y, r )

            circleBools = []
            for i in range(len(circle)):
                try:
                    circleBools.append( self.world.foreground.bool[ circle[i][0] , circle[i][1] ] )
                except IndexError:
                    pass

            layerArr = mycv2.cut( layerArr , circleBools )
            nlayerArr = mycv2.cutCircle( layerArr , r )
            layerArr = nlayerArr

            narr += layerArr


        narr *= 255
        narr[ narr > 255 ] = 255

        if self.edgeColor == None:
            self.edgeColor = narr[0,self.glowsize[0]//2]
            

        narr -= np.amax(narr[0,:])
        narr -= np.amax(narr[:,0])
        narr[narr<0] = 0

        surf = pygame.Surface( self.world.screen.get_size(), flags = pygame.SRCALPHA )

        surf.fill( (255,255,255) )
        surfarray = pygame.surfarray.pixels_alpha( surf )
        surfarray[:,:] = 0

        arrBlitMiddle( narr, surfarray, int(self.x), int(self.y) )

        del surfarray
        self.world.screen.blit( surf, (0,0) )

        


def arrBlitMiddle(source,dest,x,y):

    ssize = source.shape
    dsize = dest.shape

    x -= int( ssize[0]/2 )
    y -= int( ssize[1]/2 )

    sleft = 0
    stop  = 0
    srig = ssize[0]
    sbot = ssize[1]

    dleft = x
    dtop  = y
    drig = x + srig
    dbot = y + sbot

    if dleft < 0:
        sleft -= dleft
        dleft = 0

    if dtop < 0:
        stop -= dtop
        dtop = 0

    if drig > dsize[0]:
        srig -= drig - dsize[0]
        drig = dsize[0]

    if dbot > dsize[1]:
        sbot -= dbot - dsize[1]
        dbot = dsize[1]
    dest[ dleft:drig , dtop:dbot ] = source[ sleft:srig , stop:sbot ]



def quadruple( arr ):

    shape = arr.shape

    mx0 =       int( shape[0]/2 )
    my0 =       int( shape[1]/2 ) 
    mx1 = math.ceil( shape[0]/2 )
    my1 = math.ceil( shape[1]/2 )

    arr[ mx0: , :my1 ] = arr[ range(mx1-1,-1,-1) , :my1 ]
    arr[  :   , my0: ] = arr[  :   , range(my1-1,-1,-1) ]

    return arr

def glow( shape ):

    arr = np.zeros( shape )
    
    mx = math.ceil( shape[0]/2 )
    my = math.ceil( shape[1]/2 )

    for x in range( mx ):
        for y in range( my ):
            dx = x-mx
            dy = y-my
            if (dx,dy) == (0,0):
                arr[x,y] = 1
                continue
            dis = math.hypot(dx,dy)
            n = 3 / ( dis )**1.2 
            arr[x,y] = n

    arr -= arr[0,shape[0]-1]

    return quadruple( arr )


if __name__ == '__main__':
    import main
    main.main()
