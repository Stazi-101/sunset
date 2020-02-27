
import pygame

from foreground import Foreground
from sky import Sky
from sun import Sun

def init(world):

    pygame.init()
    screen = pygame.display.set_mode( world.size )

    return screen

def firstDraw( world ):

    world.sky.create()

    draw( world )

    pygame.display.update()


def draw( world ):

    world.sky.draw()
    world.foreground.draw()
    world.sun.draw()

    pygame.display.update()
