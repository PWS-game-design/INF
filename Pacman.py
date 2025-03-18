import pygame
import time

pygame.init()

# resolution
resx = 1920
resy = 1080

win = pygame.display.set_mode((resx, resy))
pac_pos = pygame.Vector2(win.get_width() / 5, win.get_height() / 5)

dt = 0

keys = pygame.key.get_pressed()
if keys[pygame.K_w]:
        pac_pos.y -= 300 * dt
if keys[pygame.K_s]:
        pac_pos.y += 300 * dt
if keys[pygame.K_a]:
        pac_pos.x -= 300 * dt
if keys[pygame.K_d]:
        pac_pos.x += 300 * dt