import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen_color = (0,0,0)
        screen.fill(screen_color)

        pygame.display.flip()







if __name__ == "__main__":
    main()

