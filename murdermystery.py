import pygame
pygame.init()

# resolution
resx = 1920
resy = 1080

# pygame setup
win = pygame.display.set_mode((resx, resy))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Murder Mystery")

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fil the screen with a color to wipe away anytinh from the last frame
    win.fill("black")

    # RENDER GAME HERE


    # flip() the display to put your work on the screen
    pygame.display.flip()

    # fps limiter
    clock.tick(60) 

pygame.quit()

