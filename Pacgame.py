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

x = 0
# sprites
yippee1 = pygame.image.load("frame_00_delay-0.1s.png").convert_alpha()
yippee2 = pygame.image.load("frame_01_delay-0.1s.png").convert_alpha()
yippee3 = pygame.image.load("frame_02_delay-0.1s.png").convert_alpha()
yippee4 = pygame.image.load("frame_03_delay-0.1s.png").convert_alpha()
yippee5 = pygame.image.load("frame_04_delay-0.1s.png").convert_alpha()
yippee6 = pygame.image.load("frame_05_delay-0.1s.png").convert_alpha()
yippee7 = pygame.image.load("frame_06_delay-0.1s.png").convert_alpha()
yippee8 = pygame.image.load("frame_07_delay-0.1s.png").convert_alpha()
yippee9 = pygame.image.load("frame_08_delay-0.1s.png").convert_alpha()
yippee10 = pygame.image.load("frame_09_delay-0.1s.png").convert_alpha()
yippee11 = pygame.image.load("frame_10_delay-0.1s.png").convert_alpha()
yippee12 = pygame.image.load("frame_11_delay-0.1s.png").convert_alpha()
yippee13 = pygame.image.load("frame_12_delay-0.1s.png").convert_alpha()
yippee = [yippee1, yippee2, yippee3, yippee4, yippee5, yippee6, yippee7, yippee8, yippee9, yippee10, yippee11, yippee12, yippee13]
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
    
ldot1 =	(500, 400, 10, 10) 
ldot2 =	(535, 400, 10, 10)
ldot3 =	(570, 400, 10, 10) 
ldot4 =	(570, 435, 10, 10)
ldot5 =	(570, 470, 10, 10)
ldot6 =	(570, 505, 10, 10)
ldot7	=	(570, 540, 10, 10) 
ldot8	=	(570, 575, 10, 10)
ldot9	=	(570, 610, 10, 10)
ldot10	=	(570, 645, 10, 10) 
ldot11	=	(570, 680, 10, 10)
ldot12	=	(570, 715, 10, 10)
ldot13	=	(570, 750, 10, 10)
ldot14	=	(570, 785, 10, 10) 
ldot15	=	(570, 820, 10, 10)
ldot16	=	(570, 860, 10, 10) 
ldot17	=	(605, 860, 10, 10)
ldot18	=	(640, 860, 10, 10)
ldot19	=	(675, 860, 10, 10)
ldot20	=	(710, 860, 10, 10)
ldot21	=	(750, 860, 10, 10) 
ldot22	=	(750, 895, 10, 10)
ldot23	=	(750, 930, 10, 10) 
ldot24	=	(500, 365, 10, 10)
ldot25	=	(500, 330, 10, 10)
ldot26	=	(500, 295, 10, 10)
ldot27	=	(500, 265, 10, 10)
ldot28	=	(500, 230, 10, 10)
ldot29	=	(500, 200, 10, 10)
ldot30	=	(500, 170, 10, 10)
ldot31	=	(500, 140, 10, 10) 
ldot32	=	(500, 435, 10, 10)
ldot33	=	(500, 470, 10, 10)
ldot34	=	(500, 505, 10, 10)
ldot35	=	(500, 540, 10, 10)
ldot36	=	(500, 575, 10, 10)
ldot37	=	(500, 610, 10, 10)
ldot38	=	(500, 645, 10, 10) 
ldot39	=	(500, 680, 10, 10)
ldot40	=	(500, 715, 10, 10)
ldot41	=	(500, 750, 10, 10)
ldot42	=	(535, 655, 10, 10)
ldot43	=	(500, 785, 10, 10)
ldot44	=	(500, 820, 10, 10)
ldot45	=	(500, 855, 10, 10)
ldot46	=	(500, 890, 10, 10)
ldot47	=	(500, 930, 10, 10) 
ldot48	=	(535, 930, 10, 10)
ldot49	=	(570, 930, 10, 10)
ldot50	=	(605, 930, 10, 10)
ldot51	=	(640, 930, 10, 10)
ldot52	=	(675, 930, 10, 10)
ldot53	=	(710, 930, 10, 10)
ldot54	=	(785, 930, 10, 10)
ldot55	=	(820, 930, 10, 10)
ldot56	=	(855, 930, 10, 10)
ldot57	=	(890, 930, 10, 10)
ldot58	=	(930, 930, 10, 10) 
ldot59	=	(930, 895, 10, 10)
ldot60	=	(930, 860, 10, 10)
ldot61	=	(930, 825, 10, 10)
ldot62	=	(930, 790, 10, 10)
ldot63	=	(895, 860, 10, 10)
ldot64	=	(860, 860, 10, 10)
ldot65	=	(825, 860, 10, 10)
ldot66	=	(790, 860, 10, 10)
ldot67	=	(860, 790, 10, 10)
ldot68	=	(825, 790, 10, 10)
ldot69	=	(895, 790, 10, 10)
ldot70	=	(780, 790, 10, 10)
ldot71	=	(780, 755, 10, 10)
ldot72	=	(780, 720, 10, 10)
ldot73	=	(780, 685, 10, 10)
ldot74	=	(780, 650, 10, 10)
ldot75	=	(780, 615, 10, 10)
ldot76	=	(780, 580, 10, 10)
ldot77	=	(780, 545, 10, 10)
ldot78	=	(780, 510, 10, 10)
ldot79	=	(780, 475, 10, 10)
ldot80	=	(780, 440, 10, 10)
ldot81	=	(780, 405, 10, 10)
ldot82	=	(780, 365, 10, 10)
ldot83	=	(780, 325, 10, 10)
ldot84	=	(780, 280, 10, 10)
ldot85	=	(780, 210, 10, 10)
ldot86	=	(535, 140, 10, 10)
ldot87	=	(570, 140, 10, 10)
ldot88	=	(605, 140, 10, 10)
ldot89	=	(640, 140, 10, 10)
ldot90	=	(675, 140, 10, 10)
ldot91	=	(710, 140, 10, 10)
ldot92	=	(785, 140, 10, 10)
ldot93	=	(820, 140, 10, 10)
ldot94	=	(855, 140, 10, 10)
ldot95	=	(890, 140, 10, 10)
ldot96	=	(930, 140, 10, 10)
ldot97	=	(750, 140, 10, 10)
ldot98	=	(1000, 140, 10, 10)
ldot99	=	(1035, 140, 10, 10)
ldot100	=	(1070, 140, 10, 10)
ldot101	=	(1105, 140, 10, 10)
ldot102	=	(1140, 140, 10, 10)
ldot103	=	(1180, 140, 10, 10)
ldot104	=	(1210, 140, 10, 10)
ldot105	=	(1245, 140, 10, 10)
ldot106	=	(1280, 140, 10, 10)
ldot107	=	(1315, 140, 10, 10)
ldot108	=	(1350, 140, 10, 10)
ldot109	=	(1385, 140, 10, 10)
ldot110	=	(1430, 140, 10, 10)
ldot111	=	(1180, 175, 10, 10)
ldot112	=	(1180, 210, 10, 10)
ldot113	=	(1000, 175, 10, 10)
ldot114	=	(1000, 210, 10, 10)
ldot115	=	(1000, 245, 10, 10)
ldot116	=	(1035, 280, 10, 10)
ldot117	=	(1070, 280, 10, 10)
ldot118	=	(1105, 280, 10, 10)
ldot119	=	(825, 280, 10, 10)
ldot120	=	(860, 280, 10, 10)
ldot121	=	(895, 280, 10, 10)
ldot122	=	(930, 280, 10, 10)
ldot123	=	(570, 280, 10, 10)
ldot124	=	(605, 280, 10, 10)
ldot125	=	(640, 280, 10, 10)
ldot126	=	(675, 280, 10, 10)
ldot127	=	(710, 280, 10, 10)
ldot128	=	(710, 315, 10, 10)
ldot129	=	(710, 350, 10, 10)
ldot130	=	(710, 385, 10, 10)
ldot131	=	(710, 420, 10, 10)
ldot132	=	(710, 455, 10, 10)
ldot133	=	(745, 455, 10, 10)
ldot134	=	(710, 490, 10, 10)
ldot135	=	(710, 525, 10, 10)
ldot136	=	(710, 560, 10, 10)
ldot137	=	(710, 595, 10, 10)
ldot138	=	(745, 595, 10, 10)
ldot139	=	(710, 630, 10, 10)
ldot140	=	(710, 665, 10, 10)
ldot141	=	(710, 715, 10, 10)
ldot142	=	(675, 715, 10, 10)
ldot143	=	(640, 715, 10, 10)
ldot144	=	(640, 680, 10, 10)
ldot145	=	(640, 645, 10, 10)
ldot146	=	(640, 610, 10, 10)
ldot147	=	(640, 575, 10, 10)
ldot148	=	(640, 540, 10, 10)
ldot149	=	(605, 540, 10, 10)
ldot150	=	(640, 500, 10, 10)
ldot151	=	(640, 460, 10, 10)
ldot152	=	(640, 425, 10, 10)
ldot153	=	(640, 390, 10, 10)
ldot154	=	(640, 350, 10, 10)
ldot155	=	(675, 350, 10, 10)
ldot156	=	(710, 750, 10, 10)
ldot157	=	(710, 790, 10, 10)
ldot158	=	(675, 790, 10, 10)
ldot159	=	(640, 790, 10, 10)
ldot160	=	(605, 790, 10, 10)
ldot161	=	(570, 315, 10, 10)
ldot162	=	(570, 350, 10, 10)
ldot163	=	(570, 245, 10, 10)
ldot164	=	(570, 210, 10, 10)
ldot165	=	(605, 210, 10, 10)
ldot166	=	(640, 210, 10, 10)
ldot167	=	(675, 210, 10, 10)
ldot168	=	(710, 210, 10, 10)
ldot169	=	(750, 210, 10, 10)
ldot170	=	(815, 210, 10, 10)
ldot171	=	(850, 210, 10, 10)
ldot172	=	(885, 210, 10, 10)
ldot173	=	(930, 210, 10, 10)
ldot174	=	(930, 175, 10, 10)
ldot175	=	(930, 245, 10, 10)
ldot176	=	(750, 175, 10, 10)
ldot177	=	(1000, 280, 10, 10)
ldot178	=	(1035, 210, 10, 10)
ldot179	=	(1070, 210, 10, 10)
ldot180	=	(1105, 210, 10, 10)
ldot181	=	(1210, 210, 10, 10)
ldot182	=	(1245, 210, 10, 10)
ldot183	=	(1280, 210, 10, 10)
ldot184	=	(1140, 210, 10, 10)
ldot185	=	(1315, 210, 10, 10)
ldot186	=	(1430, 175, 10, 10)
ldot187	=	(1430, 210, 10, 10)
ldot188	=	(1430, 365, 10, 10)
ldot189	=	(1430, 295, 10, 10)
ldot190	=	(1430, 265, 10, 10)
ldot191	=	(1430, 325, 10, 10)
ldot192	=	(1430, 395, 10, 10)
ldot193	=	(1395, 395, 10, 10)
ldot194	=	(1360, 395, 10, 10)
ldot195	=	(1430, 235, 10, 10)
ldot196	=	(1430, 210, 10, 10)
ldot197	=	(1430, 435, 10, 10)
ldot198	=	(1430, 470, 10, 10)
ldot199	=	(1430, 505, 10, 10)
ldot200	=	(1430, 505, 10, 10)
ldot201	=	(1430, 540, 10, 10)
ldot202	=	(1430, 575, 10, 10)
ldot203	=	(1430, 610, 10, 10)
ldot204	=	(1430, 645, 10, 10)
ldot205	=	(1430, 680, 10, 10)
ldot206	=	(1430, 715, 10, 10)
ldot207	=	(1430, 750, 10, 10)
ldot208	=	(1395, 655, 10, 10)
ldot209	=	(1430, 785, 10, 10)
ldot210	=	(1430, 820, 10, 10)
ldot211	=	(1430, 855, 10, 10)
ldot212	=	(1430, 890, 10, 10)
ldot213	=	(1430, 930, 10, 10)
ldot214	=	(1360, 435, 10, 10)
ldot215	=	(1360, 470, 10, 10)
ldot216	=	(1360, 505, 10, 10)
ldot217	=	(1360, 540, 10, 10) 
ldot218	=	(1360, 575, 10, 10)
ldot219	=	(1360, 610, 10, 10)
ldot220	=	(1360, 645, 10, 10) 
ldot221	=	(1360, 680, 10, 10)
ldot222	=	(1360, 715, 10, 10)
ldot223	=	(1360, 750, 10, 10)
ldot224	=	(1360, 785, 10, 10) 
ldot225	=	(1360, 820, 10, 10)
ldot226	=	(1360, 860, 10, 10) 
ldot227	=	(1150, 790, 10, 10)
ldot228	=	(1150, 755, 10, 10)
ldot229	=	(1150, 720, 10, 10)
ldot230	=	(1150, 685, 10, 10)
ldot231	=	(1150, 650, 10, 10)
ldot232	=	(1150, 615, 10, 10)
ldot233	=	(1150, 580, 10, 10)
ldot234	=	(1150, 545, 10, 10)
ldot235	=	(1150, 510, 10, 10)
ldot236	=	(1150, 475, 10, 10)
ldot237	=	(1150, 440, 10, 10)
ldot238	=	(1150, 405, 10, 10)
ldot239	=	(1150, 365, 10, 10)
ldot240	=	(1150, 325, 10, 10)
ldot241	=	(1150, 280, 10, 10)
ldot242	=	(1220, 280, 10, 10)
ldot243	=	(1255, 280, 10, 10)
ldot244	=	(1290, 280, 10, 10)
ldot245	=	(1325, 280, 10, 10)
ldot246	=	(1360, 280, 10, 10)
ldot247	=	(1360, 245, 10, 10)
ldot248	=	(1360, 210, 10, 10)
ldot249	=	(1360, 315, 10, 10)
ldot250	=	(1360, 350, 10, 10)
ldot251	=	(1220, 315, 10, 10)
ldot252	=	(1220, 350, 10, 10)
ldot253	=	(1220, 385, 10, 10)
ldot254	=	(1220, 420, 10, 10)
ldot255	=	(1220, 455, 10, 10)
ldot256	=	(1220, 490, 10, 10)
ldot257	=	(1185, 455, 10, 10)
ldot258	=	(1220, 525, 10, 10)
ldot259	=	(1220, 560, 10, 10)
ldot260	=	(1220, 595, 10, 10)
ldot261	=	(1185, 595, 10, 10)
ldot262	=	(1220, 630, 10, 10)
ldot263	=	(1220, 675, 10, 10)
ldot264	=	(1220, 715, 10, 10)
ldot265	=	(1255, 715, 10, 10)
ldot266	=	(1290, 715, 10, 10)
ldot267	=	(1290, 350, 10, 10)
ldot268	=	(1255, 350, 10, 10)
ldot269	=	(1290, 385, 10, 10)
ldot270	=	(1290, 420, 10, 10)
ldot271	=	(1290, 455, 10, 10)
ldot272	=	(1290, 490, 10, 10)
ldot273	=	(1290, 525, 10, 10)
ldot274	=	(1325, 525, 10, 10)
ldot275	=	(1290, 560, 10, 10)
ldot276	=	(1290, 595, 10, 10)
ldot277	=	(1290, 630, 10, 10)
ldot278	=	(1290, 675, 10, 10)
ldot279	=	(1220, 750, 10, 10)
ldot280	=	(1220, 785, 10, 10)
ldot281	=	(1255, 785, 10, 10)
ldot282	=	(1290, 785, 10, 10)
ldot283	=	(1325, 785, 10, 10)
ldot284	=	(1325, 860, 10, 10)
ldot285	=	(1290, 860, 10, 10)
ldot286	=	(1255, 860, 10, 10)
ldot287	=	(1220, 860, 10, 10)
ldot288	=	(1185, 860, 10, 10)
ldot289	=	(1150, 860, 10, 10)
ldot290	=	(1115, 860, 10, 10)
ldot291	=	(1075, 860, 10, 10)
ldot292	=	(1040, 860, 10, 10)
ldot293	=	(1000, 860, 10, 10)
ldot294	=	(1000, 825, 10, 10)
ldot295	=	(1000, 790, 10, 10)
ldot296	=	(1035, 790, 10, 10)
ldot297	=	(1070, 790, 10, 10)
ldot298	=	(1110, 790, 10, 10)
ldot299	=	(1000, 895, 10, 10)
ldot300	=	(1000, 930, 10, 10)
ldot301	=	(1035, 930, 10, 10)
ldot302	=	(1070, 930, 10, 10)
ldot303	=	(1105, 930, 10, 10)
ldot304	=	(1140, 930, 10, 10)
ldot305	=	(1180, 930, 10, 10)
ldot306	=	(1180, 895, 10, 10)
ldot307	=	(1215, 930, 10, 10)
ldot308	=	(1250, 930, 10, 10)
ldot309	=	(1285, 930, 10, 10)
ldot310	=	(1320, 930, 10, 10)
ldot311	=	(1355, 930, 10, 10)
ldot312	=	(1390, 930, 10, 10)

list = [
ldot1, 
ldot2,
ldot3, 
ldot4,
ldot5,
ldot6,
ldot7, 
ldot8,
ldot9,
ldot10, 
ldot11,
ldot12,
ldot13,
ldot14, 
ldot15,
ldot16, 
ldot17,
ldot18,
ldot19,
ldot20,
ldot21, 
ldot22,
ldot23, 
ldot24,
ldot25,
ldot26,
ldot27,
ldot28,
ldot29,
ldot30,
ldot31, 
ldot32,
ldot33,
ldot34,
ldot35,
ldot36,
ldot37,
ldot38, 
ldot39,
ldot40,
ldot41,
ldot42,
ldot43,
ldot44,
ldot45,
ldot46,
ldot47, 
ldot48,
ldot49,
ldot50,
ldot51,
ldot52,
ldot53,
ldot54,
ldot55,
ldot56,
ldot57,
ldot58, 
ldot59,
ldot60,
ldot61,
ldot62,
ldot63,
ldot64,
ldot65,
ldot66,
ldot67,
ldot68,
ldot69,
ldot70,
ldot71,
ldot72,
ldot73,
ldot74,
ldot75,
ldot76,
ldot77,
ldot78,
ldot79,
ldot80,
ldot81,
ldot82,
ldot83,
ldot84,
ldot85,
ldot86,
ldot87,
ldot88,
ldot89,
ldot90,
ldot91,
ldot92,
ldot93,
ldot94,
ldot95,
ldot96,
ldot97,
ldot98,
ldot99,
ldot100,
ldot101,
ldot102,
ldot103,
ldot104,
ldot105,
ldot106,
ldot107,
ldot108,
ldot109,
ldot110,
ldot111,
ldot112,
ldot113,
ldot114,
ldot115,
ldot116,
ldot117,
ldot118,
ldot119,
ldot120,
ldot121,
ldot122,
ldot123,
ldot124,
ldot125,
ldot126,
ldot127,
ldot128,
ldot129,
ldot130,
ldot131,
ldot132,
ldot133,
ldot134,
ldot135,
ldot136,
ldot137,
ldot138,
ldot139,
ldot140,
ldot141,
ldot142,
ldot143,
ldot144,
ldot145,
ldot146,
ldot147,
ldot148,
ldot149,
ldot150,
ldot151,
ldot152,
ldot153,
ldot154,
ldot155,
ldot156,
ldot157,
ldot158,
ldot159,
ldot160,
ldot161,
ldot162,
ldot163,
ldot164,
ldot165,
ldot166,
ldot167,
ldot168,
ldot169,
ldot170,
ldot171,
ldot172,
ldot173,
ldot174,
ldot175,
ldot176,
ldot177,
ldot178,
ldot179,
ldot180,
ldot181,
ldot182,
ldot183,
ldot184,
ldot185,
ldot186,
ldot187,
ldot188,
ldot189,
ldot190,
ldot191,
ldot192,
ldot193,
ldot194,
ldot195,
ldot196,
ldot197,
ldot198,
ldot199,
ldot200,
ldot201,
ldot202,
ldot203,
ldot204,
ldot205,
ldot206,
ldot207,
ldot208,
ldot209,
ldot210,
ldot211,
ldot212,
ldot213,
ldot214,
ldot215,
ldot216,
ldot217, 
ldot218,
ldot219,
ldot220, 
ldot221,
ldot222,
ldot223,
ldot224, 
ldot225,
ldot226, 
ldot227,
ldot228,
ldot229,
ldot230,
ldot231,
ldot232,
ldot233,
ldot234,
ldot235,
ldot236,
ldot237,
ldot238,
ldot239,
ldot240,
ldot241,
ldot242,
ldot243,
ldot244,
ldot245,
ldot246,
ldot247,
ldot248,
ldot249,
ldot250,
ldot251,
ldot252,
ldot253,
ldot254,
ldot255,
ldot256,
ldot257,
ldot258,
ldot259,
ldot260,
ldot261,
ldot262,
ldot263,
ldot264,
ldot265,
ldot266,
ldot267,
ldot268,
ldot269,
ldot270,
ldot271,
ldot272,
ldot273,
ldot274,
ldot275,
ldot276,
ldot277,
ldot278,
ldot279,
ldot280,
ldot281,
ldot282,
ldot283,
ldot284,
ldot285,
ldot286,
ldot287,
ldot288,
ldot289,
ldot290,
ldot291,
ldot292,
ldot293,
ldot294,
ldot295,
ldot296,
ldot297,
ldot298,
ldot299,
ldot300,
ldot301,
ldot302,
ldot303,
ldot304,
ldot305,
ldot306,
ldot307,
ldot308,
ldot309,
ldot310,
ldot311,
ldot312,]


    
def walls():
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


def dots():
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
    pygame.draw.rect(win, "green", (750, 860, 10, 10)) #hp`
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

dot1 =	pygame.Rect(500, 400, 10, 10) 
dot2 =	pygame.Rect(535, 400, 10, 10)
dot3 =	pygame.Rect(570, 400, 10, 10) 
dot4 =	pygame.Rect(570, 435, 10, 10)
dot5 =	pygame.Rect(570, 470, 10, 10)
dot6 =	pygame.Rect(570, 505, 10, 10)
dot7	=	pygame.Rect(570, 540, 10, 10) 
dot8	=	pygame.Rect(570, 575, 10, 10)
dot9	=	pygame.Rect(570, 610, 10, 10)
dot10	=	pygame.Rect(570, 645, 10, 10) 
dot11	=	pygame.Rect(570, 680, 10, 10)
dot12	=	pygame.Rect(570, 715, 10, 10)
dot13	=	pygame.Rect(570, 750, 10, 10)
dot14	=	pygame.Rect(570, 785, 10, 10) 
dot15	=	pygame.Rect(570, 820, 10, 10)
dot16	=	pygame.Rect(570, 860, 10, 10) 
dot17	=	pygame.Rect(605, 860, 10, 10)
dot18	=	pygame.Rect(640, 860, 10, 10)
dot19	=	pygame.Rect(675, 860, 10, 10)
dot20	=	pygame.Rect(710, 860, 10, 10)
dot21	=	pygame.Rect(750, 860, 10, 10) 
dot22	=	pygame.Rect(750, 895, 10, 10)
dot23	=	pygame.Rect(750, 930, 10, 10) 
dot24	=	pygame.Rect(500, 365, 10, 10)
dot25	=	pygame.Rect(500, 330, 10, 10)
dot26	=	pygame.Rect(500, 295, 10, 10)
dot27	=	pygame.Rect(500, 265, 10, 10)
dot28	=	pygame.Rect(500, 230, 10, 10)
dot29	=	pygame.Rect(500, 200, 10, 10)
dot30	=	pygame.Rect(500, 170, 10, 10)
dot31	=	pygame.Rect(500, 140, 10, 10) 
dot32	=	pygame.Rect(500, 435, 10, 10)
dot33	=	pygame.Rect(500, 470, 10, 10)
dot34	=	pygame.Rect(500, 505, 10, 10)
dot35	=	pygame.Rect(500, 540, 10, 10)
dot36	=	pygame.Rect(500, 575, 10, 10)
dot37	=	pygame.Rect(500, 610, 10, 10)
dot38	=	pygame.Rect(500, 645, 10, 10) 
dot39	=	pygame.Rect(500, 680, 10, 10)
dot40	=	pygame.Rect(500, 715, 10, 10)
dot41	=	pygame.Rect(500, 750, 10, 10)
dot42	=	pygame.Rect(535, 655, 10, 10)
dot43	=	pygame.Rect(500, 785, 10, 10)
dot44	=	pygame.Rect(500, 820, 10, 10)
dot45	=	pygame.Rect(500, 855, 10, 10)
dot46	=	pygame.Rect(500, 890, 10, 10)
dot47	=	pygame.Rect(500, 930, 10, 10) 
dot48	=	pygame.Rect(535, 930, 10, 10)
dot49	=	pygame.Rect(570, 930, 10, 10)
dot50	=	pygame.Rect(605, 930, 10, 10)
dot51	=	pygame.Rect(640, 930, 10, 10)
dot52	=	pygame.Rect(675, 930, 10, 10)
dot53	=	pygame.Rect(710, 930, 10, 10)
dot54	=	pygame.Rect(785, 930, 10, 10)
dot55	=	pygame.Rect(820, 930, 10, 10)
dot56	=	pygame.Rect(855, 930, 10, 10)
dot57	=	pygame.Rect(890, 930, 10, 10)
dot58	=	pygame.Rect(930, 930, 10, 10) 
dot59	=	pygame.Rect(930, 895, 10, 10)
dot60	=	pygame.Rect(930, 860, 10, 10)
dot61	=	pygame.Rect(930, 825, 10, 10)
dot62	=	pygame.Rect(930, 790, 10, 10)
dot63	=	pygame.Rect(895, 860, 10, 10)
dot64	=	pygame.Rect(860, 860, 10, 10)
dot65	=	pygame.Rect(825, 860, 10, 10)
dot66	=	pygame.Rect(790, 860, 10, 10)
dot67	=	pygame.Rect(860, 790, 10, 10)
dot68	=	pygame.Rect(825, 790, 10, 10)
dot69	=	pygame.Rect(895, 790, 10, 10)
dot70	=	pygame.Rect(780, 790, 10, 10)
dot71	=	pygame.Rect(780, 755, 10, 10)
dot72	=	pygame.Rect(780, 720, 10, 10)
dot73	=	pygame.Rect(780, 685, 10, 10)
dot74	=	pygame.Rect(780, 650, 10, 10)
dot75	=	pygame.Rect(780, 615, 10, 10)
dot76	=	pygame.Rect(780, 580, 10, 10)
dot77	=	pygame.Rect(780, 545, 10, 10)
dot78	=	pygame.Rect(780, 510, 10, 10)
dot79	=	pygame.Rect(780, 475, 10, 10)
dot80	=	pygame.Rect(780, 440, 10, 10)
dot81	=	pygame.Rect(780, 405, 10, 10)
dot82	=	pygame.Rect(780, 365, 10, 10)
dot83	=	pygame.Rect(780, 325, 10, 10)
dot84	=	pygame.Rect(780, 280, 10, 10)
dot85	=	pygame.Rect(780, 210, 10, 10)
dot86	=	pygame.Rect(535, 140, 10, 10)
dot87	=	pygame.Rect(570, 140, 10, 10)
dot88	=	pygame.Rect(605, 140, 10, 10)
dot89	=	pygame.Rect(640, 140, 10, 10)
dot90	=	pygame.Rect(675, 140, 10, 10)
dot91	=	pygame.Rect(710, 140, 10, 10)
dot92	=	pygame.Rect(785, 140, 10, 10)
dot93	=	pygame.Rect(820, 140, 10, 10)
dot94	=	pygame.Rect(855, 140, 10, 10)
dot95	=	pygame.Rect(890, 140, 10, 10)
dot96	=	pygame.Rect(930, 140, 10, 10)
dot97	=	pygame.Rect(750, 140, 10, 10)
dot98	=	pygame.Rect(1000, 140, 10, 10)
dot99	=	pygame.Rect(1035, 140, 10, 10)
dot100	=	pygame.Rect(1070, 140, 10, 10)
dot101	=	pygame.Rect(1105, 140, 10, 10)
dot102	=	pygame.Rect(1140, 140, 10, 10)
dot103	=	pygame.Rect(1180, 140, 10, 10)
dot104	=	pygame.Rect(1210, 140, 10, 10)
dot105	=	pygame.Rect(1245, 140, 10, 10)
dot106	=	pygame.Rect(1280, 140, 10, 10)
dot107	=	pygame.Rect(1315, 140, 10, 10)
dot108	=	pygame.Rect(1350, 140, 10, 10)
dot109	=	pygame.Rect(1385, 140, 10, 10)
dot110	=	pygame.Rect(1430, 140, 10, 10)
dot111	=	pygame.Rect(1180, 175, 10, 10)
dot112	=	pygame.Rect(1180, 210, 10, 10)
dot113	=	pygame.Rect(1000, 175, 10, 10)
dot114	=	pygame.Rect(1000, 210, 10, 10)
dot115	=	pygame.Rect(1000, 245, 10, 10)
dot116	=	pygame.Rect(1035, 280, 10, 10)
dot117	=	pygame.Rect(1070, 280, 10, 10)
dot118	=	pygame.Rect(1105, 280, 10, 10)
dot119	=	pygame.Rect(825, 280, 10, 10)
dot120	=	pygame.Rect(860, 280, 10, 10)
dot121	=	pygame.Rect(895, 280, 10, 10)
dot122	=	pygame.Rect(930, 280, 10, 10)
dot123	=	pygame.Rect(570, 280, 10, 10)
dot124	=	pygame.Rect(605, 280, 10, 10)
dot125	=	pygame.Rect(640, 280, 10, 10)
dot126	=	pygame.Rect(675, 280, 10, 10)
dot127	=	pygame.Rect(710, 280, 10, 10)
dot128	=	pygame.Rect(710, 315, 10, 10)
dot129	=	pygame.Rect(710, 350, 10, 10)
dot130	=	pygame.Rect(710, 385, 10, 10)
dot131	=	pygame.Rect(710, 420, 10, 10)
dot132	=	pygame.Rect(710, 455, 10, 10)
dot133	=	pygame.Rect(745, 455, 10, 10)
dot134	=	pygame.Rect(710, 490, 10, 10)
dot135	=	pygame.Rect(710, 525, 10, 10)
dot136	=	pygame.Rect(710, 560, 10, 10)
dot137	=	pygame.Rect(710, 595, 10, 10)
dot138	=	pygame.Rect(745, 595, 10, 10)
dot139	=	pygame.Rect(710, 630, 10, 10)
dot140	=	pygame.Rect(710, 665, 10, 10)
dot141	=	pygame.Rect(710, 715, 10, 10)
dot142	=	pygame.Rect(675, 715, 10, 10)
dot143	=	pygame.Rect(640, 715, 10, 10)
dot144	=	pygame.Rect(640, 680, 10, 10)
dot145	=	pygame.Rect(640, 645, 10, 10)
dot146	=	pygame.Rect(640, 610, 10, 10)
dot147	=	pygame.Rect(640, 575, 10, 10)
dot148	=	pygame.Rect(640, 540, 10, 10)
dot149	=	pygame.Rect(605, 540, 10, 10)
dot150	=	pygame.Rect(640, 500, 10, 10)
dot151	=	pygame.Rect(640, 460, 10, 10)
dot152	=	pygame.Rect(640, 425, 10, 10)
dot153	=	pygame.Rect(640, 390, 10, 10)
dot154	=	pygame.Rect(640, 350, 10, 10)
dot155	=	pygame.Rect(675, 350, 10, 10)
dot156	=	pygame.Rect(710, 750, 10, 10)
dot157	=	pygame.Rect(710, 790, 10, 10)
dot158	=	pygame.Rect(675, 790, 10, 10)
dot159	=	pygame.Rect(640, 790, 10, 10)
dot160	=	pygame.Rect(605, 790, 10, 10)
dot161	=	pygame.Rect(570, 315, 10, 10)
dot162	=	pygame.Rect(570, 350, 10, 10)
dot163	=	pygame.Rect(570, 245, 10, 10)
dot164	=	pygame.Rect(570, 210, 10, 10)
dot165	=	pygame.Rect(605, 210, 10, 10)
dot166	=	pygame.Rect(640, 210, 10, 10)
dot167	=	pygame.Rect(675, 210, 10, 10)
dot168	=	pygame.Rect(710, 210, 10, 10)
dot169	=	pygame.Rect(750, 210, 10, 10)
dot170	=	pygame.Rect(815, 210, 10, 10)
dot171	=	pygame.Rect(850, 210, 10, 10)
dot172	=	pygame.Rect(885, 210, 10, 10)
dot173	=	pygame.Rect(930, 210, 10, 10)
dot174	=	pygame.Rect(930, 175, 10, 10)
dot175	=	pygame.Rect(930, 245, 10, 10)
dot176	=	pygame.Rect(750, 175, 10, 10)
dot177	=	pygame.Rect(1000, 280, 10, 10)
dot178	=	pygame.Rect(1035, 210, 10, 10)
dot179	=	pygame.Rect(1070, 210, 10, 10)
dot180	=	pygame.Rect(1105, 210, 10, 10)
dot181	=	pygame.Rect(1210, 210, 10, 10)
dot182	=	pygame.Rect(1245, 210, 10, 10)
dot183	=	pygame.Rect(1280, 210, 10, 10)
dot184	=	pygame.Rect(1140, 210, 10, 10)
dot185	=	pygame.Rect(1315, 210, 10, 10)
dot186	=	pygame.Rect(1430, 175, 10, 10)
dot187	=	pygame.Rect(1430, 210, 10, 10)
dot188	=	pygame.Rect(1430, 365, 10, 10)
dot189	=	pygame.Rect(1430, 295, 10, 10)
dot190	=	pygame.Rect(1430, 265, 10, 10)
dot191	=	pygame.Rect(1430, 325, 10, 10)
dot192	=	pygame.Rect(1430, 395, 10, 10)
dot193	=	pygame.Rect(1395, 395, 10, 10)
dot194	=	pygame.Rect(1360, 395, 10, 10)
dot195	=	pygame.Rect(1430, 235, 10, 10)
dot196	=	pygame.Rect(1430, 210, 10, 10)
dot197	=	pygame.Rect(1430, 435, 10, 10)
dot198	=	pygame.Rect(1430, 470, 10, 10)
dot199	=	pygame.Rect(1430, 505, 10, 10)
dot200	=	pygame.Rect(1430, 505, 10, 10)
dot201	=	pygame.Rect(1430, 540, 10, 10)
dot202	=	pygame.Rect(1430, 575, 10, 10)
dot203	=	pygame.Rect(1430, 610, 10, 10)
dot204	=	pygame.Rect(1430, 645, 10, 10)
dot205	=	pygame.Rect(1430, 680, 10, 10)
dot206	=	pygame.Rect(1430, 715, 10, 10)
dot207	=	pygame.Rect(1430, 750, 10, 10)
dot208	=	pygame.Rect(1395, 655, 10, 10)
dot209	=	pygame.Rect(1430, 785, 10, 10)
dot210	=	pygame.Rect(1430, 820, 10, 10)
dot211	=	pygame.Rect(1430, 855, 10, 10)
dot212	=	pygame.Rect(1430, 890, 10, 10)
dot213	=	pygame.Rect(1430, 930, 10, 10)
dot214	=	pygame.Rect(1360, 435, 10, 10)
dot215	=	pygame.Rect(1360, 470, 10, 10)
dot216	=	pygame.Rect(1360, 505, 10, 10)
dot217	=	pygame.Rect(1360, 540, 10, 10) 
dot218	=	pygame.Rect(1360, 575, 10, 10)
dot219	=	pygame.Rect(1360, 610, 10, 10)
dot220	=	pygame.Rect(1360, 645, 10, 10) 
dot221	=	pygame.Rect(1360, 680, 10, 10)
dot222	=	pygame.Rect(1360, 715, 10, 10)
dot223	=	pygame.Rect(1360, 750, 10, 10)
dot224	=	pygame.Rect(1360, 785, 10, 10) 
dot225	=	pygame.Rect(1360, 820, 10, 10)
dot226	=	pygame.Rect(1360, 860, 10, 10) 
dot227	=	pygame.Rect(1150, 790, 10, 10)
dot228	=	pygame.Rect(1150, 755, 10, 10)
dot229	=	pygame.Rect(1150, 720, 10, 10)
dot230	=	pygame.Rect(1150, 685, 10, 10)
dot231	=	pygame.Rect(1150, 650, 10, 10)
dot232	=	pygame.Rect(1150, 615, 10, 10)
dot233	=	pygame.Rect(1150, 580, 10, 10)
dot234	=	pygame.Rect(1150, 545, 10, 10)
dot235	=	pygame.Rect(1150, 510, 10, 10)
dot236	=	pygame.Rect(1150, 475, 10, 10)
dot237	=	pygame.Rect(1150, 440, 10, 10)
dot238	=	pygame.Rect(1150, 405, 10, 10)
dot239	=	pygame.Rect(1150, 365, 10, 10)
dot240	=	pygame.Rect(1150, 325, 10, 10)
dot241	=	pygame.Rect(1150, 280, 10, 10)
dot242	=	pygame.Rect(1220, 280, 10, 10)
dot243	=	pygame.Rect(1255, 280, 10, 10)
dot244	=	pygame.Rect(1290, 280, 10, 10)
dot245	=	pygame.Rect(1325, 280, 10, 10)
dot246	=	pygame.Rect(1360, 280, 10, 10)
dot247	=	pygame.Rect(1360, 245, 10, 10)
dot248	=	pygame.Rect(1360, 210, 10, 10)
dot249	=	pygame.Rect(1360, 315, 10, 10)
dot250	=	pygame.Rect(1360, 350, 10, 10)
dot251	=	pygame.Rect(1220, 315, 10, 10)
dot252	=	pygame.Rect(1220, 350, 10, 10)
dot253	=	pygame.Rect(1220, 385, 10, 10)
dot254	=	pygame.Rect(1220, 420, 10, 10)
dot255	=	pygame.Rect(1220, 455, 10, 10)
dot256	=	pygame.Rect(1220, 490, 10, 10)
dot257	=	pygame.Rect(1185, 455, 10, 10)
dot258	=	pygame.Rect(1220, 525, 10, 10)
dot259	=	pygame.Rect(1220, 560, 10, 10)
dot260	=	pygame.Rect(1220, 595, 10, 10)
dot261	=	pygame.Rect(1185, 595, 10, 10)
dot262	=	pygame.Rect(1220, 630, 10, 10)
dot263	=	pygame.Rect(1220, 675, 10, 10)
dot264	=	pygame.Rect(1220, 715, 10, 10)
dot265	=	pygame.Rect(1255, 715, 10, 10)
dot266	=	pygame.Rect(1290, 715, 10, 10)
dot267	=	pygame.Rect(1290, 350, 10, 10)
dot268	=	pygame.Rect(1255, 350, 10, 10)
dot269	=	pygame.Rect(1290, 385, 10, 10)
dot270	=	pygame.Rect(1290, 420, 10, 10)
dot271	=	pygame.Rect(1290, 455, 10, 10)
dot272	=	pygame.Rect(1290, 490, 10, 10)
dot273	=	pygame.Rect(1290, 525, 10, 10)
dot274	=	pygame.Rect(1325, 525, 10, 10)
dot275	=	pygame.Rect(1290, 560, 10, 10)
dot276	=	pygame.Rect(1290, 595, 10, 10)
dot277	=	pygame.Rect(1290, 630, 10, 10)
dot278	=	pygame.Rect(1290, 675, 10, 10)
dot279	=	pygame.Rect(1220, 750, 10, 10)
dot280	=	pygame.Rect(1220, 785, 10, 10)
dot281	=	pygame.Rect(1255, 785, 10, 10)
dot282	=	pygame.Rect(1290, 785, 10, 10)
dot283	=	pygame.Rect(1325, 785, 10, 10)
dot284	=	pygame.Rect(1325, 860, 10, 10)
dot285	=	pygame.Rect(1290, 860, 10, 10)
dot286	=	pygame.Rect(1255, 860, 10, 10)
dot287	=	pygame.Rect(1220, 860, 10, 10)
dot288	=	pygame.Rect(1185, 860, 10, 10)
dot289	=	pygame.Rect(1150, 860, 10, 10)
dot290	=	pygame.Rect(1115, 860, 10, 10)
dot291	=	pygame.Rect(1075, 860, 10, 10)
dot292	=	pygame.Rect(1040, 860, 10, 10)
dot293	=	pygame.Rect(1000, 860, 10, 10)
dot294	=	pygame.Rect(1000, 825, 10, 10)
dot295	=	pygame.Rect(1000, 790, 10, 10)
dot296	=	pygame.Rect(1035, 790, 10, 10)
dot297	=	pygame.Rect(1070, 790, 10, 10)
dot298	=	pygame.Rect(1110, 790, 10, 10)
dot299	=	pygame.Rect(1000, 895, 10, 10)
dot300	=	pygame.Rect(1000, 930, 10, 10)
dot301	=	pygame.Rect(1035, 930, 10, 10)
dot302	=	pygame.Rect(1070, 930, 10, 10)
dot303	=	pygame.Rect(1105, 930, 10, 10)
dot304	=	pygame.Rect(1140, 930, 10, 10)
dot305	=	pygame.Rect(1180, 930, 10, 10)
dot306	=	pygame.Rect(1180, 895, 10, 10)
dot307	=	pygame.Rect(1215, 930, 10, 10)
dot308	=	pygame.Rect(1250, 930, 10, 10)
dot309	=	pygame.Rect(1285, 930, 10, 10)
dot310	=	pygame.Rect(1320, 930, 10, 10)
dot311	=	pygame.Rect(1355, 930, 10, 10)
dot312	=	pygame.Rect(1390, 930, 10, 10)

clist = [dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10, dot11, dot12, dot13, dot14, dot15, dot16, dot17, dot18, dot19, dot20, dot21, dot22, dot23, dot24, dot25, dot26, dot27, dot28, dot29, dot30, dot31, dot32, dot33, dot34, dot35, dot36, dot37, dot38, dot39, dot40, dot41, dot42, dot43, dot44, dot45, dot46, dot47, dot48, dot49, dot50, dot51, dot52, dot53, dot54, dot55, dot56, dot57, dot58, dot59, dot60, dot61, dot62, dot63, dot64, dot65, dot66, dot67, dot68, dot69, dot70, dot71, dot72, dot73, dot74, dot75, dot76, dot77, dot78, dot79, dot80, dot81, dot82, dot83, dot84, dot85, dot86, dot87, dot88, dot89, dot90, dot91, dot92, dot93, dot94, dot95, dot96, dot97, dot98, dot99, dot100, dot101, dot102, dot103, dot104, dot105, dot106, dot107, dot108, dot109, dot110, dot111, dot112, dot113, dot114, dot115, dot116, dot117, dot118, dot119, dot120, dot121, dot122, dot123, dot124, dot125, dot126, dot127, dot128, dot129, dot130, dot131, dot132, dot133, dot134, dot135, dot136, dot137, dot138, dot139, dot140, dot141, dot142, dot143, dot144, dot145, dot146, dot147, dot148, dot149, dot150, dot151, dot152, dot153, dot154, dot155, dot156, dot157, dot158, dot159, dot160, dot161, dot162, dot163, dot164, dot165, dot166, dot167, dot168, dot169, dot170, dot171, dot172, dot173, dot174, dot175, dot176, dot177, dot178, dot179, dot180, dot181, dot182, dot183, dot184, dot185, dot186, dot187, dot188, dot189, dot190, dot191, dot192, dot193, dot194, dot195, dot196, dot197, dot198, dot199, dot200, dot201, dot202, dot203, dot204, dot205, dot206, dot207, dot208, dot209, dot210, dot211, dot212, dot213, dot214, dot215, dot216, dot217, dot218, dot219, dot220, dot221, dot222, dot223, dot224, dot225, dot226, dot227, dot228, dot229, dot230, dot231, dot232, dot233, dot234, dot235, dot236, dot237, dot238, dot239, dot240, dot241, dot242, dot243, dot244, dot245, dot246, dot247, dot248, dot249, dot250, dot251, dot252, dot253, dot254, dot255, dot256, dot257, dot258, dot259, dot260, dot261, dot262, dot263, dot264, dot265, dot266, dot267, dot268, dot269, dot270, dot271, dot272, dot273, dot274, dot275, dot276, dot277, dot278, dot279, dot280, dot281, dot282, dot283, dot284, dot285, dot286, dot287, dot288, dot289, dot290, dot291, dot292, dot293, dot294, dot295, dot296, dot297, dot298, dot299, dot300, dot301, dot302, dot303, dot304, dot305, dot306, dot307, dot308, dot309, dot310, dot311, dot312]


t1 = False
t2 = False

while running:


    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    
    # fil the screen with a color to wipe away anyting from the last frame
    win.fill("black")


    
    if len(list) > 0:
        # hitboxes
        pachitbox = pygame.Rect(pac_pos.x -20, pac_pos.y - 20, 40, 40)
        wallhitbox = pygame.Rect(460, 100, 1000, 20)
        checkU = pygame.Rect(pac_pos.x - 17, pac_pos.y - 22, 34, 1) 
        checkD = pygame.Rect(pac_pos.x - 17, pac_pos.y + 21, 34, 1)
        checkL = pygame.Rect(pac_pos.x - 22, pac_pos.y - 17, 1, 34)
        checkR = pygame.Rect(pac_pos.x + 21, pac_pos.y - 17, 1, 34)

        PAC = pygame.transform.flip(img_copy, flip, flip2)

        
        for i in list:
            pygame.draw.rect(win, "orange", (i))

        for i in clist:
            if pachitbox.colliderect(i):
                clist.remove(i)
                list.remove(i)        

        # RENDER GAME HERE
        win.blit(PAC, (pac_pos.x - 20, pac_pos.y - 20))

        win.blit(ghostB, (ghostB_pos.x - 20, ghostB_pos.y - 20))


        pygame.draw.circle(win, "green", ghostG_pos, 10)
        pygame.draw.circle(win, "orange", ghostO_pos, 10)
        pygame.draw.circle(win, "red", ghostR_pos, 10)
        
        pygame.draw.rect(win, "blue", (460, 100, 1000, 20))
                                        # x, y, with, height tot. is 1920, 1060
                                        # linksboven is (0,0)







        walls()
        #dots()



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

        if keys[pygame.K_t]:
            for i in list:
                list.remove(i)


        





    
    else:
        for i in yippee:
            win.fill("black")            
            win.blit(i, (850, 450))
            # flip() the display to put your work on the screen
            pygame.display.flip()

            # fps limiter
            clock.tick(60) 

            # dt is delta time in seconds since last frame, used for framerate
            dt = clock.tick(60) / 1000

        x += 1
    
    if x == 5:
        running = False
    # flip() the display to put your work on the screen
    pygame.display.flip()

    # fps limiter
    clock.tick(60) 

    # dt is delta time in seconds since last frame, used for framerate
    dt = clock.tick(60) / 1000

pygame.quit()