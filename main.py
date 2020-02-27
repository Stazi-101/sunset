
import pygame
import graphics
from foreground import Foreground
from sky import Sky
from sun import Sun

class World():

    def __init__(self):

        self.size = (800,400)
        self.fps = 30
        self.screen = None

        self.sky = Sky(self)
        self.foreground = Foreground(self)
        self.sun = Sun(self)

    def tick(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True

        if pygame.mouse.get_pressed()[0]:

            mx,my = pygame.mouse.get_pos()
            self.sun.x = mx
            self.sun.y = my
            self.sun.b = (self.size[1] - my)*4 #This prolly needs tweaking

            graphics.firstDraw(self)
            pygame.display.update()

        elif pygame.mouse.get_pressed()[2]:

            self.sun.x , self.sun.y = pygame.mouse.get_pos()

            graphics.draw(self)
            pygame.display.update()




def init(world):
    
    pygame.init()
    world.screen = pygame.display.set_mode(world.size)
    world.screen.fill([255,50,100])
    pygame.display.update()


def main():

    world = World()
    init(world)

    graphics.firstDraw(world)

    loop(world)


def loop(world):

    clock = pygame.time.Clock()#
    end = False
    while not end:
        
        end = world.tick()
        clock.tick(world.fps)


if __name__ == '__main__':
    main()


        
