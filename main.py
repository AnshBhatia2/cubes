import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("cubes")
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
purple = (255,0,255)

screen.fill("white")
pygame.display.update()

while True:
    class Cube():
        def __init__(self,color,dimensions):
            self.cube_surf = screen
            self.cube_color = color
            self.cube_dimensions = dimensions

        def draw(self):
            self.Draw_Cube = pygame.draw.rect(self.cube_surf, self.cube_color, self.cube_dimensions)

    yellowCube = Cube(yellow,(50,20,100,100))
    redCube = Cube(red,(150,200,150,150))
    purpleCube = Cube(purple,(300,400,200,200))

    yellowCube.draw()
    redCube.draw()
    purpleCube.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()