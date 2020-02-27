
import pygame
import math
import random
import numpy as np
import colourise



class Sky():

    def __init__(self,world):

        self.sunb = 200
        self.skyb = 2000
        self.reverseh = 20
        self.sunOverlayR = 20
        self.res = 5
        self.startCol = [76,20,56]#[ 323,74,30,100 ]
        self.endCol   = [255,255,50]#[ 60,48,100,100 ]
        self.colReverse = True

        #self.bSunR = 50
        #self.behindSun = 255*np.fromfunction( lambda x,y: qurve(np.hypot(x-self.bSunR,y-self.bSunR),1), (self.bSunR*2,self.bSunR*2) )

        self.world = world

    def create(self):

        def sunFun(x,y):
            return qurve( np.hypot(sunx-x,suny-y)/2 ,self.sunb)*(10/self.res)**2

        def skyFun(x,y):
            #downness = sizey - y - reverseh
            downness = qurve( (arry-self.reverseh-suny)/30, 1) *3
            return qurve(arry-y-self.reverseh,self.skyb/self.res) * downness 

        sizex, sizey = self.world.size
        sunx,  suny  = self.world.sun.x/self.res, self.world.sun.y/self.res

        arrx,arry = sizex//self.res,sizey//self.res

        self.surf = pygame.Surface( (sizex,sizey) )
        arr = np.zeros( (arrx,arry) )

        arr += np.fromfunction( lambda x,y: sunFun(x,y), (arrx,arry) )
        arr += np.fromfunction( lambda x,y: skyFun(x,y), (arrx,arry) )

        arr = curve(arr,2)
        #arr *= 255

        arr = colourise.gradient( arr, self.startCol,self.endCol,swap=True)

        

        surfarray = pygame.surfarray.pixels3d( self.surf )

        arr = np.repeat( np.repeat(arr,self.res,axis=0), self.res, axis=1) 
        
        arrx,arry = arr.shape[:2]
        '''
        surfarray[:arrx,:arry,0] = arr
        surfarray[:arrx,:arry,1] = arr
        surfarray[:arrx,:arry,2] = arr'''

        surfarray[:arrx,:arry,:] = arr

        del surfarray

    def draw(self):

        self.world.screen.blit( self.surf, (0,0) )
        pygame.draw.circle(self.world.screen, [255,255,255], (self.world.sun.x,self.world.sun.y), self.sunOverlayR ) 




def colInHsva(start,end,n):

    col = [ lerp(start[i],end[i],n) for i in range(4) ]
    col[0] = col[0]%360

    colObj = pygame.Color(0,0,0)
    colObj.hsva = col

    return colObj

def arrToHsv( arr, start, end ):
    
    arrx,arry = shape.arr
    narr = np.zeros( (arrx,arry,3), dtype=int8)
    #start, end = np.array(start), np.array(end)
    narr[:,:,0] = lerp(start[0],end[0],arr)
    narr[:,:,1] = lerp(start[1],end[1],arr)
    narr[:,:,2] = lerp(start[2],end[2],arr)
    
    
    



def lerp( a,b,n ):
    return a + (b-a)*n

def qurve( n , k ):
    return k/(n**2+k)
    

def curve( n , k ):

    return n/(n+k)

if __name__ == '__main__':
    import main
    main.main()
