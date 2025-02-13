import pygame
pygame.init()

# resolution
resx = 1920
resy = 1080

# pygame setup
win = pygame.display.set_mode((resx, resy))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Murder Mystery")

player_pos = pygame.Vector2(win.get_width() / 2, win.get_height() / 2)

while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fil the screen with a color to wipe away anytinh from the last frame
    win.fill("black")

    # RENDER GAME HERE
    pygame.draw.circle(win, "green", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on the screen
    pygame.display.flip()

    # fps limiter
    clock.tick(60) 

    # dt is delta time in seconds since last frame, used for framerate
    dt = clock.tick(60) / 1000

pygame.quit()

