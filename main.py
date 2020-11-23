import pygame
import random
import math

#initializing pygame
pygame.init()


#building screen
screen=pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Invader")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
background=pygame.image.load("index.jpg")

#player
playerImg=pygame.image.load('space-invaders.png')
playerX=370
playerY=480
playerXchange=0
#Enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyXchange=[]
enemyYchange=[]
nu_of_enemies=6
for i in range(nu_of_enemies):

    enemyImg.append(pygame.image.load('space-ship.png'))
    enemyX.append(random.randint(0,730))
    enemyY.append(random.randint(50,150))
    enemyXchange.append(1)
    enemyYchange.append(40)

#Bullet
#ready-we can see the bullet
#fire-we can see the bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bulletXchange=0
bulletYchange=10
bullet_state="ready"
#score
score=0



def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y):
    screen.blit(enemyImg[0],(x,y))
def collisiondetect(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance<27:
        return True
    return False        
      
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))      


#Game Loop
running=True
while running:
    #RGB=Red,Green,Blue  
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        # determining the keystroke is it right or left
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerXchange=-2
            if event.key==pygame.K_RIGHT:
                playerXchange=2
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)   
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerXchange=0
    for i in range(nu_of_enemies):            
        enemyX[i]+=enemyXchange[i]
        if enemyX[i]<=0:
            enemyXchange[i]=1
            enemyY[i]+=enemyYchange[i]
        if enemyX[i]>=736:
            enemyXchange[i]=-1
            enemyY[i]+=enemyYchange[i]
        #collision detection
        collision=collisiondetect(enemyX[i],enemyY[i],bulletX,bulletY)       
        if collision:
            bulletY=480
            bullet_state="ready"  
            score+=1
            print(score) 
            enemyX[i]=random.randint(0,730)
            enemyY[i]=random.randint(50,150)   
        enemy(enemyX[i],enemyY[i])       



    playerX+=playerXchange
    if playerX<=0:
        playerX=0
    if playerX>736:
        playerX=736    
    # bullet Movement    
    if bullet_state is "fire":
        bulletY-=10
        fire_bullet(bulletX,bulletY)
    if bulletY<=0:
        bulletY=480
        bullet_state="ready" 
    
    player(playerX,playerY)
    # enemy(enemyX,enemyY)

    pygame.display.update()     