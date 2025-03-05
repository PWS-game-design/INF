
import pygame
import random as r
import time
pygame.init()

# resolution
resx = 1920
resy = 1080


# pygame setup
win = pygame.display.set_mode((resx, resy))
clock = pygame.time.Clock()
running = True
dt = 0


pygame.display.set_caption("Pacman")
pac_pos = pygame.Vector2(win.get_width() / 5, win.get_height() / 5)
ghostB_pos = pygame.Vector2(win.get_width() / 1.5, win.get_height() / 1.5)
ghostG_pos = pygame.Vector2(win.get_width() / 2, win.get_height() / 2)
ghostO_pos = pygame.Vector2(win.get_width() / 2.5, win.get_height() / 2.5)
ghostR_pos = pygame.Vector2(win.get_width() / 3, win.get_height() / 3)

wall1 = pygame.Vector2(20, 50)

def ghostmovement():
    ghostB_pos

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fil the screen with a color to wipe away anytinh from the last frame
    win.fill("black")

    # hitboxes
    pachitbox = pygame.Rect(pac_pos.x -20, pac_pos.y - 20, 40, 40)
    wallhitbox = pygame.Rect(250, 50, 2000, 50)
    sidecheckU = pygame.Rect(pac_pos.x, pac_pos.y - 20, 1, 1)
    sidecheckD = pygame.Rect(pac_pos.x, pac_pos.y + 20, 1, 1)
    sidecheckL = pygame.Rect(pac_pos.x - 20, pac_pos.y, 1, 1)
    sidecheckR = pygame.Rect(pac_pos.x + 20, pac_pos.y, 1, 1)




    # RENDER GAME HERE
    pygame.draw.circle(win, "yellow", pac_pos, 20)
    pygame.draw.circle(win, "blue", ghostB_pos, 10)
    pygame.draw.circle(win, "green", ghostG_pos, 10)
    pygame.draw.circle(win, "orange", ghostO_pos, 10)
    pygame.draw.circle(win, "red", ghostR_pos, 10)
    
    pygame.draw.rect(win, "blue", (250, 50, 2000, 50))
                                    # x, y, with, height
                                    # linksboven is (0,0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and sidecheckU.colliderect(wallhitbox) == False:
        pac_pos.y -= 300 * dt
    if keys[pygame.K_s] and sidecheckD.colliderect(wallhitbox) == False:
        pac_pos.y += 300 * dt
    if keys[pygame.K_a] and sidecheckL.colliderect(wallhitbox) == False:
        pac_pos.x -= 300 * dt
    if keys[pygame.K_d] and sidecheckR.colliderect(wallhitbox) == False:
        pac_pos.x += 300 * dt







    # flip() the display to put your work on the screen
    pygame.display.flip()

    # fps limiter
    clock.tick(60) 

    # dt is delta time in seconds since last frame, used for framerate
    dt = clock.tick(60) / 1000

pygame.quit()

