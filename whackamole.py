import pygame
from random import randrange


def main():

    def Griddraw():
        size = 32
        for x in range(0,640,size):
            for y in range(0,512,size):
                rect = pygame.Rect(x,y,size,size)
                pygame.draw.rect(screen, (0,0,0), rect,1 )
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        molex, moley =  0, 0
        clock = pygame.time.Clock()
        running = True
        clicked = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            Griddraw()
            screen.blit(mole_image, mole_image.get_rect(topleft=(molex,moley)))
            pygame.display.flip()
            clock.tick(60)
            if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                clicked = True
                if clicked:
                    targetx, targety = molex, moley
                    width, height = 32, 32
                    x, y = event.pos
                    if targetx <= x <= targetx + width and targety <= y <= targety + height:
                        molex = randrange(0,640 - 32,32)
                        moley = randrange(0,512 - 32,32)

            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = False


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
