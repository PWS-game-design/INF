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
    
wall01 = pygame.Rect(460, 960, 1000, 20)
wall02 = pygame.Rect(460, 100, 20, 860)
wall03 = pygame.Rect(1460, 100, 20, 880)
wall04 = pygame.Rect(530, 170, 200, 20)
wall05 = pygame.Rect(780, 170, 130, 20)
wall06 = pygame.Rect(1030, 170, 130, 20)
wall07 = pygame.Rect(960, 100, 20, 220)
wall08 = pygame.Rect(1210, 170, 200, 20)
wall09 = pygame.Rect(530, 170, 20, 200)
wall10 = pygame.Rect(1390, 170, 20, 200)
wall11 = pygame.Rect(530, 890, 200, 20)
wall12 = pygame.Rect(530, 690, 20, 200)
wall13 = pygame.Rect(780, 890, 130, 20)
wall14 = pygame.Rect(1030, 890, 130, 20)
wall15 = pygame.Rect(960, 750, 20, 220)
wall16 = pygame.Rect(1390, 690, 20, 200)
wall17 = pygame.Rect(1210, 890, 200, 20)
wall18 = pygame.Rect(600, 240, 310, 20)
wall19 = pygame.Rect(1030, 240, 310, 20)
wall20 = pygame.Rect(740, 240, 20, 200)
wall21 = pygame.Rect(1180, 240, 20, 200)
wall22 = pygame.Rect(1180, 240, 20, 200)
wall23 = pygame.Rect(810, 310, 320, 20)
wall24 = pygame.Rect(890, 380, 170, 20)
wall25 = pygame.Rect(810, 310, 20, 200)
wall26 = pygame.Rect(880, 380, 20, 320)
wall27 = pygame.Rect(1040, 380, 20, 115)
wall28 = pygame.Rect(1040, 565, 20, 135)
wall29 = pygame.Rect(890, 680, 170, 20)
wall30 = pygame.Rect(1110, 310, 20, 200)
wall31 = pygame.Rect(600, 310, 90, 20)
wall32 = pygame.Rect(1250, 310, 90, 20)
wall33 = pygame.Rect(600, 310, 20, 200)
wall34 = pygame.Rect(670, 380, 20, 310)
wall35 = pygame.Rect(600, 560, 20, 200)
wall36 = pygame.Rect(600, 820, 310, 20)
wall37 = pygame.Rect(530, 430, 20, 200)
wall38 = pygame.Rect(1390, 430, 20, 200)
wall39 = pygame.Rect(1250, 380, 20, 310)
wall40 = pygame.Rect(1320, 310, 20, 200)
wall41 = pygame.Rect(1320, 560, 20, 200)
wall42 = pygame.Rect(600, 750, 90, 20)
wall43 = pygame.Rect(1250, 750, 90, 20)
wall44 = pygame.Rect(810, 750, 320, 20)
wall45 = pygame.Rect(740, 620, 20, 200)
wall46 = pygame.Rect(1180, 620, 20, 20)
wall47 = pygame.Rect(600, 820, 200, 20)
wall48 = pygame.Rect (1030, 820, 310, 20)
wall49 = pygame.Rect(1110, 560, 20, 200)
wall50 = pygame.Rect(810, 560, 20, 200)
wall51 = pygame.Rect(740, 490, 20, 80)
wall52 = pygame.Rect(1180, 490, 20, 80)

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

