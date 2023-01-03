# Imports
import sys
import pygame
import pygame.freetype

from mem_comp import Mem2D

DISPX, DISPY = 1024, 1024
FPS = 30

if __name__ == '__main__':
    # Initialize pygame
    pygame.init()
    # Initialize display
    screen = pygame.display.set_mode((DISPX, DISPY))
    screen.fill((255, 255, 255))
    # Initialize Font
    font = pygame.freetype.SysFont('Sans', 20)
    # Initialize clock
    clock = pygame.time.Clock()
    # Initialize Memory
    mem = Mem2D(9, 9)

    mem.draw(screen, font)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(20)
    for k in range(10):
        for i in range(10):
            for j in range(10):            
                mem.access((i, k))
                mem.draw(screen, font)
                pygame.display.flip()
                pygame.display.update()
                clock.tick(20)



    # cells = []
    # for i in range(10):
    #     for j in range(10):
    #         cells.append(MemCell((i, j)))
    # 

    # # Initial setup
    # for cell in cells:
    #     cell.draw(screen, font)
    # pygame.display.flip()
    # pygame.display.update()

    # for cell in cells:
    #     cell.access()
    #     cell.draw(screen, font)    
    #     pygame.display.flip()
    #     pygame.display.update()
    #     clock.tick(FPS)

    # for cell in cells:
    #     cell.access()
    #     cell.draw(screen, font)    
    #     pygame.display.flip()
    #     pygame.display.update()
    #     clock.tick(FPS)



    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit(0)
    #         elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
    #             sys.exit(0)
    #     for cell in cells:
    #         cell.draw(screen)
    #     pygame.display.flip()
    #     pygame.display.update()

    #     clock.tick(FPS)

