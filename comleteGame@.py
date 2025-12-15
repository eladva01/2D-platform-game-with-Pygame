import pygame ,time, sys, math, random #modules

pygame.init()
screenW =1800
screenH = 500
WIN = pygame.display.set_mode((screenW,screenH)) #screen #window 
pygame.display.set_caption('Platform Game') #window name
score = 0
FONT = pygame.font.SysFont('ariel', 50)
bulletSound = pygame.mixer.Sound('shot.wav')
hitSound=pygame.mixer.Sound('hit.wav')
jumpSound=pygame.mixer.Sound('jump.wav')
stepSound =pygame.mixer.Sound('step.wav')
music = pygame.mixer.music.load('Msic.mp3')
pygame.mixer.music.play(-1)



#SPRITE LV.1 - INSERTING IT AS A VALUE
#putting 27 animation spirites into lists 
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]


bg = pygame.image.load('gamebackground.jpg') #bachround sprite
char = pygame.image.load('standing.png') # character sprite
bg_W =bg.get_width()
scroll = 0
tiles = math.ceil (screenW / bg_W ) 
print ('tiles')


EwalkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
EwalkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]
goblin = pygame.image.load('R10E.png')

WwalkRight = pygame.image.load('wizzardR.jpg')
WwalkLeft = pygame.image.load('wizzardL.jpg')
wizzard1 =pygame.image.load('wizzardR.jpg')

swordR = [pygame.image.load('SR1.png'),pygame.image.load('SR2.png'),pygame.image.load('SR3.png')]
swordL = [pygame.image.load('SL1.png'),pygame.image.load('SL2.png'),pygame.image.load('SL3.png')]
    

class player(object):
    def __init__(self,x, y, width, height):
        self.DMUTx = 850
        self.DMUTy = y +5
        self.DMUTw = width
        self.DMUTh = height
        self.VEL = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right =False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.DMUTx +17, self.DMUTy+11, 29,52)

        

    #pygame.draw.rect(WIN,(225,0,0),(DMUTx, DMUTy, DMUTw, DMUTh))  
    def draw(self,WIN): 
        
     
        if man.walkCount + 1 >= 27:
            man.walkCount = 0# so it will repeat the animation
        
                
        if not (self.standing):
            if man.left:
                WIN.blit(walkLeft[man.walkCount//3], (man.DMUTx, man.DMUTy))  #walkleft is the list              
                man.walkCount +=1
            elif man.right:
                WIN.blit(walkRight[man.walkCount//3], (man.DMUTx, man.DMUTy))
                man.walkCount += 1
                
        else:
            if self.right:
                WIN.blit(walkRight[0], (self.DMUTx, self.DMUTy))
            else:
                WIN.blit(walkLeft[0], (self.DMUTx, self.DMUTy))
        
        

        self.hitbox = (self.DMUTx +21, self.DMUTy+11, 20,22)
        pygame.draw.rect(WIN , (255,0,0), self.hitbox,2)
        if man.right:
            if KEYS [pygame.K_l]:
                blade.hitbox = (self.DMUTx +35, self.DMUTy+5, 30,50)
                pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
        else:
            if KEYS [pygame.K_l]:
                blade.hitbox = (self.DMUTx -5, self.DMUTy+5, 30,50)
                pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
            
        
    def hit(self):
        isJump = False
        self.jumpCount=10
        self.DMUTx = random.randint(0, 1800)
        self.DMUTy = 415
        self.walkCount = 0
        font1 = pygame.font.SysFont('ariel', 50)
        text = font1.render('-5', 1, (255,0,0))
        WIN.blit (text,(185,  8 ))
        pygame.display.update()
        i = 0
        while i < 3:
            pygame.time.delay(70)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

        
class sword(object):
    def __init__(self,x,y,width,height): 
         self.x =x
         self.y =y
         self.w =width
         self.height =height
         self.hitbox = (man.DMUTx +17, man.DMUTy+11, 29,52)
         self.visible = False
         self.swordR = False
         self.swordL = False
    def draw():
        blade.hitbox = (blade.x +21, blade.y+11, 20,22)
        pygame.draw.rect(WIN , (255,0,0), blade.hitbox,2)
           
class enemy(object):   
    EwalkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
    EwalkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
 
    def __init__(self, x, y, width, height, end):
        self.x = 825
        self.y =y + 10
        self.width= width
        self.height = height
        self.end = end +1600
        self.path = (self.x, self.end)
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x +17, self.y+2, 31,57)
        self.health = 10
        self.visible = True

    def draw(self, WIN):
        
                
        self.move()
        if self.visible:
            if self.walkCount +1 >= 33:
                self.walkCount =0

            if self.x <man.DMUTx:
                WIN.blit(self.EwalkRight[self.walkCount //3], (self.x , self.y))
                self.walkCount += 1
            else:
                WIN.blit(self.EwalkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(WIN , (255,0,0), (self.hitbox[0], self.hitbox[1] -20, 50, 10))
            pygame.draw.rect(WIN , (0,0,255), (self.hitbox[0], self.hitbox[1] -20, 50-(5* (10-self.health)), 10))

            
            self.hitbox = (self.x +20, self.y+2, 31,57)
            pygame.draw.rect(WIN, (255,0,0),self.hitbox,2)

    def move(self): 
        if True:
            if man.standing:
                if KEYS [pygame.K_l]:
                    if man.walkCount + 1 >= 9:
                        man.walkCount = 0
                        WIN.blit(swordR[man.walkCount//3],(man.DMUTx, man.DMUTy))
                     
            if  KEYS [pygame.K_l]  :
                if man.walkCount + 1 >= 9:
                    man.walkCount = 0 # so it will repeat the animation        
                
                if man.right:
                        
                    WIN.blit(swordR[man.walkCount//3],(man.DMUTx, man.DMUTy))
                    man.left = False
                    man.right = True 
                        
                            
                if man.left:
                        
                    WIN.blit(swordL[man.walkCount//3],(man.DMUTx, man.DMUTy))
                    man.left = True
                    man.right = False
                        
                
                           
        
        #stepSound.play()
        
               
            if self.x >man.DMUTx:
                self.x -= self.vel
            else:
                self.x += self.vel

        

            
                
    
    def hit(self):

        
        
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = True
            self.health = 10
            self.x =  random.randint (1, 1750)
            self.y  = 415
            
        

        
        
          

class projectile(object):
     def __init__(self,x, y, radius, color, facing):
          self.x =x
          self.y = y
          self.radius =radius 
          self.color = color
          self.facing =facing 
          self.VEL =20 * facing 

     def draw(self,WIN):
            pygame.draw.circle (WIN, self.color,(self.x, self.y), self.radius)
            
            
     
#SPRITE LV2 - INSERTING THE SPRITE VALUE AS A COMMAND
# putting it all in "def" so we will put a shorter line oin the main loop 

def redrawGAME():
        scroll = 0
        WIN.fill((0,0,0))
        WIN.blit( bg, (0,0)) # this is a backround blit . a 'blit' is putting a sprite on the window
        for i in range(0,tiles):
            WIN.blit(bg,(i*bg_W + scroll,0))
            if scroll <= 0:
                scroll = 0
        
        
        
        
            
        

        man.draw(WIN)
        
        goblin.draw(WIN)
        lost_text = FONT.render(' score: '+ str(score) ,1,   'black')
        WIN.blit(lost_text, (10,10))
        


       
        for bullet in bullets:
            bullet.draw(WIN)
        pygame.display.update()


clock = pygame.time.Clock()
FPS = 60

goblin= enemy(100, 410, 64,64, 450)
man =player(300,410,64,64)

blade =sword(300, 410 ,64,64)
shootLoop= 0

bullets =[]





#THE MAIN LOOP
run = True
while run: 
    

    if goblin.visible:
    
        if man.hitbox[1]  < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3]> goblin.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0]  < goblin.hitbox[0] +goblin.hitbox[2]:
         
                        man.hit()
                        score -= 5
                        
        if blade.hitbox[1] < goblin.hitbox[1]+goblin.hitbox[3] and blade.hitbox[1] + goblin.hitbox[3] > goblin.hitbox[1]:
            if blade.hitbox[0] + blade.hitbox[2] > goblin.hitbox[0] and blade.hitbox[0] < goblin.hitbox[2] +goblin.hitbox[0]:
                goblin.hit()
                score += 1 
        
    clock.tick(27) # FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
       
    for bullet in bullets:
        if goblin.visible:
            if bullet.y + bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius> goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] +goblin.hitbox[2]:
            
                    goblin.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))
            
    
        if bullet.x < 1800 and bullet.x > 0:
              bullet.x += bullet.VEL
        else:
             bullets.pop(bullets.index(bullet))
    if shootLoop >0:
        shootLoop+=1
    if shootLoop >3:
        shootLoop=0

    KEYS = pygame.key.get_pressed() #Keyboard commands
   
        
    
                  
    if KEYS [pygame.K_SPACE] and shootLoop ==0:
        bulletSound.play()
        if man.left:
              facing = -1
        else:
              facing = 1
        if len(bullets)< 5:
              bullets.append(projectile(round(man.DMUTx + man.DMUTw //2 +25 *facing),round(man.DMUTy + man.DMUTh//2 ), 9, (0,0,0),facing))

        shootLoop =1
    #if KEYS [pygame.K_w] and DMUTy >= DMUTh -50:
     #   DMUTy -= VEL
    #if KEYS [pygame.K_s] and DMUTy <= screenH - DMUTh:
     #   DMUTy += VEL   
    if KEYS [pygame.K_a] and man.DMUTx >= man.VEL : #LEFT
        man.DMUTx -= man.VEL
        man.left = True
        man.right = False
        man.standing =False
        scroll -= 5
        
    elif KEYS [pygame.K_d] and man.DMUTx <= screenW - man.DMUTw: # RIGHT
        man.DMUTx += man.VEL
        man.left = False
        man.right = True
        man.standing = False
        scroll +=5
        
    else:
        man.standing = True
        man.walkCount = 0
    if not (man.isJump):
        if KEYS[pygame.K_w]: #JUMP
            jumpSound.play()
            man.standing = True
            man.walkCount = 0
            man.isJump = True
    else:    
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.DMUTy -= (man.jumpCount ** 2) *0.3 * neg 
            man.jumpCount -= 0.5
        else:
            man.isJump =False
            man.jumpCount= 10



    
    redrawGAME() #SPRITE LV 3 - PUTTING THE DEF IN THE MAIN LOOP
    # This is the def we did all the blit int
    
pygame.quit() # finish
    
    
    

