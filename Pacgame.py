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
    



d1 = False
d2 = False
d3 = False
d4 = False
d5 = False
d6 = False
d7 = False
d8 = False
d9 = False
d10 = False
d11 = False
d12 = False
d13 = False
d14 = False
d15 = False
d16 = False
d17 = False
d18 = False
d19 = False
d20 = False
d21 = False
d22 = False
d23 = False
d24 = False
d25 = False
d26 = False
d27 = False
d28 = False
d29 = False
d30 = False
d31 = False
d32 = False
d33 = False
d34 = False
d35 = False
d36 = False
d37 = False
d38 = False
d39 = False
d40 = False
d41 = False
d42 = False
d43 = False
d44 = False
d45 = False
d46 = False
d47 = False
d48 = False
d49 = False
d50 = False
d51 = False
d52 = False
d53 = False
d54 = False
d55 = False
d56 = False
d57 = False
d58 = False
d59 = False
d60 = False
d61 = False
d62 = False
d63 = False
d64 = False
d65 = False
d66 = False
d67 = False
d68 = False
d69 = False
d70 = False
d71 = False
d72 = False
d73 = False
d74 = False
d75 = False
d76 = False
d77 = False
d78 = False
d79 = False
d80 = False
d81 = False
d82 = False
d83 = False
d84 = False
d85 = False
d86 = False
d87 = False
d88 = False
d89 = False
d90 = False
d91 = False
d92 = False
d93 = False
d94 = False
d95 = False
d96 = False
d97 = False
d98 = False
d99 = False
d100 = False
d101 = False
d102 = False
d103 = False
d104 = False
d105 = False
d106 = False
d107 = False
d108 = False
d109 = False
d110 = False
d111 = False
d112 = False
d113 = False
d114 = False
d115 = False
d116 = False
d117 = False
d118 = False
d119 = False
d120 = False
d121 = False
d122 = False
d123 = False
d124 = False
d125 = False
d126 = False
d127 = False
d128 = False
d129 = False
d130 = False
d131 = False
d132 = False
d133 = False
d134 = False
d135 = False
d136 = False
d137 = False
d138 = False
d139 = False
d140 = False
d141 = False
d142 = False
d143 = False
d144 = False
d145 = False
d146 = False
d147 = False
d148 = False
d149 = False
d150 = False
d151 = False
d152 = False
d153 = False
d154 = False
d155 = False
d156 = False
d157 = False
d158 = False
d159 = False
d160 = False
d161 = False
d162 = False
d163 = False
d164 = False
d165 = False
d166 = False
d167 = False
d168 = False
d169 = False
d170 = False
d171 = False
d172 = False
d173 = False
d174 = False
d175 = False
d176 = False
d177 = False
d178 = False
d179 = False
d180 = False
d181 = False
d182 = False
d183 = False
d184 = False
d185 = False
d186 = False
d187 = False
d188 = False
d189 = False
d190 = False
d191 = False
d192 = False
d193 = False
d194 = False
d195 = False
d196 = False
d197 = False
d198 = False
d199 = False
d200 = False
d201 = False
d202 = False
d203 = False
d204 = False
d205 = False
d206 = False
d207 = False
d208 = False
d209 = False
d210 = False
d211 = False
d212 = False
d213 = False
d214 = False
d215 = False
d216 = False
d217 = False
d218 = False
d219 = False
d220 = False
d221 = False
d222 = False
d223 = False
d224 = False
d225 = False
d226 = False
d227 = False
d228 = False
d229 = False
d230 = False
d231 = False
d232 = False
d233 = False
d234 = False
d235 = False
d236 = False
d237 = False
d238 = False
d239 = False
d240 = False
d241 = False
d242 = False
d243 = False
d244 = False
d245 = False
d246 = False
d247 = False
d248 = False
d249 = False
d250 = False
d251 = False
d252 = False
d253 = False
d254 = False
d255 = False
d256 = False
d257 = False
d258 = False
d259 = False
d260 = False
d261 = False
d262 = False
d263 = False
d264 = False
d265 = False
d266 = False
d267 = False
d268 = False
d269 = False
d270 = False
d271 = False
d272 = False
d273 = False
d274 = False
d275 = False
d276 = False
d277 = False
d278 = False
d279 = False
d280 = False
d281 = False
d282 = False
d283 = False
d284 = False
d285 = False
d286 = False
d287 = False
d288 = False
d289 = False
d290 = False
d291 = False
d292 = False
d293 = False
d294 = False
d295 = False
d296 = False
d297 = False
d298 = False
d299 = False
d300 = False
d301 = False
d302 = False
d303 = False
d304 = False
d305 = False
d306 = False
d307 = False
d308 = False
d309 = False
d310 = False
d311 = False
d312 = False


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

    if dot1.colliderect(pachitbox):    
        d1 = True
    if dot2.colliderect(pachitbox):
        d2 = True
    if dot3.colliderect(pachitbox):
        d3 = True
    if dot4.colliderect(pachitbox):
        d4 = True
    if dot5.colliderect(pachitbox):
        d5 = True
    if dot6.colliderect(pachitbox):
        d6 = True
    if dot7.colliderect(pachitbox):
        d7 = True
    if dot8.colliderect(pachitbox):
        d8 = True
    if dot9.colliderect(pachitbox):
        d9 = True
    if dot10.colliderect(pachitbox):
        d10 = True
    if dot11.colliderect(pachitbox):
        d11 = True
    if dot12.colliderect(pachitbox):
        d12 = True
    if dot13.colliderect(pachitbox):
        d13 = True
    if dot14.colliderect(pachitbox):
        d14 = True
    if dot15.colliderect(pachitbox):
        d15 = True
    if dot16.colliderect(pachitbox):
        d16 = True
    if dot17.colliderect(pachitbox):
        d17 = True
    if dot18.colliderect(pachitbox):
        d18 = True
    if dot19.colliderect(pachitbox):
        d19 = True
    if dot20.colliderect(pachitbox):
        d20 = True
    if dot21.colliderect(pachitbox):
        d21 = True
    if dot22.colliderect(pachitbox):
        d22 = True
    if dot23.colliderect(pachitbox):
        d23 = True
    if dot24.colliderect(pachitbox):
        d24 = True
    if dot25.colliderect(pachitbox):
        d25 = True
    if dot26.colliderect(pachitbox):
        d26 = True
    if dot27.colliderect(pachitbox):
        d27 = True
    if dot28.colliderect(pachitbox):
        d28 = True
    if dot29.colliderect(pachitbox):
        d29 = True
    if dot30.colliderect(pachitbox):
        d30 = True
    if dot31.colliderect(pachitbox):
        d31 = True
    if dot32.colliderect(pachitbox):
        d32 = True
    if dot33.colliderect(pachitbox):
        d33 = True
    if dot34.colliderect(pachitbox):
        d34 = True
    if dot35.colliderect(pachitbox):
        d35 = True
    if dot36.colliderect(pachitbox):
        d36 = True
    if dot37.colliderect(pachitbox):
        d37 = True
    if dot38.colliderect(pachitbox):
        d38 = True
    if dot39.colliderect(pachitbox):
        d39 = True
    if dot40.colliderect(pachitbox):
        d40 = True
    if dot41.colliderect(pachitbox):
        d41 = True
    if dot42.colliderect(pachitbox):
        d42 = True
    if dot43.colliderect(pachitbox):
        d43 = True
    if dot44.colliderect(pachitbox):
        d44 = True
    if dot45.colliderect(pachitbox):
        d45 = True
    if dot46.colliderect(pachitbox):
        d46 = True
    if dot47.colliderect(pachitbox):
        d47 = True
    if dot48.colliderect(pachitbox):
        d48 = True
    if dot49.colliderect(pachitbox):
        d49 = True
    if dot50.colliderect(pachitbox):
        d50 = True
    if dot51.colliderect(pachitbox):
        d51 = True
    if dot52.colliderect(pachitbox):
        d52 = True
    if dot53.colliderect(pachitbox):
        d53 = True
    if dot54.colliderect(pachitbox):
        d54 = True
    if dot55.colliderect(pachitbox):
        d55 = True
    if dot56.colliderect(pachitbox):
        d56 = True
    if dot57.colliderect(pachitbox):
        d57 = True
    if dot58.colliderect(pachitbox):
        d58 = True
    if dot59.colliderect(pachitbox):
        d59 = True
    if dot60.colliderect(pachitbox):
        d60 = True
    if dot61.colliderect(pachitbox):
        d61 = True
    if dot62.colliderect(pachitbox):
        d62 = True
    if dot63.colliderect(pachitbox):
        d63 = True
    if dot64.colliderect(pachitbox):
        d64 = True
    if dot65.colliderect(pachitbox):
        d65 = True
    if dot66.colliderect(pachitbox):
        d66 = True
    if dot67.colliderect(pachitbox):
        d67 = True
    if dot68.colliderect(pachitbox):
        d68 = True
    if dot69.colliderect(pachitbox):
        d69 = True
    if dot70.colliderect(pachitbox):
        d70 = True
    if dot71.colliderect(pachitbox):
        d71 = True
    if dot72.colliderect(pachitbox):
        d72 = True
    if dot73.colliderect(pachitbox):
        d73 = True
    if dot74.colliderect(pachitbox):
        d74 = True
    if dot75.colliderect(pachitbox):
        d75 = True
    if dot76.colliderect(pachitbox):
        d76 = True
    if dot77.colliderect(pachitbox):
        d77 = True
    if dot78.colliderect(pachitbox):
        d78 = True
    if dot79.colliderect(pachitbox):
        d79 = True
    if dot80.colliderect(pachitbox):
        d80 = True
    if dot81.colliderect(pachitbox):
        d81 = True
    if dot82.colliderect(pachitbox):
        d82 = True
    if dot83.colliderect(pachitbox):
        d83 = True
    if dot84.colliderect(pachitbox):
        d84 = True
    if dot85.colliderect(pachitbox):
        d85 = True
    if dot86.colliderect(pachitbox):
        d86 = True
    if dot87.colliderect(pachitbox):
        d87 = True
    if dot88.colliderect(pachitbox):
        d88 = True
    if dot89.colliderect(pachitbox):
        d89 = True
    if dot90.colliderect(pachitbox):
        d90 = True
    if dot91.colliderect(pachitbox):
        d91 = True
    if dot92.colliderect(pachitbox):
        d92 = True
    if dot93.colliderect(pachitbox):
        d93 = True
    if dot94.colliderect(pachitbox):
        d94 = True
    if dot95.colliderect(pachitbox):
        d95 = True
    if dot96.colliderect(pachitbox):
        d96 = True
    if dot97.colliderect(pachitbox):
        d97 = True
    if dot98.colliderect(pachitbox):
        d98 = True
    if dot99.colliderect(pachitbox):
        d99 = True
    if dot100.colliderect(pachitbox):
        d100 = True
    if dot101.colliderect(pachitbox):
        d101 = True
    if dot102.colliderect(pachitbox):
        d102 = True
    if dot103.colliderect(pachitbox):
        d103 = True
    if dot104.colliderect(pachitbox):
        d104 = True
    if dot105.colliderect(pachitbox):
        d105 = True
    if dot106.colliderect(pachitbox):
        d106 = True
    if dot107.colliderect(pachitbox):
        d107 = True
    if dot108.colliderect(pachitbox):
        d108 = True
    if dot109.colliderect(pachitbox):
        d109 = True
    if dot110.colliderect(pachitbox):
        d110 = True
    if dot111.colliderect(pachitbox):
        d111 = True
    if dot112.colliderect(pachitbox):
        d112 = True
    if dot113.colliderect(pachitbox):
        d113 = True
    if dot114.colliderect(pachitbox):
        d114 = True
    if dot115.colliderect(pachitbox):
        d115 = True
    if dot116.colliderect(pachitbox):
        d116 = True
    if dot117.colliderect(pachitbox):
        d117 = True
    if dot118.colliderect(pachitbox):
        d118 = True
    if dot119.colliderect(pachitbox):
        d119 = True
    if dot120.colliderect(pachitbox):
        d120 = True
    if dot121.colliderect(pachitbox):
        d121 = True
    if dot122.colliderect(pachitbox):
        d122 = True
    if dot123.colliderect(pachitbox):
        d123 = True
    if dot124.colliderect(pachitbox):
        d124 = True
    if dot125.colliderect(pachitbox):
        d125 = True
    if dot126.colliderect(pachitbox):
        d126 = True
    if dot127.colliderect(pachitbox):
        d127 = True
    if dot128.colliderect(pachitbox):
        d128 = True
    if dot129.colliderect(pachitbox):
        d129 = True
    if dot130.colliderect(pachitbox):
        d130 = True
    if dot131.colliderect(pachitbox):
        d131 = True
    if dot132.colliderect(pachitbox):
        d132 = True
    if dot133.colliderect(pachitbox):
        d133 = True
    if dot134.colliderect(pachitbox):
        d134 = True
    if dot135.colliderect(pachitbox):
        d135 = True
    if dot136.colliderect(pachitbox):
        d136 = True
    if dot137.colliderect(pachitbox):
        d137 = True
    if dot138.colliderect(pachitbox):
        d138 = True
    if dot139.colliderect(pachitbox):
        d139 = True
    if dot140.colliderect(pachitbox):
        d140 = True
    if dot141.colliderect(pachitbox):
        d141 = True
    if dot142.colliderect(pachitbox):
        d142 = True
    if dot143.colliderect(pachitbox):
        d143 = True
    if dot144.colliderect(pachitbox):
        d144 = True
    if dot145.colliderect(pachitbox):
        d145 = True
    if dot146.colliderect(pachitbox):
        d146 = True
    if dot147.colliderect(pachitbox):
        d147 = True
    if dot148.colliderect(pachitbox):
        d148 = True
    if dot149.colliderect(pachitbox):
        d149 = True
    if dot150.colliderect(pachitbox):
        d150 = True
    if dot151.colliderect(pachitbox):
        d151 = True
    if dot152.colliderect(pachitbox):
        d152 = True
    if dot153.colliderect(pachitbox):
        d153 = True
    if dot154.colliderect(pachitbox):
        d154 = True
    if dot155.colliderect(pachitbox):
        d155 = True
    if dot156.colliderect(pachitbox):
        d156 = True
    if dot157.colliderect(pachitbox):
        d157 = True
    if dot158.colliderect(pachitbox):
        d158 = True
    if dot159.colliderect(pachitbox):
        d159 = True
    if dot160.colliderect(pachitbox):
        d160 = True
    if dot161.colliderect(pachitbox):
        d161 = True
    if dot162.colliderect(pachitbox):
        d162 = True
    if dot163.colliderect(pachitbox):
        d163 = True
    if dot164.colliderect(pachitbox):
        d164 = True
    if dot165.colliderect(pachitbox):
        d165 = True
    if dot166.colliderect(pachitbox):
        d166 = True
    if dot167.colliderect(pachitbox):
        d167 = True
    if dot168.colliderect(pachitbox):
        d168 = True
    if dot169.colliderect(pachitbox):
        d169 = True
    if dot170.colliderect(pachitbox):
        d170 = True
    if dot171.colliderect(pachitbox):
        d171 = True
    if dot172.colliderect(pachitbox):
        d172 = True
    if dot173.colliderect(pachitbox):
        d173 = True
    if dot174.colliderect(pachitbox):
        d174 = True
    if dot175.colliderect(pachitbox):
        d175 = True
    if dot176.colliderect(pachitbox):
        d176 = True
    if dot177.colliderect(pachitbox):
        d177 = True
    if dot178.colliderect(pachitbox):
        d178 = True
    if dot179.colliderect(pachitbox):
        d179 = True
    if dot180.colliderect(pachitbox):
        d180 = True
    if dot181.colliderect(pachitbox):
        d181 = True
    if dot182.colliderect(pachitbox):
        d182 = True
    if dot183.colliderect(pachitbox):
        d183 = True
    if dot184.colliderect(pachitbox):
        d184 = True
    if dot185.colliderect(pachitbox):
        d185 = True
    if dot186.colliderect(pachitbox):
        d186 = True
    if dot187.colliderect(pachitbox):
        d187 = True
    if dot188.colliderect(pachitbox):
        d188 = True
    if dot189.colliderect(pachitbox):
        d189 = True
    if dot190.colliderect(pachitbox):
        d190 = True
    if dot191.colliderect(pachitbox):
        d191 = True
    if dot192.colliderect(pachitbox):
        d192 = True
    if dot193.colliderect(pachitbox):
        d193 = True
    if dot194.colliderect(pachitbox):
        d194 = True
    if dot195.colliderect(pachitbox):
        d195 = True
    if dot196.colliderect(pachitbox):
        d196 = True
    if dot197.colliderect(pachitbox):
        d197 = True
    if dot198.colliderect(pachitbox):
        d198 = True
    if dot199.colliderect(pachitbox):
        d199 = True
    if dot200.colliderect(pachitbox):
        d200 = True
    if dot201.colliderect(pachitbox):
        d201 = True
    if dot202.colliderect(pachitbox):
        d202 = True
    if dot203.colliderect(pachitbox):
        d203 = True
    if dot204.colliderect(pachitbox):
        d204 = True
    if dot205.colliderect(pachitbox):
        d205 = True
    if dot206.colliderect(pachitbox):
        d206 = True
    if dot207.colliderect(pachitbox):
        d207 = True
    if dot208.colliderect(pachitbox):
        d208 = True
    if dot209.colliderect(pachitbox):
        d209 = True
    if dot210.colliderect(pachitbox):
        d210 = True
    if dot211.colliderect(pachitbox):
        d211 = True
    if dot212.colliderect(pachitbox):
        d212 = True
    if dot213.colliderect(pachitbox):
        d213 = True
    if dot214.colliderect(pachitbox):
        d214 = True
    if dot215.colliderect(pachitbox):
        d215 = True
    if dot216.colliderect(pachitbox):
        d216 = True
    if dot217.colliderect(pachitbox):
        d217 = True
    if dot218.colliderect(pachitbox):
        d218 = True
    if dot219.colliderect(pachitbox):
        d219 = True
    if dot220.colliderect(pachitbox):
        d220 = True
    if dot221.colliderect(pachitbox):
        d221 = True
    if dot222.colliderect(pachitbox):
        d222 = True
    if dot223.colliderect(pachitbox):
        d223 = True
    if dot224.colliderect(pachitbox):
        d224 = True
    if dot225.colliderect(pachitbox):
        d225 = True
    if dot226.colliderect(pachitbox):
        d226 = True
    if dot227.colliderect(pachitbox):
        d227 = True
    if dot228.colliderect(pachitbox):
        d228 = True
    if dot229.colliderect(pachitbox):
        d229 = True
    if dot230.colliderect(pachitbox):
        d230 = True
    if dot231.colliderect(pachitbox):
        d231 = True
    if dot232.colliderect(pachitbox):
        d232 = True
    if dot233.colliderect(pachitbox):
        d233 = True
    if dot234.colliderect(pachitbox):
        d234 = True
    if dot235.colliderect(pachitbox):
        d235 = True
    if dot236.colliderect(pachitbox):
        d236 = True
    if dot237.colliderect(pachitbox):
        d237 = True
    if dot238.colliderect(pachitbox):
        d238 = True
    if dot239.colliderect(pachitbox):
        d239 = True
    if dot240.colliderect(pachitbox):
        d240 = True
    if dot241.colliderect(pachitbox):
        d241 = True
    if dot242.colliderect(pachitbox):
        d242 = True
    if dot243.colliderect(pachitbox):
        d243 = True
    if dot244.colliderect(pachitbox):
        d244 = True
    if dot245.colliderect(pachitbox):
        d245 = True
    if dot246.colliderect(pachitbox):
        d246 = True
    if dot247.colliderect(pachitbox):
        d247 = True
    if dot248.colliderect(pachitbox):
        d248 = True
    if dot249.colliderect(pachitbox):
        d249 = True
    if dot250.colliderect(pachitbox):
        d250 = True
    if dot251.colliderect(pachitbox):
        d251 = True
    if dot252.colliderect(pachitbox):
        d252 = True
    if dot253.colliderect(pachitbox):
        d253 = True
    if dot254.colliderect(pachitbox):
        d254 = True
    if dot255.colliderect(pachitbox):
        d255 = True
    if dot256.colliderect(pachitbox):
        d256 = True
    if dot257.colliderect(pachitbox):
        d257 = True
    if dot258.colliderect(pachitbox):
        d258 = True
    if dot259.colliderect(pachitbox):
        d259 = True
    if dot260.colliderect(pachitbox):
        d260 = True
    if dot261.colliderect(pachitbox):
        d261 = True
    if dot262.colliderect(pachitbox):
        d262 = True
    if dot263.colliderect(pachitbox):
        d263 = True
    if dot264.colliderect(pachitbox):
        d264 = True
    if dot265.colliderect(pachitbox):
        d265 = True
    if dot266.colliderect(pachitbox):
        d266 = True
    if dot267.colliderect(pachitbox):
        d267 = True
    if dot268.colliderect(pachitbox):
        d268 = True
    if dot269.colliderect(pachitbox):
        d269 = True
    if dot270.colliderect(pachitbox):
        d270 = True
    if dot271.colliderect(pachitbox):
        d271 = True
    if dot272.colliderect(pachitbox):
        d272 = True
    if dot273.colliderect(pachitbox):
        d273 = True
    if dot274.colliderect(pachitbox):
        d274 = True
    if dot275.colliderect(pachitbox):
        d275 = True
    if dot276.colliderect(pachitbox):
        d276 = True
    if dot277.colliderect(pachitbox):
        d277 = True
    if dot278.colliderect(pachitbox):
        d278 = True
    if dot279.colliderect(pachitbox):
        d279 = True
    if dot280.colliderect(pachitbox):
        d280 = True
    if dot281.colliderect(pachitbox):
        d281 = True
    if dot282.colliderect(pachitbox):
        d282 = True
    if dot283.colliderect(pachitbox):
        d283 = True
    if dot284.colliderect(pachitbox):
        d284 = True
    if dot285.colliderect(pachitbox):
        d285 = True
    if dot286.colliderect(pachitbox):
        d286 = True
    if dot287.colliderect(pachitbox):
        d287 = True
    if dot288.colliderect(pachitbox):
        d288 = True
    if dot289.colliderect(pachitbox):
        d289 = True
    if dot290.colliderect(pachitbox):
        d290 = True
    if dot291.colliderect(pachitbox):
        d291 = True
    if dot292.colliderect(pachitbox):
        d292 = True
    if dot293.colliderect(pachitbox):
        d293 = True
    if dot294.colliderect(pachitbox):
        d294 = True
    if dot295.colliderect(pachitbox):
        d295 = True
    if dot296.colliderect(pachitbox):
        d296 = True
    if dot297.colliderect(pachitbox):
        d297 = True
    if dot298.colliderect(pachitbox):
        d298 = True
    if dot299.colliderect(pachitbox):
        d299 = True
    if dot300.colliderect(pachitbox):
        d300 = True
    if dot301.colliderect(pachitbox):
        d301 = True
    if dot302.colliderect(pachitbox):
        d302 = True
    if dot303.colliderect(pachitbox):
        d303 = True
    if dot304.colliderect(pachitbox):
        d304 = True
    if dot305.colliderect(pachitbox):
        d305 = True
    if dot306.colliderect(pachitbox):
        d306 = True
    if dot307.colliderect(pachitbox):
        d307 = True
    if dot308.colliderect(pachitbox):
        d308 = True
    if dot309.colliderect(pachitbox):
        d309 = True
    if dot310.colliderect(pachitbox):
        d310 = True
    if dot311.colliderect(pachitbox):
        d311 = True
    if dot312.colliderect(pachitbox):
        d312 = True



    PAC = pygame.transform.flip(img_copy, flip, flip2)


    # RENDER GAME HERE
    win.blit(PAC, (pac_pos.x - 20, pac_pos.y - 20))

    win.blit(ghostB, (ghostB_pos.x - 20, ghostB_pos.y - 20))

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
    
    if d1 == False:
        pygame.draw.rect(win, "green", (500, 400, 10, 10)) #hp
    if d2 == False:
        pygame.draw.rect(win, "orange", (535, 400, 10, 10))
    if d3 == False:
        pygame.draw.rect(win, "green", (570, 400, 10, 10)) #hp
    if d4 == False:
        pygame.draw.rect(win, "orange", (570, 435, 10, 10))
    if d5 == False:
        pygame.draw.rect(win, "orange", (570, 470, 10, 10))
    if d6 == False:
        pygame.draw.rect(win, "orange", (570, 505, 10, 10))
    if d7 == False:
        pygame.draw.rect(win, "green", (570, 540, 10, 10)) #hp
    if d8 == False:
        pygame.draw.rect(win, "orange", (570, 575, 10, 10))
    if d9 == False:
        pygame.draw.rect(win, "orange", (570, 610, 10, 10))
    if d10 == False:
        pygame.draw.rect(win, "green", (570, 645, 10, 10)) #hp
    if d11 == False:
        pygame.draw.rect(win, "orange", (570, 680, 10, 10))
    if d12 == False:
        pygame.draw.rect(win, "orange", (570, 715, 10, 10))
    if d13 == False:
        pygame.draw.rect(win, "orange", (570, 750, 10, 10))
    if d14 == False:
        pygame.draw.rect(win, "green", (570, 785, 10, 10)) #hp
    if d15 == False:
        pygame.draw.rect(win, "orange", (570, 820, 10, 10))
    if d16 == False:
        pygame.draw.rect(win, "green", (570, 860, 10, 10)) #hp
    if d17 == False:
        pygame.draw.rect(win, "orange", (605, 860, 10, 10))
    if d18 == False:
        pygame.draw.rect(win, "orange", (640, 860, 10, 10))
    if d19 == False:
        pygame.draw.rect(win, "orange", (675, 860, 10, 10))
    if d20 == False:
        pygame.draw.rect(win, "orange", (710, 860, 10, 10))
    if d21 == False:
        pygame.draw.rect(win, "green", (750, 860, 10, 10)) #hp`
    if d22 == False:
        pygame.draw.rect(win, "orange", (750, 895, 10, 10))
    if d23 == False:
        pygame.draw.rect(win, "green", (750, 930, 10, 10)) #hp
    if d24 == False:
        pygame.draw.rect(win, "orange", (500, 365, 10, 10))
    if d25 == False:
        pygame.draw.rect(win, "orange", (500, 330, 10, 10))
    if d26 == False:
        pygame.draw.rect(win, "orange", (500, 295, 10, 10))
    if d27 == False:
        pygame.draw.rect(win, "orange", (500, 265, 10, 10))
    if d28 == False:
        pygame.draw.rect(win, "orange", (500, 230, 10, 10))
    if d29 == False:
        pygame.draw.rect(win, "orange", (500, 200, 10, 10))
    if d30 == False:
        pygame.draw.rect(win, "orange", (500, 170, 10, 10))
    if d31 == False:
        pygame.draw.rect(win, "green", (500, 140, 10, 10)) #hp
    if d32 == False:
        pygame.draw.rect(win, "orange", (500, 435, 10, 10))
    if d33 == False:
        pygame.draw.rect(win, "orange", (500, 470, 10, 10))
    if d34 == False:
        pygame.draw.rect(win, "orange", (500, 505, 10, 10))
    if d35 == False:
        pygame.draw.rect(win, "orange", (500, 540, 10, 10))
    if d36 == False:
        pygame.draw.rect(win, "orange", (500, 575, 10, 10))
    if d37 == False:
        pygame.draw.rect(win, "orange", (500, 610, 10, 10))
    if d38 == False:
        pygame.draw.rect(win, "green", (500, 645, 10, 10)) #hp
    if d39 == False:
        pygame.draw.rect(win, "orange", (500, 680, 10, 10))
    if d40 == False:
        pygame.draw.rect(win, "orange", (500, 715, 10, 10))
    if d41 == False:
        pygame.draw.rect(win, "orange", (500, 750, 10, 10))
    if d42 == False:
        pygame.draw.rect(win, "orange", (535, 655, 10, 10))
    if d43 == False:
        pygame.draw.rect(win, "orange", (500, 785, 10, 10))
    if d44 == False:
        pygame.draw.rect(win, "orange", (500, 820, 10, 10))
    if d45 == False:
        pygame.draw.rect(win, "orange", (500, 855, 10, 10))
    if d46 == False:
        pygame.draw.rect(win, "orange", (500, 890, 10, 10))
    if d47 == False:
        pygame.draw.rect(win, "green", (500, 930, 10, 10)) #hp
    if d48 == False:
        pygame.draw.rect(win, "orange", (535, 930, 10, 10))
    if d49 == False:
        pygame.draw.rect(win, "orange", (570, 930, 10, 10))
    if d50 == False:
        pygame.draw.rect(win, "orange", (605, 930, 10, 10))
    if d51 == False:
        pygame.draw.rect(win, "orange", (640, 930, 10, 10))
    if d52 == False:
        pygame.draw.rect(win, "orange", (675, 930, 10, 10))
    if d53 == False:
        pygame.draw.rect(win, "orange", (710, 930, 10, 10))
    if d54 == False:
        pygame.draw.rect(win, "orange", (785, 930, 10, 10))
    if d55 == False:
        pygame.draw.rect(win, "orange", (820, 930, 10, 10))
    if d56 == False:
        pygame.draw.rect(win, "orange", (855, 930, 10, 10))
    if d57 == False:
        pygame.draw.rect(win, "orange", (890, 930, 10, 10))
    if d58 == False:
        pygame.draw.rect(win, "green", (930, 930, 10, 10)) #hp
    if d59 == False:
        pygame.draw.rect(win, "orange", (930, 895, 10, 10))
    if d60 == False:
        pygame.draw.rect(win, "orange", (930, 860, 10, 10))
    if d61 == False:
        pygame.draw.rect(win, "orange", (930, 825, 10, 10))
    if d62 == False:
        pygame.draw.rect(win, "orange", (930, 790, 10, 10))
    if d63 == False:
        pygame.draw.rect(win, "orange", (895, 860, 10, 10))
    if d64 == False:
        pygame.draw.rect(win, "orange", (860, 860, 10, 10))
    if d65 == False:
        pygame.draw.rect(win, "orange", (825, 860, 10, 10))
    if d66 == False:    
        pygame.draw.rect(win, "orange", (790, 860, 10, 10))
    if d67 == False:
        pygame.draw.rect(win, "orange", (860, 790, 10, 10))
    if d68 == False:
        pygame.draw.rect(win, "orange", (825, 790, 10, 10))
    if d69 == False:
        pygame.draw.rect(win, "orange", (895, 790, 10, 10))
    if d70 == False:
        pygame.draw.rect(win, "orange", (780, 790, 10, 10))
    if d71 == False:
        pygame.draw.rect(win, "orange", (780, 755, 10, 10))
    if d72 == False:
        pygame.draw.rect(win, "orange", (780, 720, 10, 10))
    if d73 == False:
        pygame.draw.rect(win, "orange", (780, 685, 10, 10))
    if d74 == False:
        pygame.draw.rect(win, "orange", (780, 650, 10, 10))
    if d75 == False:
        pygame.draw.rect(win, "orange", (780, 615, 10, 10))
    if d76 == False:    
        pygame.draw.rect(win, "orange", (780, 580, 10, 10))
    if d77 == False:
        pygame.draw.rect(win, "orange", (780, 545, 10, 10))
    if d78 == False:
        pygame.draw.rect(win, "orange", (780, 510, 10, 10))
    if d79 == False:
        pygame.draw.rect(win, "orange", (780, 475, 10, 10))
    if d80 == False:
        pygame.draw.rect(win, "orange", (780, 440, 10, 10))
    if d81 == False:
        pygame.draw.rect(win, "orange", (780, 405, 10, 10))
    if d82 == False:
        pygame.draw.rect(win, "orange", (780, 365, 10, 10))
    if d83 == False:
        pygame.draw.rect(win, "orange", (780, 325, 10, 10))
    if d84 == False:
        pygame.draw.rect(win, "orange", (780, 280, 10, 10))
    if d85 == False:
        pygame.draw.rect(win, "orange", (780, 210, 10, 10))
    if d86 == False:
        pygame.draw.rect(win, "orange", (535, 140, 10, 10))
    if d87 == False:
        pygame.draw.rect(win, "orange", (570, 140, 10, 10))
    if d88 == False:
        pygame.draw.rect(win, "orange", (605, 140, 10, 10))
    if d89 == False:
        pygame.draw.rect(win, "orange", (640, 140, 10, 10))
    if d90 == False:
        pygame.draw.rect(win, "orange", (675, 140, 10, 10))
    if d91 == False:
        pygame.draw.rect(win, "orange", (710, 140, 10, 10))
    if d92 == False:
        pygame.draw.rect(win, "orange", (785, 140, 10, 10))
    if d93 == False:
        pygame.draw.rect(win, "orange", (820, 140, 10, 10))
    if d94 == False:
        pygame.draw.rect(win, "orange", (855, 140, 10, 10))
    if d95 == False:
        pygame.draw.rect(win, "orange", (890, 140, 10, 10))
    if d96 == False:
        pygame.draw.rect(win, "orange", (930, 140, 10, 10))
    if d97 == False:
        pygame.draw.rect(win, "orange", (750, 140, 10, 10))
    if d98 == False:
        pygame.draw.rect(win, "green", (1000, 140, 10, 10))#hp
    if d99 == False:
        pygame.draw.rect(win, "orange", (1035, 140, 10, 10))
    if d100 == False:
        pygame.draw.rect(win, "orange", (1070, 140, 10, 10))
    if d101 == False:
        pygame.draw.rect(win, "orange", (1105, 140, 10, 10))
    if d102 == False:
        pygame.draw.rect(win, "orange", (1140, 140, 10, 10))
    if d103 == False:
        pygame.draw.rect(win, "orange", (1180, 140, 10, 10))
    if d104 == False:
        pygame.draw.rect(win, "orange", (1210, 140, 10, 10))
    if d105 == False:
        pygame.draw.rect(win, "orange", (1245, 140, 10, 10))
    if d106 == False:
        pygame.draw.rect(win, "orange", (1280, 140, 10, 10))
    if d107 == False:
        pygame.draw.rect(win, "orange", (1315, 140, 10, 10))
    if d108 == False:
        pygame.draw.rect(win, "orange", (1350, 140, 10, 10))
    if d109 == False:
        pygame.draw.rect(win, "orange", (1385, 140, 10, 10))
    if d110 == False:
        pygame.draw.rect(win, "orange", (1430, 140, 10, 10))
    if d111 == False:
        pygame.draw.rect(win, "orange", (1180, 175, 10, 10))
    if d112 == False:
        pygame.draw.rect(win, "orange", (1180, 210, 10, 10))
    if d113 == False:
        pygame.draw.rect(win, "orange", (1000, 175, 10, 10))
    if d114 == False:
        pygame.draw.rect(win, "orange", (1000, 210, 10, 10))
    if d115 == False:
        pygame.draw.rect(win, "orange", (1000, 245, 10, 10))
    if d116 == False:
        pygame.draw.rect(win, "orange", (1035, 280, 10, 10))
    if d117 == False:
        pygame.draw.rect(win, "orange", (1070, 280, 10, 10))
    if d118 == False:
        pygame.draw.rect(win, "orange", (1105, 280, 10, 10))
    if d119 == False:
        pygame.draw.rect(win, "orange", (825, 280, 10, 10))
    if d120 == False:
        pygame.draw.rect(win, "orange", (860, 280, 10, 10))
    if d121 == False:
        pygame.draw.rect(win, "orange", (895, 280, 10, 10))
    if d122 == False:
        pygame.draw.rect(win, "green", (930, 280, 10, 10))#hp
    if d123 == False:
        pygame.draw.rect(win, "green", (570, 280, 10, 10))#hp
    if d124 == False:
        pygame.draw.rect(win, "orange", (605, 280, 10, 10))
    if d125 == False:
        pygame.draw.rect(win, "orange", (640, 280, 10, 10))
    if d126 == False:
        pygame.draw.rect(win, "orange", (675, 280, 10, 10))
    if d127 == False:
        pygame.draw.rect(win, "green", (710, 280, 10, 10))#hp
    if d128 == False:
        pygame.draw.rect(win, "orange", (710, 315, 10, 10))
    if d129 == False:
        pygame.draw.rect(win, "green", (710, 350, 10, 10))#hp
    if d130 == False:
        pygame.draw.rect(win, "orange", (710, 385, 10, 10))
    if d131 == False:
        pygame.draw.rect(win, "orange", (710, 420, 10, 10))
    if d132 == False:
        pygame.draw.rect(win, "green", (710, 455, 10, 10))#hp
    if d133 == False:
        pygame.draw.rect(win, "orange", (745, 455, 10, 10))
    if d134 == False:
        pygame.draw.rect(win, "orange", (710, 490, 10, 10))
    if d135 == False:
        pygame.draw.rect(win, "orange", (710, 525, 10, 10))
    if d136 == False:
        pygame.draw.rect(win, "orange", (710, 560, 10, 10))
    if d137 == False:
        pygame.draw.rect(win, "green", (710, 595, 10, 10))#hp
    if d138 == False:
        pygame.draw.rect(win, "orange", (745, 595, 10, 10))
    if d139 == False:
        pygame.draw.rect(win, "orange", (710, 630, 10, 10))
    if d140 == False:
        pygame.draw.rect(win, "orange", (710, 665, 10, 10))
    if d141 == False:
        pygame.draw.rect(win, "green", (710, 715, 10, 10))#hp
    if d142 == False:
        pygame.draw.rect(win, "orange", (675, 715, 10, 10))
    if d143 == False:
        pygame.draw.rect(win, "green", (640, 715, 10, 10))#hp
    if d144 == False:
        pygame.draw.rect(win, "orange", (640, 680, 10, 10))
    if d145 == False:
        pygame.draw.rect(win, "orange", (640, 645, 10, 10))
    if d146 == False:
        pygame.draw.rect(win, "orange", (640, 610, 10, 10))
    if d147 == False:
        pygame.draw.rect(win, "orange", (640, 575, 10, 10))
    if d148 == False:
        pygame.draw.rect(win, "green", (640, 540, 10, 10))#hp
    if d149 == False:
        pygame.draw.rect(win, "orange", (605, 540, 10, 10))
    if d150 == False:    
        pygame.draw.rect(win, "orange", (640, 500, 10, 10))
    if d151 == False:
        pygame.draw.rect(win, "orange", (640, 460, 10, 10))
    if d152 == False:
        pygame.draw.rect(win, "orange", (640, 425, 10, 10))
    if d153 == False:
        pygame.draw.rect(win, "orange", (640, 390, 10, 10))
    if d154 == False:
        pygame.draw.rect(win, "green", (640, 350, 10, 10))#hp
    if d155 == False:
        pygame.draw.rect(win, "orange", (675, 350, 10, 10))
    if d156 == False:
        pygame.draw.rect(win, "orange", (710, 750, 10, 10))
    if d157 == False:
        pygame.draw.rect(win, "green", (710, 790, 10, 10))#hp
    if d158 == False:
        pygame.draw.rect(win, "orange", (675, 790, 10, 10))
    if d159 == False:
        pygame.draw.rect(win, "orange", (640, 790, 10, 10))
    if d160 == False:
        pygame.draw.rect(win, "orange", (605, 790, 10, 10))
    if d161 == False:
        pygame.draw.rect(win, "orange", (570, 315, 10, 10))
    if d162 == False:
        pygame.draw.rect(win, "orange", (570, 350, 10, 10))
    if d163 == False:
        pygame.draw.rect(win, "orange", (570, 245, 10, 10))
    if d164 == False:
        pygame.draw.rect(win, "green", (570, 210, 10, 10))#hp
    if d165 == False:
        pygame.draw.rect(win, "orange", (605, 210, 10, 10))
    if d166 == False:
        pygame.draw.rect(win, "orange", (640, 210, 10, 10))
    if d167 == False:
        pygame.draw.rect(win, "orange", (675, 210, 10, 10))
    if d168 == False:
        pygame.draw.rect(win, "orange", (710, 210, 10, 10))
    if d169 == False:
        pygame.draw.rect(win, "green", (750, 210, 10, 10))#hp
    if d170 == False:
        pygame.draw.rect(win, "orange", (815, 210, 10, 10))
    if d171 == False:
        pygame.draw.rect(win, "orange", (850, 210, 10, 10))
    if d172 == False:       
        pygame.draw.rect(win, "orange", (885, 210, 10, 10))
    if d173 == False:
        pygame.draw.rect(win, "green", (930, 210, 10, 10))#hp
    if d174 == False:    
        pygame.draw.rect(win, "orange", (930, 175, 10, 10))
    if d175 == False:
        pygame.draw.rect(win, "orange", (930, 245, 10, 10))
    if d176 == False:
        pygame.draw.rect(win, "orange", (750, 175, 10, 10))
    if d177 == False:
        pygame.draw.rect(win, "orange", (1000, 280, 10, 10))
    if d178 == False:
        pygame.draw.rect(win, "orange", (1035, 210, 10, 10))
    if d179 == False:
        pygame.draw.rect(win, "orange", (1070, 210, 10, 10))
    if d180 == False:
        pygame.draw.rect(win, "orange", (1105, 210, 10, 10))
    if d181 == False:
        pygame.draw.rect(win, "orange", (1210, 210, 10, 10))
    if d182 == False:
        pygame.draw.rect(win, "orange", (1245, 210, 10, 10))
    if d183 == False:
        pygame.draw.rect(win, "orange", (1280, 210, 10, 10))
    if d184 == False:
        pygame.draw.rect(win, "orange", (1140, 210, 10, 10))
    if d185 == False:
        pygame.draw.rect(win, "orange", (1315, 210, 10, 10))
    if d186 == False:
        pygame.draw.rect(win, "orange", (1430, 175, 10, 10))
    if d187 == False:
        pygame.draw.rect(win, "orange", (1430, 210, 10, 10))
    if d188 == False:
        pygame.draw.rect(win, "orange", (1430, 365, 10, 10))
    if d189 == False:
        pygame.draw.rect(win, "orange", (1430, 295, 10, 10))
    if d190 == False:
        pygame.draw.rect(win, "orange", (1430, 265, 10, 10))
    if d191 == False:
        pygame.draw.rect(win, "orange", (1430, 325, 10, 10))
    if d192 == False:
        pygame.draw.rect(win, "green", (1430, 395, 10, 10))
    if d193 == False:
        pygame.draw.rect(win, "orange", (1395, 395, 10, 10))
    if d194 == False:
        pygame.draw.rect(win, "green", (1360, 395, 10, 10))
    if d195 == False:
        pygame.draw.rect(win, "orange", (1430, 235, 10, 10))
    if d196 == False:
        pygame.draw.rect(win, "orange", (1430, 210, 10, 10))
    if d197 == False:
        pygame.draw.rect(win, "orange", (1430, 435, 10, 10))
    if d198 == False:
        pygame.draw.rect(win, "orange", (1430, 470, 10, 10))
    if d199 == False:
        pygame.draw.rect(win, "orange", (1430, 505, 10, 10))
    if d200 == False:
        pygame.draw.rect(win, "orange", (1430, 505, 10, 10))
    if d201 == False:
        pygame.draw.rect(win, "orange", (1430, 540, 10, 10))
    if d202 == False:
        pygame.draw.rect(win, "orange", (1430, 575, 10, 10))
    if d203 == False:
        pygame.draw.rect(win, "orange", (1430, 610, 10, 10))
    if d204 == False:
        pygame.draw.rect(win, "orange", (1430, 645, 10, 10))
    if d205 == False:
        pygame.draw.rect(win, "orange", (1430, 680, 10, 10))
    if d206 == False:
        pygame.draw.rect(win, "orange", (1430, 715, 10, 10))
    if d207 == False:
        pygame.draw.rect(win, "orange", (1430, 750, 10, 10))
    if d208 == False:
        pygame.draw.rect(win, "orange", (1395, 655, 10, 10))
    if d209 == False:
        pygame.draw.rect(win, "orange", (1430, 785, 10, 10))
    if d210 == False:
        pygame.draw.rect(win, "orange", (1430, 820, 10, 10))
    if d211 == False:
        pygame.draw.rect(win, "orange", (1430, 855, 10, 10))
    if d212 == False:
        pygame.draw.rect(win, "orange", (1430, 890, 10, 10))
    if d213 == False:
        pygame.draw.rect(win, "green", (1430, 930, 10, 10))
    if d214 == False:
        pygame.draw.rect(win, "orange", (1360, 435, 10, 10))
    if d215 == False:
        pygame.draw.rect(win, "orange", (1360, 470, 10, 10))
    if d216 == False:
        pygame.draw.rect(win, "orange", (1360, 505, 10, 10))
    if d217 == False:
        pygame.draw.rect(win, "green", (1360, 540, 10, 10)) #hp
    if d218 == False:
        pygame.draw.rect(win, "orange", (1360, 575, 10, 10))
    if d219 == False:
        pygame.draw.rect(win, "orange", (1360, 610, 10, 10))
    if d220 == False:
        pygame.draw.rect(win, "green", (1360, 645, 10, 10)) #hp
    if d221 == False:
        pygame.draw.rect(win, "orange", (1360, 680, 10, 10))
    if d222 == False:
        pygame.draw.rect(win, "orange", (1360, 715, 10, 10))
    if d223 == False:
        pygame.draw.rect(win, "orange", (1360, 750, 10, 10))
    if d224 == False:
        pygame.draw.rect(win, "green", (1360, 785, 10, 10)) #hp
    if d225 == False:
        pygame.draw.rect(win, "orange", (1360, 820, 10, 10))
    if d226 == False:
        pygame.draw.rect(win, "green", (1360, 860, 10, 10)) #hp
    if d227 == False:
        pygame.draw.rect(win, "green", (1150, 790, 10, 10))
    if d228 == False:
        pygame.draw.rect(win, "orange", (1150, 755, 10, 10))
    if d229 == False:
        pygame.draw.rect(win, "orange", (1150, 720, 10, 10))
    if d230 == False:
        pygame.draw.rect(win, "orange", (1150, 685, 10, 10))
    if d231 == False:
        pygame.draw.rect(win, "orange", (1150, 650, 10, 10))
    if d232 == False:
        pygame.draw.rect(win, "orange", (1150, 615, 10, 10))
    if d233 == False:
        pygame.draw.rect(win, "orange", (1150, 580, 10, 10))
    if d234 == False:
        pygame.draw.rect(win, "orange", (1150, 545, 10, 10))
    if d235 == False:
        pygame.draw.rect(win, "orange", (1150, 510, 10, 10))
    if d236 == False:
        pygame.draw.rect(win, "orange", (1150, 475, 10, 10))
    if d237 == False:
        pygame.draw.rect(win, "orange", (1150, 440, 10, 10))
    if d238 == False:
        pygame.draw.rect(win, "orange", (1150, 405, 10, 10))
    if d239 == False:
        pygame.draw.rect(win, "orange", (1150, 365, 10, 10))
    if d240 == False:
        pygame.draw.rect(win, "orange", (1150, 325, 10, 10))
    if d241 == False:
        pygame.draw.rect(win, "green", (1150, 280, 10, 10))#hp
    if d242 == False:
        pygame.draw.rect(win, "green", (1220, 280, 10, 10))#hp
    if d243 == False:
        pygame.draw.rect(win, "orange", (1255, 280, 10, 10))
    if d244 == False:
        pygame.draw.rect(win, "orange", (1290, 280, 10, 10))
    if d245 == False:
        pygame.draw.rect(win, "orange", (1325, 280, 10, 10))
    if d246 == False:
        pygame.draw.rect(win, "green", (1360, 280, 10, 10))#hp
    if d247 == False:
        pygame.draw.rect(win, "orange", (1360, 245, 10, 10))
    if d248 == False:
        pygame.draw.rect(win, "green", (1360, 210, 10, 10))#hp
    if d249 == False:
        pygame.draw.rect(win, "orange", (1360, 315, 10, 10))
    if d250 == False:
        pygame.draw.rect(win, "orange", (1360, 350, 10, 10))
    if d251 == False:
        pygame.draw.rect(win, "orange", (1220, 315, 10, 10))
    if d252 == False:
        pygame.draw.rect(win, "orange", (1220, 350, 10, 10))
    if d253 == False:
        pygame.draw.rect(win, "orange", (1220, 385, 10, 10))
    if d254 == False:
        pygame.draw.rect(win, "orange", (1220, 420, 10, 10))
    if d255 == False:
        pygame.draw.rect(win, "green", (1220, 455, 10, 10))#hp
    if d256 == False:
        pygame.draw.rect(win, "orange", (1220, 490, 10, 10))
    if d257 == False:
        pygame.draw.rect(win, "orange", (1185, 455, 10, 10))
    if d258 == False:
        pygame.draw.rect(win, "orange", (1220, 525, 10, 10))
    if d259 == False:
        pygame.draw.rect(win, "orange", (1220, 560, 10, 10))
    if d260 == False:
        pygame.draw.rect(win, "green", (1220, 595, 10, 10))#hp
    if d261 == False:
        pygame.draw.rect(win, "orange", (1185, 595, 10, 10))
    if d262 == False:
        pygame.draw.rect(win, "orange", (1220, 630, 10, 10))
    if d263 == False:
        pygame.draw.rect(win, "orange", (1220, 675, 10, 10))
    if d264 == False:
        pygame.draw.rect(win, "green", (1220, 715, 10, 10))#hp
    if d265 == False:
        pygame.draw.rect(win, "orange", (1255, 715, 10, 10))
    if d266 == False:
        pygame.draw.rect(win, "green", (1290, 715, 10, 10))#hp
    if d267 == False:
        pygame.draw.rect(win, "green", (1290, 350, 10, 10))#hp
    if d268 == False:
        pygame.draw.rect(win, "orange", (1255, 350, 10, 10))
    if d269 == False:
        pygame.draw.rect(win, "orange", (1290, 385, 10, 10))
    if d270 == False:
        pygame.draw.rect(win, "orange", (1290, 420, 10, 10))
    if d271 == False:
        pygame.draw.rect(win, "orange", (1290, 455, 10, 10))
    if d272 == False:
        pygame.draw.rect(win, "orange", (1290, 490, 10, 10))
    if d273 == False:
        pygame.draw.rect(win, "green", (1290, 525, 10, 10))#hp
    if d274 == False:
        pygame.draw.rect(win, "orange", (1325, 525, 10, 10))
    if d275 == False:
        pygame.draw.rect(win, "orange", (1290, 560, 10, 10))
    if d276 == False:
        pygame.draw.rect(win, "orange", (1290, 595, 10, 10))
    if d277 == False:
        pygame.draw.rect(win, "orange", (1290, 630, 10, 10))
    if d278 == False:
        pygame.draw.rect(win, "orange", (1290, 675, 10, 10))
    if d279 == False:
        pygame.draw.rect(win, "orange", (1220, 750, 10, 10))
    if d280 == False:
        pygame.draw.rect(win, "green", (1220, 785, 10, 10))#hp
    if d281 == False:
        pygame.draw.rect(win, "orange", (1255, 785, 10, 10))
    if d282 == False:
        pygame.draw.rect(win, "orange", (1290, 785, 10, 10))
    if d283 == False:
        pygame.draw.rect(win, "orange", (1325, 785, 10, 10))
    if d284 == False:
        pygame.draw.rect(win, "orange", (1325, 860, 10, 10))
    if d285 == False:
        pygame.draw.rect(win, "orange", (1290, 860, 10, 10))
    if d286 == False:
        pygame.draw.rect(win, "orange", (1255, 860, 10, 10))
    if d287 == False:
        pygame.draw.rect(win, "orange", (1220, 860, 10, 10))
    if d288 == False:
        pygame.draw.rect(win, "green", (1185, 860, 10, 10))#hp
    if d289 == False:
        pygame.draw.rect(win, "orange", (1150, 860, 10, 10))
    if d290 == False:
        pygame.draw.rect(win, "orange", (1115, 860, 10, 10))
    if d291 == False:
        pygame.draw.rect(win, "orange", (1075, 860, 10, 10))
    if d292 == False:
        pygame.draw.rect(win, "orange", (1040, 860, 10, 10))
    if d293 == False:
        pygame.draw.rect(win, "green", (1000, 860, 10, 10))#hp
    if d294 == False:
        pygame.draw.rect(win, "orange", (1000, 825, 10, 10))
    if d295 == False:
        pygame.draw.rect(win, "green", (1000, 790, 10, 10))#hp
    if d296 == False:
        pygame.draw.rect(win, "orange", (1035, 790, 10, 10))
    if d297 == False:
        pygame.draw.rect(win, "orange", (1070, 790, 10, 10))
    if d298 == False:
        pygame.draw.rect(win, "orange", (1110, 790, 10, 10))
    if d299 == False:
        pygame.draw.rect(win, "orange", (1000, 895, 10, 10))
    if d300 == False:
        pygame.draw.rect(win, "green", (1000, 930, 10, 10))#hp
    if d301 == False:
        pygame.draw.rect(win, "orange", (1035, 930, 10, 10))
    if d302 == False:
        pygame.draw.rect(win, "orange", (1070, 930, 10, 10))
    if d303 == False:
        pygame.draw.rect(win, "orange", (1105, 930, 10, 10))
    if d304 == False:
        pygame.draw.rect(win, "orange", (1140, 930, 10, 10))
    if d305 == False:
        pygame.draw.rect(win, "green", (1180, 930, 10, 10))#hp
    if d306 == False:
        pygame.draw.rect(win, "orange", (1180, 895, 10, 10))
    if d307 == False:
        pygame.draw.rect(win, "orange", (1215, 930, 10, 10))
    if d308 == False:
        pygame.draw.rect(win, "orange", (1250, 930, 10, 10))
    if d309 == False:
        pygame.draw.rect(win, "orange", (1285, 930, 10, 10))
    if d310 == False:
        pygame.draw.rect(win, "orange", (1320, 930, 10, 10))
    if d311 == False:
        pygame.draw.rect(win, "orange", (1355, 930, 10, 10))
    if d312 == False:
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

