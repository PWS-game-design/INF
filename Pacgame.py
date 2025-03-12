
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
    

def sidecheckU():
    if checkU.colliderect(wallhitbox):
        return True
    else:
        return False

def sidecheckD():
    if checkD.colliderect(wallhitbox):
        return True
    else:
        return False
    
def sidecheckL():
    if checkL.colliderect(wallhitbox):
        return True
    else:
        return False
    
def sidecheckR():
    if checkR.colliderect(wallhitbox):
        return True
    else:
        return False

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fil the screen with a color to wipe away anyting from the last frame
    win.fill("black")

    # hitboxes
    pachitbox = pygame.Rect(pac_pos.x -20, pac_pos.y - 20, 40, 40)
    wallhitbox = pygame.Rect(250, 50, 2000, 50)
    checkU = pygame.Rect(pac_pos.x -15, pac_pos.y - 20, 30, 1)
    checkD = pygame.Rect(pac_pos.x -15, pac_pos.y + 20, 30, 1)
    checkL = pygame.Rect(pac_pos.x - 20, pac_pos.y - 15, 1, 30)
    checkR = pygame.Rect(pac_pos.x + 20, pac_pos.y - 15, 1, 30)




    # RENDER GAME HERE
    pygame.draw.circle(win, "yellow", pac_pos, 20)

    pygame.draw.circle(win, "blue", ghostB_pos, 10)
    pygame.draw.circle(win, "green", ghostG_pos, 10)
    pygame.draw.circle(win, "orange", ghostO_pos, 10)
    pygame.draw.circle(win, "red", ghostR_pos, 10)
    
    pygame.draw.rect(win, "blue", (460, 100, 1000, 20))
                                    # x, y, with, height tot. is 1920, 1060
                                    # linksboven is (0,0)
    pygame.draw.rect(win, "blue", (460, 960, 1000, 20))
    pygame.draw.rect(win, "blue", (460, 100, 20, 860))
    pygame.draw.rect(win, "blue", (1460, 100, 20, 880))
    pygame.draw.rect(win, "blue", (530, 170, 200, 20))
    pygame.draw.rect(win, "blue", (780, 170, 130, 20))
    pygame.draw.rect(win, "blue", (1030, 170, 130, 20))
    pygame.draw.rect(win, "blue", (960, 100, 20, 220))
    pygame.draw.rect(win, "blue", (1210, 170, 200, 20))
    pygame.draw.rect(win, "blue", (530, 170, 20, 200))
    pygame.draw.rect(win, "blue", (1390, 170, 20, 200))
    pygame.draw.rect(win, "blue", (530, 890, 200, 20))
    pygame.draw.rect(win, "blue", (530, 690, 20, 200))
    pygame.draw.rect(win, "blue", (780, 890, 130, 20))
    pygame.draw.rect(win, "blue", (1030, 890, 130, 20))
    pygame.draw.rect(win, "blue", (960, 750, 20, 220))
    pygame.draw.rect(win, "blue", (1390, 690, 20, 200))
    pygame.draw.rect(win, "blue", (1210, 890, 200, 20))
    pygame.draw.rect(win, "blue", (600, 240, 310, 20))
    pygame.draw.rect(win, "blue", (1030, 240, 310, 20))
    pygame.draw.rect(win, "blue", (740, 240, 20, 200))
    pygame.draw.rect(win, "blue", (1180, 240, 20, 200))
    pygame.draw.rect(win, "blue", (810, 310, 320, 20))
    pygame.draw.rect(win, "blue", (890, 380, 170, 20))
    pygame.draw.rect(win, "blue", (810, 310, 20, 200))
    pygame.draw.rect(win, "blue", (880, 380, 20, 320))
    pygame.draw.rect(win, "blue", (1040, 380, 20, 115))
    pygame.draw.rect(win, "blue", (1040, 565, 20, 135))
    pygame.draw.rect(win, "blue", (890, 680, 170, 20))
    pygame.draw.rect(win, "blue", (1110, 310, 20, 200))
    pygame.draw.rect(win, "blue", (600, 310, 90, 20))
    pygame.draw.rect(win, "blue", (1250, 310, 90, 20))
    pygame.draw.rect(win, "blue", (600, 310, 20, 200))
    pygame.draw.rect(win, "blue", (670, 380, 20, 310))
    pygame.draw.rect(win, "blue", (600, 560, 20, 200))
    pygame.draw.rect(win, "blue", (600, 820, 310, 20))
    pygame.draw.rect(win, "blue", (530, 430, 20, 200))
    pygame.draw.rect(win, "blue", (1390, 430, 20, 200))
    pygame.draw.rect(win, "blue", (1250, 380, 20, 310))
    pygame.draw.rect(win, "blue", (1320, 310, 20, 200))
    pygame.draw.rect(win, "blue", (1320, 560, 20, 200))
    pygame.draw.rect(win, "blue", (600, 750, 90, 20))
    pygame.draw.rect(win, "blue", (1250, 750, 90, 20))
    pygame.draw.rect(win, "blue", (810, 750, 320, 20))
    pygame.draw.rect(win, "blue", (740, 620, 20, 200))
    pygame.draw.rect(win, "blue", (1180, 620, 20, 200))
    pygame.draw.rect(win, "blue", (600, 820, 200, 20))
    pygame.draw.rect(win, "blue", (1030, 820, 310, 20))
    pygame.draw.rect(win, "blue", (1110, 560, 20, 200))
    pygame.draw.rect(win, "blue", (810, 560, 20, 200))
    pygame.draw.rect(win, "blue", (740, 490, 20, 80))
    pygame.draw.rect(win, "blue", (1180, 490, 20, 80))
    pygame.draw.rect(win, "orange", (500, 400, 10, 10))
    pygame.draw.rect(win, "orange", (535, 400, 10, 10))
    pygame.draw.rect(win, "orange", (570, 400, 10, 10))
    pygame.draw.rect(win, "orange", (570, 435, 10, 10))
    pygame.draw.rect(win, "orange", (570, 470, 10, 10))
    pygame.draw.rect(win, "orange", (570, 505, 10, 10))
    pygame.draw.rect(win, "orange", (570, 540, 10, 10))
    pygame.draw.rect(win, "orange", (570, 575, 10, 10))
    pygame.draw.rect(win, "orange", (570, 610, 10, 10))
    pygame.draw.rect(win, "orange", (570, 645, 10, 10))
    pygame.draw.rect(win, "orange", (570, 680, 10, 10))
    pygame.draw.rect(win, "orange", (570, 715, 10, 10))
    pygame.draw.rect(win, "orange", (570, 750, 10, 10))
    pygame.draw.rect(win, "orange", (570, 785, 10, 10))
    pygame.draw.rect(win, "orange", (570, 820, 10, 10))
    pygame.draw.rect(win, "orange", (570, 860, 10, 10))
    pygame.draw.rect(win, "orange", (605, 860, 10, 10))
    pygame.draw.rect(win, "orange", (640, 860, 10, 10))
    pygame.draw.rect(win, "orange", (675, 860, 10, 10))
    pygame.draw.rect(win, "orange", (710, 860, 10, 10))
    pygame.draw.rect(win, "orange", (750, 860, 10, 10))
    pygame.draw.rect(win, "orange", (750, 895, 10, 10))
    pygame.draw.rect(win, "orange", (750, 930, 10, 10))
    pygame.draw.rect(win, "orange", (500, 365, 10, 10))
    pygame.draw.rect(win, "orange", (500, 330, 10, 10))
    pygame.draw.rect(win, "orange", (500, 295, 10, 10))
    pygame.draw.rect(win, "orange", (500, 265, 10, 10))
    pygame.draw.rect(win, "orange", (500, 230, 10, 10))
    pygame.draw.rect(win, "orange", (500, 200, 10, 10))
    pygame.draw.rect(win, "orange", (500, 170, 10, 10))
    pygame.draw.rect(win, "orange", (500, 140, 10, 10))
    pygame.draw.rect(win, "orange", (500, 435, 10, 10))
    pygame.draw.rect(win, "orange", (500, 470, 10, 10))
    pygame.draw.rect(win, "orange", (500, 505, 10, 10))
    pygame.draw.rect(win, "orange", (500, 540, 10, 10))
    pygame.draw.rect(win, "orange", (500, 575, 10, 10))
    pygame.draw.rect(win, "orange", (500, 610, 10, 10))
    pygame.draw.rect(win, "orange", (500, 645, 10, 10))
    pygame.draw.rect(win, "orange", (500, 680, 10, 10))
    pygame.draw.rect(win, "orange", (500, 715, 10, 10))
    pygame.draw.rect(win, "orange", (500, 750, 10, 10))
    pygame.draw.rect(win, "orange", (535, 655, 10, 10))
    pygame.draw.rect(win, "orange", (500, 785, 10, 10))
    pygame.draw.rect(win, "orange", (500, 820, 10, 10))
    pygame.draw.rect(win, "orange", (500, 855, 10, 10))
    pygame.draw.rect(win, "orange", (500, 890, 10, 10))
    pygame.draw.rect(win, "orange", (500, 930, 10, 10))
    pygame.draw.rect(win, "orange", (535, 930, 10, 10))
    pygame.draw.rect(win, "orange", (570, 930, 10, 10))
    pygame.draw.rect(win, "orange", (605, 930, 10, 10))
    pygame.draw.rect(win, "orange", (640, 930, 10, 10))
    pygame.draw.rect(win, "orange", (675, 930, 10, 10))
    pygame.draw.rect(win, "orange", (710, 930, 10, 10))
    pygame.draw.rect(win, "orange", (785, 930, 10, 10))
    pygame.draw.rect(win, "orange", (820, 930, 10, 10))
    pygame.draw.rect(win, "orange", (855, 930, 10, 10))
    pygame.draw.rect(win, "orange", (890, 930, 10, 10))
    pygame.draw.rect(win, "orange", (930, 930, 10, 10))
    pygame.draw.rect(win, "orange", (930, 895, 10, 10))
    pygame.draw.rect(win, "orange", (930, 860, 10, 10))
    pygame.draw.rect(win, "orange", (930, 825, 10, 10))
    pygame.draw.rect(win, "orange", (930, 790, 10, 10))
    pygame.draw.rect(win, "orange", (895, 860, 10, 10))
    pygame.draw.rect(win, "orange", (860, 860, 10, 10))
    pygame.draw.rect(win, "orange", (825, 860, 10, 10))
    pygame.draw.rect(win, "orange", (790, 860, 10, 10))
    pygame.draw.rect(win, "orange", (860, 790, 10, 10))
    pygame.draw.rect(win, "orange", (825, 790, 10, 10))
    pygame.draw.rect(win, "orange", (780, 790, 10, 10))
    pygame.draw.rect(win, "orange", (895, 790, 10, 10))
    pygame.draw.rect(win, "orange", (780, 755, 10, 10))
    pygame.draw.rect(win, "orange", (780, 720, 10, 10))
    pygame.draw.rect(win, "orange", (780, 685, 10, 10))
    pygame.draw.rect(win, "orange", (780, 650, 10, 10))
    pygame.draw.rect(win, "orange", (780, 615, 10, 10))
    pygame.draw.rect(win, "orange", (780, 580, 10, 10))
    pygame.draw.rect(win, "orange", (780, 545, 10, 10))
    pygame.draw.rect(win, "orange", (780, 510, 10, 10))
    pygame.draw.rect(win, "orange", (780, 475, 10, 10))
    pygame.draw.rect(win, "orange", (780, 440, 10, 10))
    pygame.draw.rect(win, "orange", (780, 405, 10, 10))
    pygame.draw.rect(win, "orange", (780, 365, 10, 10))
    pygame.draw.rect(win, "orange", (780, 325, 10, 10))
    pygame.draw.rect(win, "orange", (780, 280, 10, 10))
    pygame.draw.rect(win, "orange", (780, 210, 10, 10))
    pygame.draw.rect(win, "orange", (535, 140, 10, 10))
    pygame.draw.rect(win, "orange", (570, 140, 10, 10))
    pygame.draw.rect(win, "orange", (605, 140, 10, 10))
    pygame.draw.rect(win, "orange", (640, 140, 10, 10))
    pygame.draw.rect(win, "orange", (675, 140, 10, 10))
    pygame.draw.rect(win, "orange", (710, 140, 10, 10))
    pygame.draw.rect(win, "orange", (785, 140, 10, 10))
    pygame.draw.rect(win, "orange", (820, 140, 10, 10))
    pygame.draw.rect(win, "orange", (855, 140, 10, 10))
    pygame.draw.rect(win, "orange", (890, 140, 10, 10))
    pygame.draw.rect(win, "orange", (930, 140, 10, 10))
    pygame.draw.rect(win, "orange", (750, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1000, 140, 10, 10))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and sidecheckU() == False:
        pac_pos.y -= 300 * dt
    if keys[pygame.K_s] and sidecheckD() == False:
        pac_pos.y += 300 * dt
    if keys[pygame.K_a] and sidecheckL() == False:
        pac_pos.x -= 300 * dt
    if keys[pygame.K_d] and sidecheckR() == False:
        pac_pos.x += 300 * dt







    # flip() the display to put your work on the screen
    pygame.display.flip()

    # fps limiter
    clock.tick(60) 

    # dt is delta time in seconds since last frame, used for framerate
    dt = clock.tick(60) / 1000

pygame.quit()

