import pygame

pygame.init()
window = pygame.display.set_mode((800, 800))
rect1 = pygame.Rect(*window.get_rect().center, 0, 0).inflate(75, 75)
xpos = 0
ypos = 363
LEFT = 0
RIGHT = 1
keys = [False, False]
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                keys[RIGHT]=False   

    if keys[LEFT] == True:
        vx = -5
        movingx = True
    elif keys[RIGHT] ==True:
        vx = 5
        movingx = True
    else:
        vx = 0
            
    xpos += vx
    rect2 = pygame.Rect(xpos, ypos, 75, 75)

    collide = rect1.colliderect(rect2)
    color = (255, 0, 0) if collide else (255, 255, 255)

    window.fill(0)
    pygame.draw.rect(window, color, rect1)
    pygame.draw.rect(window, (0, 255, 0), rect2, 6, 1)
    pygame.display.flip()

pygame.quit()
exit()
