import pygame
import time

pygame.init()

# resolution
resx = 1920
resy = 1080

win = pygame.display.set_mode((resx, resy))
player_pos = pygame.Vector2(win.get_width() / 5, win.get_height() / 5)
dt = 0

keys = pygame.key.get_pressed()
if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
if keys[pygame.K_s]:
        player_pos.y += 300 * dt
if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
if keys[pygame.K_d]:
        player_pos.x += 300 * dt