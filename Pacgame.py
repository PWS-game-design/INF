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
flip = False
flip2 = False
# sprites
img = pygame.image.load("Untitled382.png").convert_alpha()
img2 = pygame.image.load("Untitled382flip.png").convert_alpha()
ghostB = pygame.image.load("Untitled383.png").convert_alpha()

img_copy = img.copy()

pygame.display.set_caption("Pacman")
pac_pos = pygame.Vector2(505, 145)
ghostB_pos = pygame.Vector2(970, 435)
ghostG_pos = pygame.Vector2(970, 505)
ghostO_pos = pygame.Vector2(970, 575)
ghostR_pos = pygame.Vector2(970, 645)


def ghostmovement():
    ghostB_pos
    

def sidecheckU():
    if checkU.colliderect(wallhitbox) or checkU.colliderect(wall01) or checkU.colliderect(wall02) or checkU.colliderect(wall03) or checkU.colliderect(wall04 ) or checkU.colliderect(wall05) or checkU.colliderect(wall06) or checkU.colliderect(wall07) or checkU.colliderect(wall08) or checkU.colliderect(wall09) or checkU.colliderect(wall10) or checkU.colliderect(wall11) or checkU.colliderect(wall12) or checkU.colliderect(wall13) or checkU.colliderect(wall14) or checkU.colliderect(wall15) or checkU.colliderect(wall16) or checkU.colliderect(wall17) or checkU.colliderect(wall18) or checkU.colliderect(wall19) or checkU.colliderect(wall20) or checkU.colliderect(wall21) or checkU.colliderect(wall22) or checkU.colliderect(wall23) or checkU.colliderect(wall24) or checkU.colliderect(wall25) or checkU.colliderect(wall26) or checkU.colliderect(wall27) or checkU.colliderect(wall28) or checkU.colliderect(wall29) or checkU.colliderect(wall30) or checkU.colliderect(wall31) or checkU.colliderect(wall32) or checkU.colliderect(wall33) or checkU.colliderect(wall34) or checkU.colliderect(wall35) or checkU.colliderect(wall36) or checkU.colliderect(wall37) or checkU.colliderect(wall38) or checkU.colliderect(wall39) or checkU.colliderect(wall40) or checkU.colliderect(wall41) or checkU.colliderect(wall42) or checkU.colliderect(wall43) or checkU.colliderect(wall44) or checkU.colliderect(wall45) or checkU.colliderect(wall46) or checkU.colliderect(wall47) or checkU.colliderect(wall48) or checkU.colliderect(wall49) or checkU.colliderect(wall50) or checkU.colliderect(wall51): 
        return True
    else:
        return False

def sidecheckD():
    if checkD.colliderect(wallhitbox) or checkD.colliderect(wall01) or checkD.colliderect(wall02) or checkD.colliderect(wall03) or checkD.colliderect(wall04 ) or checkD.colliderect(wall05) or checkD.colliderect(wall06) or checkD.colliderect(wall07) or checkD.colliderect(wall08) or checkD.colliderect(wall09) or checkD.colliderect(wall10) or checkD.colliderect(wall11) or checkD.colliderect(wall12) or checkD.colliderect(wall13) or checkD.colliderect(wall14) or checkD.colliderect(wall15) or checkD.colliderect(wall16) or checkD.colliderect(wall17) or checkD.colliderect(wall18) or checkD.colliderect(wall19) or checkD.colliderect(wall20) or checkD.colliderect(wall21) or checkD.colliderect(wall22) or checkD.colliderect(wall23) or checkD.colliderect(wall24) or checkD.colliderect(wall25) or checkD.colliderect(wall26) or checkD.colliderect(wall27) or checkD.colliderect(wall28) or checkD.colliderect(wall29) or checkD.colliderect(wall30) or checkD.colliderect(wall31) or checkD.colliderect(wall32) or checkD.colliderect(wall33) or checkD.colliderect(wall34) or checkD.colliderect(wall35) or checkD.colliderect(wall36) or checkD.colliderect(wall37) or checkD.colliderect(wall38) or checkD.colliderect(wall39) or checkD.colliderect(wall40) or checkD.colliderect(wall41) or checkD.colliderect(wall42) or checkD.colliderect(wall43) or checkD.colliderect(wall44) or checkD.colliderect(wall45) or checkD.colliderect(wall46) or checkD.colliderect(wall47) or checkD.colliderect(wall48) or checkD.colliderect(wall49) or checkD.colliderect(wall50) or checkD.colliderect(wall51):
        return True
    else:
        return False
    
def sidecheckL():
    if checkL.colliderect(wallhitbox) or checkL.colliderect(wall01) or checkL.colliderect(wall02) or checkL.colliderect(wall03) or checkL.colliderect(wall04 ) or checkL.colliderect(wall05) or checkL.colliderect(wall06) or checkL.colliderect(wall07) or checkL.colliderect(wall08) or checkL.colliderect(wall09) or checkL.colliderect(wall10) or checkL.colliderect(wall11) or checkL.colliderect(wall12) or checkL.colliderect(wall13) or checkL.colliderect(wall14) or checkL.colliderect(wall15) or checkL.colliderect(wall16) or checkL.colliderect(wall17) or checkL.colliderect(wall18) or checkL.colliderect(wall19) or checkL.colliderect(wall20) or checkL.colliderect(wall21) or checkL.colliderect(wall22) or checkL.colliderect(wall23) or checkL.colliderect(wall24) or checkL.colliderect(wall25) or checkL.colliderect(wall26) or checkL.colliderect(wall27) or checkL.colliderect(wall28) or checkL.colliderect(wall29) or checkL.colliderect(wall30) or checkL.colliderect(wall31) or checkL.colliderect(wall32) or checkL.colliderect(wall33) or checkL.colliderect(wall34) or checkL.colliderect(wall35) or checkL.colliderect(wall36) or checkL.colliderect(wall37) or checkL.colliderect(wall38) or checkL.colliderect(wall39) or checkL.colliderect(wall40) or checkL.colliderect(wall41) or checkL.colliderect(wall42) or checkL.colliderect(wall43) or checkL.colliderect(wall44) or checkL.colliderect(wall45) or checkL.colliderect(wall46) or checkL.colliderect(wall47) or checkL.colliderect(wall48) or checkL.colliderect(wall49) or checkL.colliderect(wall50) or checkL.colliderect(wall51):
        return True
    else:
        return False
    
def sidecheckR():
    if checkR.colliderect(wallhitbox) or checkR.colliderect(wall01) or checkR.colliderect(wall02) or checkR.colliderect(wall03) or checkR.colliderect(wall04 ) or checkR.colliderect(wall05) or checkR.colliderect(wall06) or checkR.colliderect(wall07) or checkR.colliderect(wall08) or checkR.colliderect(wall09) or checkR.colliderect(wall10) or checkR.colliderect(wall11) or checkR.colliderect(wall12) or checkR.colliderect(wall13) or checkR.colliderect(wall14) or checkR.colliderect(wall15) or checkR.colliderect(wall16) or checkR.colliderect(wall17) or checkR.colliderect(wall18) or checkR.colliderect(wall19) or checkR.colliderect(wall20) or checkR.colliderect(wall21) or checkR.colliderect(wall22) or checkR.colliderect(wall23) or checkR.colliderect(wall24) or checkR.colliderect(wall25) or checkR.colliderect(wall26) or checkR.colliderect(wall27) or checkR.colliderect(wall28) or checkR.colliderect(wall29) or checkR.colliderect(wall30) or checkR.colliderect(wall31) or checkR.colliderect(wall32) or checkR.colliderect(wall33) or checkR.colliderect(wall34) or checkR.colliderect(wall35) or checkR.colliderect(wall36) or checkR.colliderect(wall37) or checkR.colliderect(wall38) or checkR.colliderect(wall39) or checkR.colliderect(wall40) or checkR.colliderect(wall41) or checkR.colliderect(wall42) or checkR.colliderect(wall43) or checkR.colliderect(wall44) or checkR.colliderect(wall45) or checkR.colliderect(wall46) or checkR.colliderect(wall47) or checkR.colliderect(wall48) or checkR.colliderect(wall49) or checkR.colliderect(wall50) or checkR.colliderect(wall51):
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
wall22 = pygame.Rect(810, 310, 320, 20)
wall23 = pygame.Rect(890, 380, 170, 20)
wall24 = pygame.Rect(810, 310, 20, 200)
wall25 = pygame.Rect(880, 380, 20, 320)
wall26 = pygame.Rect(1040, 380, 20, 115)
wall27 = pygame.Rect(1040, 565, 20, 135)
wall28 = pygame.Rect(890, 680, 170, 20)
wall29 = pygame.Rect(1110, 310, 20, 200)
wall30 = pygame.Rect(600, 310, 90, 20)
wall31 = pygame.Rect(1250, 310, 90, 20)
wall32 = pygame.Rect(600, 310, 20, 200)
wall33 = pygame.Rect(670, 380, 20, 310)
wall34 = pygame.Rect(600, 560, 20, 200)
wall35 = pygame.Rect(600, 820, 310, 20)
wall36 = pygame.Rect(530, 430, 20, 200)
wall37 = pygame.Rect(1390, 430, 20, 200)
wall38 = pygame.Rect(1250, 380, 20, 310)
wall39 = pygame.Rect(1320, 310, 20, 200)
wall40 = pygame.Rect(1320, 560, 20, 200)
wall41 = pygame.Rect(600, 750, 90, 20)
wall42 = pygame.Rect(1250, 750, 90, 20)
wall43 = pygame.Rect(810, 750, 320, 20)
wall44 = pygame.Rect(740, 620, 20, 200)
wall45 = pygame.Rect(1180, 620, 20, 200)
wall46 = pygame.Rect(600, 820, 200, 20)
wall47 = pygame.Rect (1030, 820, 310, 20)
wall48 = pygame.Rect(1110, 560, 20, 200)
wall49 = pygame.Rect(810, 560, 20, 200)
wall50 = pygame.Rect(740, 490, 20, 80)
wall51 = pygame.Rect(1180, 490, 20, 80)

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fil the screen with a color to wipe away anyting from the last frame
    win.fill("black")

    # hitboxes
    pachitbox = pygame.Rect(pac_pos.x -20, pac_pos.y - 20, 40, 40)
    wallhitbox = pygame.Rect(460, 100, 1000, 20)
    checkU = pygame.Rect(pac_pos.x - 17, pac_pos.y - 22, 34, 1) 
    checkD = pygame.Rect(pac_pos.x - 17, pac_pos.y + 21, 34, 1)
    checkL = pygame.Rect(pac_pos.x - 22, pac_pos.y - 17, 1, 34)
    checkR = pygame.Rect(pac_pos.x + 21, pac_pos.y - 17, 1, 34)


    

    PAC = pygame.transform.flip(img_copy, flip, flip2)


    # RENDER GAME HERE
    pygame.draw.circle(win, "yellow", pac_pos, 20)
    win.blit(PAC, (pac_pos.x - 20, pac_pos.y - 20))

    win.blit(ghostB, (ghostB_pos.x - 20, ghostB_pos.y - 20))
    pygame.draw.circle(win, "blue", ghostB_pos, 10)
    pygame.draw.circle(win, "green", ghostG_pos, 10)
    pygame.draw.circle(win, "orange", ghostO_pos, 10)
    pygame.draw.circle(win, "red", ghostR_pos, 10)
    
    pygame.draw.rect(win, "blue", (460, 100, 1000, 20))
                                    # x, y, with, height tot. is 1920, 1060
                                    # linksboven is (0,0)
    pygame.draw.rect(win, "blue", (460, 960, 1000, 20)) # 1
    pygame.draw.rect(win, "blue", (460, 100, 20, 860)) # 2
    pygame.draw.rect(win, "blue", (1460, 100, 20, 880)) # 3
    pygame.draw.rect(win, "blue", (530, 170, 200, 20)) # 4
    pygame.draw.rect(win, "blue", (780, 170, 130, 20)) # 5
    pygame.draw.rect(win, "blue", (1030, 170, 130, 20)) # 6
    pygame.draw.rect(win, "blue", (960, 100, 20, 220)) # 7 
    pygame.draw.rect(win, "blue", (1210, 170, 200, 20)) # 8
    pygame.draw.rect(win, "blue", (530, 170, 20, 200)) # 9
    pygame.draw.rect(win, "blue", (1390, 170, 20, 200)) # 10
    pygame.draw.rect(win, "blue", (530, 890, 200, 20)) # 11
    pygame.draw.rect(win, "blue", (530, 690, 20, 200)) # 12
    pygame.draw.rect(win, "blue", (780, 890, 130, 20)) # 13
    pygame.draw.rect(win, "blue", (1030, 890, 130, 20)) # 14
    pygame.draw.rect(win, "blue", (960, 750, 20, 220)) # 15
    pygame.draw.rect(win, "blue", (1390, 690, 20, 200)) # 16
    pygame.draw.rect(win, "blue", (1210, 890, 200, 20)) # 17
    pygame.draw.rect(win, "blue", (600, 240, 310, 20)) # 18
    pygame.draw.rect(win, "blue", (1030, 240, 310, 20)) # 19
    pygame.draw.rect(win, "blue", (740, 240, 20, 200)) # 20
    pygame.draw.rect(win, "blue", (1180, 240, 20, 200)) # 21
    pygame.draw.rect(win, "blue", (810, 310, 320, 20)) # 22
    pygame.draw.rect(win, "blue", (890, 380, 170, 20)) # 23
    pygame.draw.rect(win, "blue", (810, 310, 20, 200)) # 24
    pygame.draw.rect(win, "blue", (880, 380, 20, 320)) # 25
    pygame.draw.rect(win, "blue", (1040, 380, 20, 115)) # 26
    pygame.draw.rect(win, "blue", (1040, 565, 20, 135)) # 27
    pygame.draw.rect(win, "blue", (890, 680, 170, 20)) # 28
    pygame.draw.rect(win, "blue", (1110, 310, 20, 200)) # 29
    pygame.draw.rect(win, "blue", (600, 310, 90, 20)) # 30
    pygame.draw.rect(win, "blue", (1250, 310, 90, 20)) # 31
    pygame.draw.rect(win, "blue", (600, 310, 20, 200)) # 32
    pygame.draw.rect(win, "blue", (670, 380, 20, 310)) # 33
    pygame.draw.rect(win, "blue", (600, 560, 20, 200)) # 34
    pygame.draw.rect(win, "blue", (600, 820, 310, 20)) # 35
    pygame.draw.rect(win, "blue", (530, 430, 20, 200)) # 36
    pygame.draw.rect(win, "blue", (1390, 430, 20, 200)) # 37
    pygame.draw.rect(win, "blue", (1250, 380, 20, 310)) # 38
    pygame.draw.rect(win, "blue", (1320, 310, 20, 200)) # 39
    pygame.draw.rect(win, "blue", (1320, 560, 20, 200)) # 40
    pygame.draw.rect(win, "blue", (600, 750, 90, 20)) # 41
    pygame.draw.rect(win, "blue", (1250, 750, 90, 20)) # 42
    pygame.draw.rect(win, "blue", (810, 750, 320, 20)) # 43
    pygame.draw.rect(win, "blue", (740, 620, 20, 200)) # 44
    pygame.draw.rect(win, "blue", (1180, 620, 20, 200)) # 45
    pygame.draw.rect(win, "blue", (600, 820, 200, 20)) # 46
    pygame.draw.rect(win, "blue", (1030, 820, 310, 20)) # 47
    pygame.draw.rect(win, "blue", (1110, 560, 20, 200)) # 48
    pygame.draw.rect(win, "blue", (810, 560, 20, 200)) # 49
    pygame.draw.rect(win, "blue", (740, 490, 20, 80)) # 50
    pygame.draw.rect(win, "blue", (1180, 490, 20, 80)) # 51
    
    pygame.draw.rect(win, "green", (500, 400, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (535, 400, 10, 10))
    pygame.draw.rect(win, "green", (570, 400, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (570, 435, 10, 10))
    pygame.draw.rect(win, "orange", (570, 470, 10, 10))
    pygame.draw.rect(win, "orange", (570, 505, 10, 10))
    pygame.draw.rect(win, "green", (570, 540, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (570, 575, 10, 10))
    pygame.draw.rect(win, "orange", (570, 610, 10, 10))
    pygame.draw.rect(win, "green", (570, 645, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (570, 680, 10, 10))
    pygame.draw.rect(win, "orange", (570, 715, 10, 10))
    pygame.draw.rect(win, "orange", (570, 750, 10, 10))
    pygame.draw.rect(win, "green", (570, 785, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (570, 820, 10, 10))
    pygame.draw.rect(win, "green", (570, 860, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (605, 860, 10, 10))
    pygame.draw.rect(win, "orange", (640, 860, 10, 10))
    pygame.draw.rect(win, "orange", (675, 860, 10, 10))
    pygame.draw.rect(win, "orange", (710, 860, 10, 10))
    pygame.draw.rect(win, "green", (750, 860, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (750, 895, 10, 10))
    pygame.draw.rect(win, "green", (750, 930, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (500, 365, 10, 10))
    pygame.draw.rect(win, "orange", (500, 330, 10, 10))
    pygame.draw.rect(win, "orange", (500, 295, 10, 10))
    pygame.draw.rect(win, "orange", (500, 265, 10, 10))
    pygame.draw.rect(win, "orange", (500, 230, 10, 10))
    pygame.draw.rect(win, "orange", (500, 200, 10, 10))
    pygame.draw.rect(win, "orange", (500, 170, 10, 10))
    pygame.draw.rect(win, "green", (500, 140, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (500, 435, 10, 10))
    pygame.draw.rect(win, "orange", (500, 470, 10, 10))
    pygame.draw.rect(win, "orange", (500, 505, 10, 10))
    pygame.draw.rect(win, "orange", (500, 540, 10, 10))
    pygame.draw.rect(win, "orange", (500, 575, 10, 10))
    pygame.draw.rect(win, "orange", (500, 610, 10, 10))
    pygame.draw.rect(win, "green", (500, 645, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (500, 680, 10, 10))
    pygame.draw.rect(win, "orange", (500, 715, 10, 10))
    pygame.draw.rect(win, "orange", (500, 750, 10, 10))
    pygame.draw.rect(win, "orange", (535, 655, 10, 10))
    pygame.draw.rect(win, "orange", (500, 785, 10, 10))
    pygame.draw.rect(win, "orange", (500, 820, 10, 10))
    pygame.draw.rect(win, "orange", (500, 855, 10, 10))
    pygame.draw.rect(win, "orange", (500, 890, 10, 10))
    pygame.draw.rect(win, "green", (500, 930, 10, 10)) #hp
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
    pygame.draw.rect(win, "green", (930, 930, 10, 10)) #hp
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
    pygame.draw.rect(win, "orange", (895, 790, 10, 10))
    pygame.draw.rect(win, "orange", (780, 790, 10, 10))
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
    pygame.draw.rect(win, "green", (1000, 140, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1035, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1070, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1105, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1140, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1180, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1210, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1245, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1280, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1315, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1350, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1385, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 140, 10, 10))
    pygame.draw.rect(win, "orange", (1180, 175, 10, 10))
    pygame.draw.rect(win, "orange", (1180, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1000, 175, 10, 10))
    pygame.draw.rect(win, "orange", (1000, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1000, 245, 10, 10))
    pygame.draw.rect(win, "orange", (1035, 280, 10, 10))
    pygame.draw.rect(win, "orange", (1070, 280, 10, 10))
    pygame.draw.rect(win, "orange", (1105, 280, 10, 10))
    pygame.draw.rect(win, "orange", (825, 280, 10, 10))
    pygame.draw.rect(win, "orange", (860, 280, 10, 10))
    pygame.draw.rect(win, "orange", (895, 280, 10, 10))
    pygame.draw.rect(win, "green", (930, 280, 10, 10))#hp
    pygame.draw.rect(win, "green", (570, 280, 10, 10))#hp
    pygame.draw.rect(win, "orange", (605, 280, 10, 10))
    pygame.draw.rect(win, "orange", (640, 280, 10, 10))
    pygame.draw.rect(win, "orange", (675, 280, 10, 10))
    pygame.draw.rect(win, "green", (710, 280, 10, 10))#hp
    pygame.draw.rect(win, "orange", (710, 315, 10, 10))
    pygame.draw.rect(win, "green", (710, 350, 10, 10))#hp
    pygame.draw.rect(win, "orange", (710, 385, 10, 10))
    pygame.draw.rect(win, "orange", (710, 420, 10, 10))
    pygame.draw.rect(win, "green", (710, 455, 10, 10))#hp
    pygame.draw.rect(win, "orange", (745, 455, 10, 10))
    pygame.draw.rect(win, "orange", (710, 490, 10, 10))
    pygame.draw.rect(win, "orange", (710, 525, 10, 10))
    pygame.draw.rect(win, "orange", (710, 560, 10, 10))
    pygame.draw.rect(win, "green", (710, 595, 10, 10))#hp
    pygame.draw.rect(win, "orange", (745, 595, 10, 10))
    pygame.draw.rect(win, "orange", (710, 630, 10, 10))
    pygame.draw.rect(win, "orange", (710, 665, 10, 10))
    pygame.draw.rect(win, "green", (710, 715, 10, 10))#hp
    pygame.draw.rect(win, "orange", (675, 715, 10, 10))
    pygame.draw.rect(win, "green", (640, 715, 10, 10))#hp
    pygame.draw.rect(win, "orange", (640, 680, 10, 10))
    pygame.draw.rect(win, "orange", (640, 645, 10, 10))
    pygame.draw.rect(win, "orange", (640, 610, 10, 10))
    pygame.draw.rect(win, "orange", (640, 575, 10, 10))
    pygame.draw.rect(win, "green", (640, 540, 10, 10))#hp
    pygame.draw.rect(win, "orange", (605, 540, 10, 10))
    pygame.draw.rect(win, "orange", (640, 500, 10, 10))
    pygame.draw.rect(win, "orange", (640, 460, 10, 10))
    pygame.draw.rect(win, "orange", (640, 425, 10, 10))
    pygame.draw.rect(win, "orange", (640, 390, 10, 10))
    pygame.draw.rect(win, "green", (640, 350, 10, 10))#hp
    pygame.draw.rect(win, "orange", (675, 350, 10, 10))
    pygame.draw.rect(win, "orange", (710, 750, 10, 10))
    pygame.draw.rect(win, "green", (710, 790, 10, 10))#hp
    pygame.draw.rect(win, "orange", (675, 790, 10, 10))
    pygame.draw.rect(win, "orange", (640, 790, 10, 10))
    pygame.draw.rect(win, "orange", (605, 790, 10, 10))
    pygame.draw.rect(win, "orange", (570, 315, 10, 10))
    pygame.draw.rect(win, "orange", (570, 350, 10, 10))
    pygame.draw.rect(win, "orange", (570, 245, 10, 10))
    pygame.draw.rect(win, "green", (570, 210, 10, 10))#hp
    pygame.draw.rect(win, "orange", (605, 210, 10, 10))
    pygame.draw.rect(win, "orange", (640, 210, 10, 10))
    pygame.draw.rect(win, "orange", (675, 210, 10, 10))
    pygame.draw.rect(win, "orange", (710, 210, 10, 10))
    pygame.draw.rect(win, "green", (750, 210, 10, 10))#hp
    pygame.draw.rect(win, "orange", (815, 210, 10, 10))
    pygame.draw.rect(win, "orange", (850, 210, 10, 10))
    pygame.draw.rect(win, "orange", (885, 210, 10, 10))
    pygame.draw.rect(win, "green", (930, 210, 10, 10))#hp
    pygame.draw.rect(win, "orange", (930, 175, 10, 10))
    pygame.draw.rect(win, "orange", (930, 245, 10, 10))
    pygame.draw.rect(win, "orange", (750, 175, 10, 10))
    pygame.draw.rect(win, "orange", (1000, 280, 10, 10))
    pygame.draw.rect(win, "orange", (1035, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1070, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1105, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1210, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1245, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1280, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1140, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1315, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 175, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 365, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 295, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 265, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 325, 10, 10))
    pygame.draw.rect(win, "green", (1430, 395, 10, 10))
    pygame.draw.rect(win, "orange", (1395, 395, 10, 10))
    pygame.draw.rect(win, "green", (1360, 395, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 235, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 210, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 435, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 470, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 505, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 505, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 540, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 575, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 610, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 645, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 680, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 715, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 750, 10, 10))
    pygame.draw.rect(win, "orange", (1395, 655, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 785, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 820, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 855, 10, 10))
    pygame.draw.rect(win, "orange", (1430, 890, 10, 10))
    pygame.draw.rect(win, "green", (1430, 930, 10, 10))
    pygame.draw.rect(win, "orange", (1360, 435, 10, 10))
    pygame.draw.rect(win, "orange", (1360, 470, 10, 10))
    pygame.draw.rect(win, "orange", (1360, 505, 10, 10))
    pygame.draw.rect(win, "green", (1360, 540, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (1360, 575, 10, 10))
    pygame.draw.rect(win, "orange", (1360, 610, 10, 10))
    pygame.draw.rect(win, "green", (1360, 645, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (1360, 680, 10, 10))
    pygame.draw.rect(win, "orange", (1360, 715, 10, 10))
    pygame.draw.rect(win, "orange", (1360, 750, 10, 10))
    pygame.draw.rect(win, "green", (1360, 785, 10, 10)) #hp
    pygame.draw.rect(win, "orange", (1360, 820, 10, 10))
    pygame.draw.rect(win, "green", (1360, 860, 10, 10)) #hp
    pygame.draw.rect(win, "green", (1150, 790, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 755, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 720, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 685, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 650, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 615, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 580, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 545, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 510, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 475, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 440, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 405, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 365, 10, 10))
    pygame.draw.rect(win, "orange", (1150, 325, 10, 10))
    pygame.draw.rect(win, "green", (1150, 280, 10, 10))#hp
    pygame.draw.rect(win, "green", (1220, 280, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1255, 280, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 280, 10, 10))
    pygame.draw.rect(win, "orange", (1325, 280, 10, 10))
    pygame.draw.rect(win, "green", (1360, 280, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1360, 245, 10, 10))
    pygame.draw.rect(win, "green", (1360, 210, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1360, 315, 10, 10))
    pygame.draw.rect(win, "orange", (1360, 350, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 315, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 350, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 385, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 420, 10, 10))
    pygame.draw.rect(win, "green", (1220, 455, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1220, 490, 10, 10))
    pygame.draw.rect(win, "orange", (1185, 455, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 525, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 560, 10, 10))
    pygame.draw.rect(win, "green", (1220, 595, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1185, 595, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 630, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 675, 10, 10))
    pygame.draw.rect(win, "green", (1220, 715, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1255, 715, 10, 10))
    pygame.draw.rect(win, "green", (1290, 715, 10, 10))#hp
    pygame.draw.rect(win, "green", (1290, 350, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1255, 350, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 385, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 420, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 455, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 490, 10, 10))
    pygame.draw.rect(win, "green", (1290, 525, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1325, 525, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 560, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 595, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 630, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 675, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 750, 10, 10))
    pygame.draw.rect(win, "green", (1220, 785, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1255, 785, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 785, 10, 10))
    pygame.draw.rect(win, "orange", (1325, 785, 10, 10))
    pygame.draw.rect(win, "orange", (1325, 860, 10, 10))
    pygame.draw.rect(win, "orange", (1290, 860, 10, 10))
    pygame.draw.rect(win, "orange", (1255, 860, 10, 10))
    pygame.draw.rect(win, "orange", (1220, 860, 10, 10))
    pygame.draw.rect(win, "green", (1185, 860, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1150, 860, 10, 10))
    pygame.draw.rect(win, "orange", (1115, 860, 10, 10))
    pygame.draw.rect(win, "orange", (1075, 860, 10, 10))
    pygame.draw.rect(win, "orange", (1040, 860, 10, 10))
    pygame.draw.rect(win, "green", (1000, 860, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1000, 825, 10, 10))
    pygame.draw.rect(win, "green", (1000, 790, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1035, 790, 10, 10))
    pygame.draw.rect(win, "orange", (1070, 790, 10, 10))
    pygame.draw.rect(win, "orange", (1110, 790, 10, 10))
    pygame.draw.rect(win, "orange", (1000, 895, 10, 10))
    pygame.draw.rect(win, "green", (1000, 930, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1035, 930, 10, 10))
    pygame.draw.rect(win, "orange", (1070, 930, 10, 10))
    pygame.draw.rect(win, "orange", (1105, 930, 10, 10))
    pygame.draw.rect(win, "orange", (1140, 930, 10, 10))
    pygame.draw.rect(win, "green", (1180, 930, 10, 10))#hp
    pygame.draw.rect(win, "orange", (1180, 895, 10, 10))
    pygame.draw.rect(win, "orange", (1215, 930, 10, 10))
    pygame.draw.rect(win, "orange", (1250, 930, 10, 10))
    pygame.draw.rect(win, "orange", (1285, 930, 10, 10))
    pygame.draw.rect(win, "orange", (1320, 930, 10, 10))
    pygame.draw.rect(win, "orange", (1355, 930, 10, 10))
    pygame.draw.rect(win, "orange", (1390, 930, 10, 10))
   

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and sidecheckU() == False:
        pac_pos.y -= 300 * dt
        img_copy = img2.copy()
        flip2 = True
    if keys[pygame.K_s] and sidecheckD() == False:
        pac_pos.y += 300 * dt
        flip2 = False
        img_copy = img2.copy()
    if keys[pygame.K_a] and sidecheckL() == False:
        pac_pos.x -= 300 * dt
        flip = True
        flip2 = False
        img_copy = img.copy()
    if keys[pygame.K_d] and sidecheckR() == False:
        pac_pos.x += 300 * dt
        flip = False
        flip2 = False
        img_copy = img.copy()







    # flip() the display to put your work on the screen
    pygame.display.flip()

    # fps limiter
    clock.tick(60) 

    # dt is delta time in seconds since last frame, used for framerate
    dt = clock.tick(60) / 1000

pygame.quit()

