
import pygame
import numpy as np


class Foreground():

    def __init__(self,world):

        self.world = world

        self.filename = 'scape.png'
        self.bool = None
        self.surf = None

        self.create()

    def create(self):

        self.surf = importImage(self.filename)
        self.bool = arrFromFun (self.surf)

    def draw(self):

        self.world.screen.blit( self.surf, (0,0) )

        

def importImage(name):

    surf = pygame.image.load(name)
    try:
        surf.convert()
    except:
        pass
    surf.set_colorkey( surf.get_at((0,0)) )

    return surf



def arrFromFun( surf ):

    shape = surf.get_size() #why was shape a peram?

    arr = np.ones( shape , dtype = bool )
    for x in range( shape[0] ):
        for y in range( shape[1] ):
            arr[x,y] = surf.get_at((x,y)) == (255,255,255,255)

    return arr


    
