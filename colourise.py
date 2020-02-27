import numpy as np


def rgbToHsv( col ):
    r,g,b = col[0]/255,col[1]/255,col[2]/255
    mn = min(r,g,b)
    mx = max(r,g,b)
    df = mx-mn
    if mn==mx:
        h = 0
    elif mx==r:
        h = (60* ((g-b)/df) )%360
    elif mx==g:
        h = (60* ((g-b)/df) +120 )%360
    elif mx==b:
        h = (60* ((g-b)/df) +240 )%360
    if mx==0:
        s=0
    else:
        s = df/mx
    v = mx
    return [h,s,v]


def hsvToRgb(colarr):
    h,s,v = colarr[:,:,0], colarr[:,:,1], colarr[:,:,2]
    h60 = h / 60.
    h60f= np.floor( h60 )
    hi = np.floor( h/60 ) % 6
    f = h60 - h60f
    p = v * (1-s)
    q = v * (1-f*s)
    t = v * (1-(1-f)*s)

    narr = np.zeros( colarr.shape )

    colKeys = [[        v,q,p,p,t,v],
               [    t,v,v,q,p,p    ],
               [p,p,t,v,v,q        ]]

    for col in range(3):
        for i in range(6):
            narr[:,:,col][hi==i] = colKeys[col][i][hi==i]

    narr *= 255
    return narr

        
def gradient( arr, start, end, swap=False ):
    start = rgbToHsv(start)
    end = rgbToHsv(end)

    if swap:
        end[0]+=360
    
    lerpedArr = colArrLerp( arr, start, end )
    lerpedArr[:,:,0][lerpedArr[:,:,0]<0]+=360

    
    return hsvToRgb(lerpedArr)

    return lerpedArr


def colArrLerp( arr, start, end ):
    narr = np.zeros( arr.shape+(3,) )
    narr[:,:,0] = start[0] + (end[0]-start[0])*arr
    narr[:,:,1] = start[1] + (end[1]-start[1])*arr
    narr[:,:,2] = start[2] + (end[2]-start[2])*arr
    return narr



if __name__ == '__main__':
    
    while True:
        h,s,v = [float(input()) for i in range(3)]
        print( hsvToRgb( np.array((((h,s,v),),)) ) )
        
    
