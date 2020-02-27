import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Pacman With BFS")

moveRight = pygame.image.load('right.png')
moveLeft = pygame.image.load('left.png')
moveUp = pygame.image.load('up.png')
moveDown = pygame.image.load('down.png')
fruit = pygame.image.load('fruit.png')

clock = pygame.time.Clock()

x=50
y=50
width = 40
heigth = 60
vel = 5
up = False
down = False
left = False
right= False
moveCount = 0

run = True


def redrawGame():
    global moveCount
    win.fill((0,0,0))
    if moveCount + 1>= 27:
        moveCount = 0

    if left:
        win.blit(moveLeft,(x,y))
        moveCount +=1
    if right:
        win.blit(moveRight,(x,y))
        moveCount +=1
    if up:
        win.blit(moveUp,(x,y))
        moveCount +=1
    if down:
        win.blit(moveDown,(x,y))
        moveCount +=1
    
    win.blit(moveRight,(x,y))

    pygame.display.update()

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
        up = False
        down = False
    elif keys[pygame.K_RIGHT] and (x < 500 - width -vel):
        x += vel
        right = True
        left = False
        up = False
        down = False
    elif keys[pygame.K_UP] and y > vel:
        y -= vel
        up = True
        right = False
        left = False
        down = False
    if keys[pygame.K_DOWN] and (y < 500 - heigth - vel):
        y += vel
        left = False
        right = False
        up = False
        down = True
    else:
        left = False
        right = False
        up = False
        down = False
        moveCount = 0
    
    redrawGame()
    

pygame.quit()